#!/usr/bin/env python3
"""
Knowledge Base Fetcher
======================
Extracts README files and folder structure from GitHub repos.
Stores them locally for reference when building skills, lessons, and modules.

Usage:
  python fetch.py add <github-url> [--notes "why tracking this"] [--depth 2]
  python fetch.py update           # Update repos stale > 30 days
  python fetch.py update --force   # Force-update all repos
  python fetch.py list             # Show all tracked repos + freshness
  python fetch.py show <name>      # Print extracted knowledge for a repo
  python fetch.py search <query>   # Search across all knowledge

Requirements:
  pip install pyyaml requests
  gh auth login (recommended for higher rate limits)
"""

import sys
import os
import re
import json
import base64
import subprocess
import textwrap
from pathlib import Path
from datetime import datetime, timedelta, timezone

# Fix Windows console encoding
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

try:
    import yaml
except ImportError:
    print("Missing dependency: pip install pyyaml requests")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("Missing dependency: pip install pyyaml requests")
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────

BASE_DIR     = Path(__file__).parent
SOURCES_DIR  = BASE_DIR / "sources"
REPOS_FILE   = BASE_DIR / "repos.yaml"
UPDATE_DAYS  = 30          # Refresh interval
MAX_DEPTH    = 2           # Default folder depth for README crawl
MAX_DIRS     = 30          # Max subdirectories to crawl per repo

# ── GitHub API ────────────────────────────────────────────────────────────────

def _gh_headers():
    """Build auth headers — use gh CLI token if available."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        try:
            result = subprocess.run(
                ["gh", "auth", "token"], capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                token = result.stdout.strip()
        except Exception:
            pass
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def gh_get(path: str) -> dict | list | None:
    """GET from GitHub API. path = '/repos/owner/repo/...' """
    url = f"https://api.github.com{path}"
    resp = requests.get(url, headers=_gh_headers(), timeout=15)
    if resp.status_code == 404:
        return None
    if resp.status_code == 403:
        print(f"  ⚠ Rate limited. Set GITHUB_TOKEN env var or run: gh auth login")
        return None
    resp.raise_for_status()
    return resp.json()


def decode_content(data: dict) -> str | None:
    """Decode base64 file content from GitHub API response."""
    if not data or data.get("encoding") != "base64":
        return None
    try:
        return base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    except Exception:
        return None

# ── URL parsing ───────────────────────────────────────────────────────────────

def parse_github_url(url: str) -> tuple[str, str]:
    """Extract owner and repo from any GitHub URL format."""
    url = url.rstrip("/").removesuffix(".git")
    m = re.search(r"github\.com[/:]([^/]+)/([^/]+)", url)
    if not m:
        raise ValueError(f"Cannot parse GitHub URL: {url}")
    return m.group(1), m.group(2)

# ── Extraction ────────────────────────────────────────────────────────────────

def fetch_readme(owner: str, repo: str, path: str = "") -> str | None:
    """Fetch README content at a given path within the repo."""
    endpoint = f"/repos/{owner}/{repo}/readme"
    if path:
        endpoint += f"?ref=HEAD"
        # GitHub readme endpoint doesn't support subpaths directly
        # Fall back to listing directory and finding README manually
        contents = gh_get(f"/repos/{owner}/{repo}/contents/{path}")
        if not contents or not isinstance(contents, list):
            return None
        readme_file = next(
            (f for f in contents
             if f.get("type") == "file"
             and f.get("name", "").upper().startswith("README")),
            None
        )
        if not readme_file:
            return None
        data = gh_get(f"/repos/{owner}/{repo}/contents/{readme_file['path']}")
        return decode_content(data)
    else:
        data = gh_get(endpoint)
        return decode_content(data)


def fetch_tree(owner: str, repo: str, max_depth: int) -> list[dict]:
    """Get repo tree, returning only directories up to max_depth."""
    data = gh_get(f"/repos/{owner}/{repo}/git/trees/HEAD?recursive=1")
    if not data or "tree" not in data:
        return []

    dirs = []
    for item in data["tree"]:
        if item.get("type") != "tree":
            continue
        path = item["path"]
        depth = path.count("/") + 1
        # Skip hidden dirs, test dirs, build artifacts
        parts = path.split("/")
        if any(p.startswith(".") or p.startswith("_") or
               p in {"node_modules", "dist", "build", "__pycache__",
                     ".git", "vendor", ".venv", "venv", "env"}
               for p in parts):
            continue
        if depth <= max_depth:
            dirs.append({"path": path, "depth": depth})

    return dirs[:MAX_DIRS]


def fetch_repo_meta(owner: str, repo: str) -> dict:
    """Fetch repo metadata from GitHub API."""
    data = gh_get(f"/repos/{owner}/{repo}")
    if not data:
        return {}
    return {
        "description": data.get("description") or "",
        "stars":       data.get("stargazers_count", 0),
        "language":    data.get("language") or "",
        "topics":      data.get("topics", []),
        "homepage":    data.get("homepage") or "",
        "license":     (data.get("license") or {}).get("spdx_id") or "",
        "default_branch": data.get("default_branch", "main"),
        "archived":    data.get("archived", False),
        "size_kb":     data.get("size", 0),
    }


def extract_repo(owner: str, repo: str, depth: int = MAX_DEPTH) -> dict:
    """Full extraction: meta + root README + subdirectory READMEs."""
    print(f"  → Fetching metadata...")
    meta = fetch_repo_meta(owner, repo)
    if not meta:
        raise RuntimeError(f"Repo {owner}/{repo} not found or inaccessible")

    print(f"  → Fetching root README...")
    root_readme = fetch_readme(owner, repo)

    print(f"  → Scanning directory tree (depth={depth})...")
    dirs = fetch_tree(owner, repo, depth)

    dir_readmes = {}
    for d in dirs:
        path = d["path"]
        print(f"  → README: {path}/", end="", flush=True)
        content = fetch_readme(owner, repo, path)
        if content:
            dir_readmes[path] = content
            print(" ✓")
        else:
            print(" (none)")

    return {
        "owner":       owner,
        "repo":        repo,
        "url":         f"https://github.com/{owner}/{repo}",
        "meta":        meta,
        "root_readme": root_readme,
        "dir_readmes": dir_readmes,
        "dirs":        [d["path"] for d in dirs],
        "fetched_at":  datetime.now(timezone.utc).isoformat(),
    }

# ── Storage ───────────────────────────────────────────────────────────────────

def save_repo(data: dict) -> Path:
    """Write extracted repo knowledge to sources/{repo}/."""
    repo_dir = SOURCES_DIR / data["repo"]
    repo_dir.mkdir(parents=True, exist_ok=True)

    # _meta.json — structured metadata
    meta_path = repo_dir / "_meta.json"
    meta_payload = {
        "url":         data["url"],
        "owner":       data["owner"],
        "repo":        data["repo"],
        "fetched_at":  data["fetched_at"],
        **data["meta"],
        "dirs_crawled": data["dirs"],
        "readmes_found": list(data["dir_readmes"].keys()),
    }
    meta_path.write_text(json.dumps(meta_payload, indent=2), encoding="utf-8")

    # Root README
    if data["root_readme"]:
        (repo_dir / "README.md").write_text(data["root_readme"], encoding="utf-8")

    # Subdir READMEs
    for path, content in data["dir_readmes"].items():
        subdir = repo_dir / path
        subdir.mkdir(parents=True, exist_ok=True)
        (subdir / "README.md").write_text(content, encoding="utf-8")

    return repo_dir


def load_registry() -> dict:
    if not REPOS_FILE.exists():
        return {"repos": []}
    with open(REPOS_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("repos", [])
    return data


def save_registry(data: dict):
    tmp = REPOS_FILE.with_suffix(".yaml.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    os.replace(tmp, REPOS_FILE)  # atomic on all platforms


def get_meta(repo_name: str) -> dict | None:
    meta_path = SOURCES_DIR / repo_name / "_meta.json"
    if not meta_path.exists():
        return None
    with open(meta_path, encoding="utf-8") as f:
        return json.load(f)


def is_stale(repo_name: str, days: int = UPDATE_DAYS) -> bool:
    meta = get_meta(repo_name)
    if not meta:
        return True
    fetched = meta.get("fetched_at")
    if not fetched:
        return True
    dt = datetime.fromisoformat(fetched)
    return datetime.now(timezone.utc) - dt > timedelta(days=days)

# ── Commands ──────────────────────────────────────────────────────────────────

def cmd_add(url: str, notes: str = "", depth: int = MAX_DEPTH):
    owner, repo = parse_github_url(url)

    # Quick duplicate check before doing any network work
    registry = load_registry()
    if any(r.get("repo") == repo for r in registry["repos"]):
        print(f"Already tracking: {repo}")
        print(f"  Run: python fetch.py update --force  to refresh")
        return

    print(f"\nAdding: {owner}/{repo}")
    data = extract_repo(owner, repo, depth)
    repo_dir = save_repo(data)

    entry = {
        "url":   data["url"],
        "owner": owner,
        "repo":  repo,
        "depth": depth,
    }
    if notes:
        entry["notes"] = notes

    # Re-read registry right before writing so parallel adds don't overwrite each other
    registry = load_registry()
    if any(r.get("repo") == repo for r in registry["repos"]):
        print(f"\n✓ Extracted (already registered by concurrent run): {repo}")
    else:
        registry["repos"].append(entry)
        save_registry(registry)

    meta = data["meta"]
    print(f"\n✓ Added: {repo}")
    print(f"  {meta.get('description', '')}")
    print(f"  Stars: {meta.get('stars', 0):,} | Language: {meta.get('language', '?')} | Topics: {', '.join(meta.get('topics', []))}")
    print(f"  READMEs extracted: {1 + len(data['dir_readmes'])}")
    print(f"  Saved to: {repo_dir}")


def cmd_update(force: bool = False):
    registry = load_registry()
    if not registry["repos"]:
        print("No repos tracked yet. Run: python fetch.py add <github-url>")
        return

    updated = 0
    skipped = 0
    for entry in registry["repos"]:
        repo = entry["repo"]
        owner = entry["owner"]
        depth = entry.get("depth", MAX_DEPTH)

        if not force and not is_stale(repo):
            meta = get_meta(repo)
            fetched = meta.get("fetched_at", "unknown")[:10] if meta else "unknown"
            print(f"  ✓ {repo}: fresh (last: {fetched})")
            skipped += 1
            continue

        print(f"\n  ↻ Updating: {owner}/{repo}")
        try:
            data = extract_repo(owner, repo, depth)
            save_repo(data)
            print(f"  ✓ {repo}: updated")
            updated += 1
        except Exception as e:
            print(f"  ✗ {repo}: FAILED — {e}")

    print(f"\nDone: {updated} updated, {skipped} already fresh")


def cmd_list():
    registry = load_registry()
    if not registry["repos"]:
        print("No repos tracked. Run: python fetch.py add <github-url>")
        return

    print(f"\n{'Repo':<35} {'Stars':>6}  {'Updated':<12}  Description")
    print("─" * 90)
    for entry in registry["repos"]:
        repo = entry["repo"]
        meta = get_meta(repo) or {}
        stars = meta.get("stars", 0)
        fetched = (meta.get("fetched_at") or "never")[:10]
        stale = " ⚠" if is_stale(repo) else ""
        desc = (meta.get("description") or "")[:45]
        print(f"  {repo:<33} {stars:>6,}  {fetched:<12}{stale}  {desc}")

    print(f"\nTotal: {len(registry['repos'])} repos")
    print(f"Stale threshold: {UPDATE_DAYS} days")


def cmd_show(repo_name: str):
    repo_dir = SOURCES_DIR / repo_name
    if not repo_dir.exists():
        print(f"Not found: {repo_name}")
        print("Run: python fetch.py list")
        return

    meta = get_meta(repo_name) or {}
    print(f"\n{'='*60}")
    print(f"  {repo_name}")
    print(f"  {meta.get('url', '')}")
    print(f"{'='*60}")
    print(f"  Description : {meta.get('description', '')}")
    print(f"  Language    : {meta.get('language', '?')}")
    print(f"  Stars       : {meta.get('stars', 0):,}")
    print(f"  Topics      : {', '.join(meta.get('topics', []))}")
    print(f"  Last updated: {(meta.get('fetched_at') or '')[:10]}")
    print(f"  READMEs     : {len(meta.get('readmes_found', []))} subdirectories")
    print()

    readme_path = repo_dir / "README.md"
    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
        # Show first 60 lines
        lines = content.splitlines()[:60]
        print("\n".join(lines))
        if len(content.splitlines()) > 60:
            print(f"\n... [{len(content.splitlines()) - 60} more lines in {readme_path}]")


def cmd_search(query: str):
    query_lower = query.lower()
    results = []

    for repo_dir in sorted(SOURCES_DIR.iterdir()):
        if not repo_dir.is_dir():
            continue
        repo_name = repo_dir.name
        meta = get_meta(repo_name) or {}

        # Search in meta fields
        score = 0
        matches = []

        desc = (meta.get("description") or "").lower()
        topics = " ".join(meta.get("topics", [])).lower()
        if query_lower in desc:
            score += 3
            matches.append(f"description: {meta['description'][:80]}")
        if query_lower in topics:
            score += 2
            matches.append(f"topics: {topics}")
        if query_lower in repo_name.lower():
            score += 2
            matches.append("repo name")

        # Search READMEs (top-level only for speed)
        readme_path = repo_dir / "README.md"
        if readme_path.exists():
            content = readme_path.read_text(encoding="utf-8", errors="replace").lower()
            count = content.count(query_lower)
            if count > 0:
                score += min(count, 5)
                # Find first matching line
                for line in readme_path.read_text(encoding="utf-8", errors="replace").splitlines():
                    if query_lower in line.lower():
                        matches.append(f"README: {line.strip()[:100]}")
                        break

        if score > 0:
            results.append((score, repo_name, meta, matches))

    if not results:
        print(f"\nNo results for: {query}")
        return

    results.sort(reverse=True)
    print(f"\nSearch results for '{query}': {len(results)} repos\n")
    for score, name, meta, matches in results:
        print(f"  [{score:2d}] {name}")
        print(f"       {meta.get('description', '')[:70]}")
        for m in matches[:2]:
            print(f"       → {m}")
        print()


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help", "help"):
        print(__doc__)
        return

    cmd = args[0]

    if cmd == "add":
        if len(args) < 2:
            print("Usage: python fetch.py add <github-url> [--notes 'why'] [--depth 2]")
            sys.exit(1)
        url = args[1]
        notes = ""
        depth = MAX_DEPTH
        for i, a in enumerate(args[2:], 2):
            if a == "--notes" and i + 1 < len(args):
                notes = args[i + 1]
            if a == "--depth" and i + 1 < len(args):
                depth = int(args[i + 1])
        cmd_add(url, notes=notes, depth=depth)

    elif cmd == "update":
        force = "--force" in args
        cmd_update(force=force)

    elif cmd == "list":
        cmd_list()

    elif cmd == "show":
        if len(args) < 2:
            print("Usage: python fetch.py show <repo-name>")
            sys.exit(1)
        cmd_show(args[1])

    elif cmd == "search":
        if len(args) < 2:
            print("Usage: python fetch.py search <query>")
            sys.exit(1)
        cmd_search(" ".join(args[1:]))

    else:
        print(f"Unknown command: {cmd}")
        print("Commands: add, update, list, show, search")
        sys.exit(1)


if __name__ == "__main__":
    main()
