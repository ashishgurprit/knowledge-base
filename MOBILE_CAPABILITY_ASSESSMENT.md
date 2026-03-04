# Mobile Capability Assessment
**Date**: 2026-03-04
**Prepared for**: Streamlined Development — Knowledge Base
**Scope**: React Native / Expo / Capacitor ecosystem, cross-referenced against top apps in 6 target verticals

---

## Table of Contents

1. [Existing Capabilities (What We Have)](#1-existing-capabilities)
2. [Top App Feature Analysis by Category](#2-top-app-feature-analysis)
3. [Capability Gaps (Ranked)](#3-capability-gaps)
4. [Top 10 Repo Recommendations](#4-top-10-repo-recommendations)
5. [Suggested New Skills to Build](#5-suggested-new-skills)

---

## 1. Existing Capabilities

### 1.1 Mobile-Specific Skills (5 Dedicated Skills)

| Skill | File | Coverage |
|-------|------|----------|
| `capacitor-mobile-app` | `.claude/skills/capacitor-mobile-app/SKILL.md` | Project setup, tab navigation, native plugins, Zustand state, Cloudflare Workers backend, i18n, IAP via RevenueCat, analytics, store submission |
| `mobile-ux-patterns` | `.claude/skills/mobile-ux-patterns/SKILL.md` | Skeleton loaders, onboarding carousels, remote config/feature flags, native share sheets, maps and geofencing |
| `mobile-resilience` | `.claude/skills/mobile-resilience/SKILL.md` | Offline-first / action queue, Sentry crash reporting, permission flows with pre-prompt dialogs, forced/soft app update gates |
| `mobile-communication` | `.claude/skills/mobile-communication/SKILL.md` | In-app chat UI, Expo push notifications, Supabase realtime subscriptions, omni-channel routing |
| `revenuecat-monetization` | `.claude/skills/revenuecat-monetization/SKILL.md` | RevenueCat SDK setup (Capacitor + React Native), subscription offerings, entitlements, paywall UI, Stripe webhook integration, purchase analytics |

### 1.2 Adjacent Skills That Apply to Mobile

| Skill | Relevance |
|-------|-----------|
| `auth-universal` | Auth flows, OAuth, JWT — applies to mobile login screens |
| `payment-processing-universal` | PCI-DSS base patterns, Stripe — mobile payments foundation |
| `stripe-subscription-billing` | Web Stripe patterns that extend to mobile PWA/hybrid |
| `analytics-universal` | Event tracking schemas — applies to mobile analytics |
| `notification-universal` | Notification delivery patterns — supplements mobile-communication |
| `sms-universal` | SMS OTP, 2FA — used in mobile auth flows |
| `file-upload-universal` | File/image upload patterns — used in mobile media features |
| `media-processing-universal` | Image/video processing — used in mobile content creation |
| `accessibility-wcag` | WCAG accessibility — web-focused but overlaps with mobile a11y |
| `journaling-cbt-universal` | Mental health app patterns for CBT journaling flows |
| `ecommerce-universal` | E-commerce logic applicable to mobile commerce apps |
| `app-store-optimization` | ASO checklists, screenshot specs, metadata optimization |
| `design-system` | Color, typography, component tokens |
| `visual-design-consultant` | UI/UX design patterns |
| `electron-desktop-app` | Tangentially useful: desktop patterns contrast with mobile patterns |

### 1.3 What the Existing Mobile Skills Cover Well

- Cross-platform project scaffolding (Capacitor + Expo/React Native)
- Tab navigation and screen-level architecture
- Subscription monetization (RevenueCat full lifecycle)
- Push notification delivery and handling
- Real-time chat and presence
- Offline queue and sync on reconnect
- Crash reporting (Sentry integration)
- Permission request flows with pre-prompt UX
- Forced / soft app update gates
- Skeleton loading and shimmer animations
- Onboarding carousels with first-launch detection
- Feature flags and A/B testing with remote config
- Native share sheets and deep link generation
- Maps, geocoding, and geofencing

---

## 2. Top App Feature Analysis

### 2.1 AI Productivity / AI Assistant Apps

**Top apps**: ChatGPT, Claude, Gemini, Perplexity, Motion, Reclaim, Copilot, Notion AI

| # | Feature | Why It Wins |
|---|---------|-------------|
| 1 | **Streaming AI responses** (token-by-token) | Perceived speed; user engagement during generation |
| 2 | **Conversation history & search** | Core retention driver — users return for past conversations |
| 3 | **Voice input / Speech-to-text** | Hands-free use cases (driving, cooking, gym) — 2-3x usage frequency |
| 4 | **Voice output / Text-to-speech** | Accessibility + multitasking |
| 5 | **On-device AI inference** | Privacy, speed, offline capability (ExecuTorch, TFLite, CoreML) |
| 6 | **File/image attachment in prompts** | Multimodal queries significantly expand use cases |
| 7 | **AI Calendar & task scheduling** (Motion/Reclaim) | Deeply sticky — requires recurring permission/access |
| 8 | **Widget support** (home screen) | Ambient AI access without opening the app |
| 9 | **Siri/Google Assistant shortcuts** | OS-level integration dramatically increases daily active use |
| 10 | **Custom personas / system prompts** | Power-user personalization drives premium conversion |

**Market stats**: GenAI apps earned $1.3B in IAP revenue in 2024 (+180% YoY). Average subscription $10.20/month. Top-tier paid subscriptions generate $120B/year globally across all app categories.

### 2.2 Healthcare / Mental Health / Wellness Apps

**Top apps**: Calm, Headspace, BetterHelp, Woebot, Moodfit, Noom, MyFitnessPal, Whoop, Oura

| # | Feature | Why It Wins |
|---|---------|-------------|
| 1 | **Daily mood tracking & journaling** | Habit formation — 45% weekly usage among retained users |
| 2 | **CBT/DBT exercises with progress tracking** | Clinical legitimacy; measurable improvement reduces churn (39% cite "no progress" as dropout reason) |
| 3 | **Guided audio sessions (meditation, sleep)** | Calm's 300+ sleep stories drive the highest session length of any category |
| 4 | **Streak/gamification mechanics** | Gamification increases usage frequency by 30% |
| 5 | **HealthKit / Health Connect integration** | Passive data reduces friction; integrates sleep, HRV, steps |
| 6 | **Personalized AI coach** | 62% AI engagement rise; AI nudges reduce early abandonment |
| 7 | **Biometric authentication** | HIPAA-friendly access; critical for sensitive data apps |
| 8 | **Provider/therapist matching & booking** | Hybrid digital+human model commands 2-4x premium pricing |
| 9 | **Wearable device sync** (Apple Watch, Fitbit) | Passive data collection reduces user friction by 60% |
| 10 | **End-to-end encryption + HIPAA compliance UI patterns** | Trust signal; required for health data handling |

**Market stats**: ~52% of wellness app users quit within weeks. Personalized progress tracking retains 45% more users. Premium subscription adoption at 38%.

### 2.3 Business / CRM / Client Management Apps

**Top apps**: HubSpot, Pipedrive, Zoho, Salesforce, Streak, Monday.com, Twenty (open-source)

| # | Feature | Why It Wins |
|---|---------|-------------|
| 1 | **Pipeline/kanban views** | Visual deal management — #1 mobile CRM differentiator |
| 2 | **Offline access with sync** | Sales reps work in dead zones; offline is non-negotiable |
| 3 | **Call logging + automatic email tracking** | Reduces manual data entry; drives CRM adoption |
| 4 | **Push notifications for deal updates** | Real-time signals increase response speed by 40% |
| 5 | **Business card / contact scan (OCR)** | Physical-to-digital conversion at conferences |
| 6 | **Voice-to-CRM** (dictate notes, log calls) | Reduces friction for field sales teams |
| 7 | **AI-suggested next actions** | CoPilot-style guidance increases deal close rates |
| 8 | **Customizable fields + forms** | Enterprise buyers require flexibility without code changes |
| 9 | **Team presence / activity feeds** | Collaboration signal that reduces overlap in large sales teams |
| 10 | **Biometric login + SSO (SAML/OAuth)** | Enterprise security requirement; gatekeeps B2B deals |

### 2.4 E-Commerce / Marketplace Apps

**Top apps**: Shopify Mobile, WooCommerce, Etsy, Amazon, ASOS, eBay, Depop, Vinted

| # | Feature | Why It Wins |
|---|---------|-------------|
| 1 | **AR product preview** (try before you buy) | AR/VR reduces returns and increases conversion; mainstream in 2025-2026 |
| 2 | **One-tap checkout** (Apple Pay, Google Pay, BNPL) | Each additional checkout step loses 20% of users |
| 3 | **AI-powered personalized product recommendations** | Implementing advanced personalization delivers up to 40% revenue uplift |
| 4 | **Visual/image search** | Camera-based product discovery used by 35% of Gen Z shoppers |
| 5 | **Post-purchase upsell / cross-sell flows** | ReConvert-style thank-you page upsells increase AOV by 15-25% |
| 6 | **Price drop & back-in-stock alerts** | Creates urgency and return visits without advertising spend |
| 7 | **Loyalty/rewards program** | Repeat purchase rate 5x higher for loyalty members |
| 8 | **Live shopping / shoppable video** | TikTok Shop proved this converts at 3-5x vs static product pages |
| 9 | **Seller analytics dashboard** (for marketplace apps) | Empowers sellers to self-optimize; reduces support load |
| 10 | **Returns management UX** | Returner-style exchange-first flows retain 40% of revenue |

### 2.5 Content Creation / Social Media Tools

**Top apps**: Canva, CapCut, Adobe Express, Buffer, Sprout Social, Proom AI, Later

| # | Feature | Why It Wins |
|---|---------|-------------|
| 1 | **AI video generation from text/image** | Sora, Runway Gen-3, Pika — reducing professional video production from hours to seconds |
| 2 | **Short-form video editor with templates** | CapCut model: template-first editing removes the blank canvas barrier |
| 3 | **AI caption/hashtag generation** | Reduces time-to-post by 70%; highest ROI feature for social tools |
| 4 | **Content calendar with scheduling** | Retention anchor — users return daily to manage queue |
| 5 | **Brand kit / asset library** | Enforces brand consistency; required for team plans (enterprise upsell) |
| 6 | **Platform-native content optimization** | Auto-resize + format for Instagram, TikTok, LinkedIn, Pinterest |
| 7 | **Background removal / object removal** | Magical UX moment — instant value delivery |
| 8 | **Collaboration / team workspaces** | Unlocks business tier pricing (3-10x individual plan price) |
| 9 | **Analytics + performance reporting** | Closes the loop; justifies subscription renewal |
| 10 | **AI avatar / digital presenter** | Proom AI model — personalized video creation without camera-shy barrier |

### 2.6 Marketing Automation Tools

**Top apps**: Braze, CleverTap, OneSignal, Klaviyo, Pushwoosh, Iterable, MoEngage, Customer.io

| # | Feature | Why It Wins |
|---|---------|-------------|
| 1 | **Visual journey/canvas builder** | Braze's Canvas Flow — non-technical marketers build complex sequences |
| 2 | **Unified omnichannel campaigns** (push + email + SMS + in-app + WhatsApp + RCS) | Single canvas with combined reporting — 2026 standard |
| 3 | **Behavioral cohort segmentation** | Real-time segments based on in-app events drive 3x higher CTR |
| 4 | **A/B + multivariate testing** | Statistically validated testing reduces guesswork |
| 5 | **AI channel affinity optimization** | Routes message to the channel each user is most likely to open |
| 6 | **In-app message builder** (banners, modals, carousels) | No-deployment feature announcements inside the live app |
| 7 | **Quiet hours / frequency capping** | Reduces notification fatigue; protects sender reputation |
| 8 | **Predictive churn scoring** | Surfaces at-risk users before they leave |
| 9 | **Deep link routing in notifications** | Notification → specific in-app screen (not just app open) |
| 10 | **Attribution / campaign ROI dashboard** | Justifies marketing spend; closes budget approval loop |

---

## 3. Capability Gaps (Ranked)

Scoring: Each gap is scored across three dimensions (1-5 scale each):
- **Freq**: Frequency across the 6 verticals (how many categories need this)
- **Rev**: Revenue impact (direct monetization or conversion uplift)
- **Ret**: Retention impact (how much it keeps users coming back)

| Rank | Gap | Freq | Rev | Ret | Total | Notes |
|------|-----|------|-----|-----|-------|-------|
| 1 | **On-device AI / Local LLM inference** | 5 | 5 | 5 | **15** | Critical for AI productivity, health, CRM. ExecuTorch + TFLite. No skill exists. |
| 2 | **Biometric authentication** (Face ID / Touch ID) | 5 | 4 | 5 | **14** | Required for health, CRM, finance. `expo-local-authentication` patterns missing. |
| 3 | **Home screen widgets** (iOS / Android) | 5 | 4 | 5 | **14** | Ambient presence = highest-retention mobile feature. No skill exists. |
| 4 | **Native payments** (Apple Pay, Google Pay, payment sheet) | 5 | 5 | 3 | **13** | `stripe-react-native` payment sheet pattern missing. RevenueCat skill covers IAP but not wallet payments. |
| 5 | **HealthKit / Health Connect / Fitness data integration** | 4 | 4 | 5 | **13** | Required for wellness, fitness, healthcare. No skill exists. |
| 6 | **AI streaming UI** (token streaming, typewriter effect, abort) | 5 | 5 | 3 | **13** | All AI apps need this. `mobile-communication` has chat but not AI stream patterns. |
| 7 | **Voice input/output** (STT/TTS with wake word) | 5 | 4 | 4 | **13** | Expo Speech + Whisper integration. No skill exists. |
| 8 | **AR / 3D product viewer** | 3 | 5 | 4 | **12** | E-commerce + healthcare + CRM demos. ViroReact + react-native-ar. No skill exists. |
| 9 | **Deep link attribution / install attribution** | 4 | 5 | 3 | **12** | AppsFlyer / Branch integration for campaign ROI. No skill. |
| 10 | **App tracking transparency / privacy UX** (ATT, SKAdNetwork) | 4 | 5 | 3 | **12** | iOS 14.5+ requirement. Impacts ad revenue. No skill exists. |
| 11 | **Wearable device integration** (Apple Watch, Wear OS) | 3 | 4 | 5 | **12** | Whoop/Oura model. `react-native-health` patterns missing. |
| 12 | **Visual / camera search** | 3 | 5 | 4 | **12** | VisionCamera + ML Kit object detection. E-commerce + CRM (business card scan). |
| 13 | **Live Activity / Dynamic Island** (iOS) | 3 | 4 | 4 | **11** | Delivery tracking, live sports, fitness metrics on lock screen. |
| 14 | **Dark mode / system theming** (full implementation pattern) | 5 | 2 | 4 | **11** | All apps need this. Covered in capacitor skill but not a standalone mobile skill. |
| 15 | **Gamification** (streaks, points, badges, leaderboards) | 4 | 4 | 5 | **13** | CBT apps, fitness, e-commerce loyalty. Journaling-cbt-universal partially covers this for one domain. |
| 16 | **OCR / document scanning** (receipts, business cards, ID) | 3 | 4 | 3 | **10** | CRM contact scan, expense apps, healthcare intake. Vision Camera + ML Kit. |
| 17 | **Short-form video recording + editing** | 2 | 5 | 4 | **11** | Content creation apps. CapCut model. No skill. |
| 18 | **In-app messaging / campaign tools integration** (OneSignal, Braze SDK) | 4 | 4 | 4 | **12** | In-app banners, modals, carousels without a deployment. `mobile-communication` covers push but not in-app CMS. |
| 19 | **Accessibility — WCAG mobile** (VoiceOver/TalkBack, dynamic type) | 4 | 2 | 3 | **9** | `accessibility-wcag` exists but is web-focused. |
| 20 | **App Clips / Instant Apps** | 2 | 4 | 3 | **9** | Frictionless onboarding without install. Increasingly adopted in e-commerce. |

### Summary of Coverage by Gap Category

| Category | Have | Missing |
|----------|------|---------|
| Communication | Push, chat, realtime, omnichannel routing | AI streaming UI, in-app campaign builder SDK |
| Monetization | RevenueCat IAP, subscriptions | Native wallet payments (Apple Pay / Google Pay) |
| Auth / Security | OAuth, JWT (web-focused) | Biometric auth, ATT/privacy transparency, secure enclave |
| AI / ML | LLM via API (agent skills) | On-device AI inference, voice STT/TTS, visual search / OCR |
| Health / Fitness | CBT journaling patterns | HealthKit/Health Connect, wearable sync |
| UX / Engagement | Onboarding, skeletons, remote config, sharing, maps | Gamification engine, widgets, dark mode theming system |
| E-Commerce | ecommerce-universal (web patterns) | AR product viewer, visual search, live shopping |
| Analytics | analytics-universal (general) | Deep link / install attribution (AppsFlyer/Branch) |
| Platform Integration | Store submission checklist | Live Activity/Dynamic Island, App Clips, Siri shortcuts |

---

## 4. Top 10 Repo Recommendations

Repos are prioritized by gap rank, GitHub stars, activity, and Expo/React Native ecosystem fit.

### Repo 1: react-native-vision-camera
**Gap addressed**: Visual / camera search, OCR, on-device AI frame processing
**GitHub**: https://github.com/mrousavy/react-native-vision-camera
**Stars**: 7,500+
**Why**: The most powerful camera library for React Native. Supports Frame Processors for running ML models (TFLite, CoreML) directly on camera frames — enabling OCR, barcode scan, object detection, face recognition, and AR overlays. Uses JSI (New Architecture native). Marc Rousavy also maintains `react-native-fast-tflite`. Essential for e-commerce visual search, CRM business card scan, and healthcare intake scanning.

### Repo 2: software-mansion/react-native-executorch
**Gap addressed**: On-device AI inference (Gap #1)
**GitHub**: https://github.com/software-mansion/react-native-executorch
**Stars**: 1,500+
**Why**: Declarative way to run local LLM and ML models in React Native powered by ExecuTorch (Meta's mobile ML runtime). Supports Llama 3, CoreML on iOS Neural Engine, Vulkan on Android. Requires Expo SDK 54. Critical for privacy-first AI apps, offline AI features, and reducing API costs. The most strategic capability gap.

### Repo 3: mrousavy/react-native-fast-tflite
**Gap addressed**: On-device AI with TensorFlow Lite (Gap #1 complement)
**GitHub**: https://github.com/mrousavy/react-native-fast-tflite
**Stars**: 1,000+
**Why**: Zero-copy TensorFlow Lite inference with GPU acceleration (CoreML/Metal on iOS, OpenGL/NNAPI on Android). Works within VisionCamera frame processors for real-time inference. Complementary to react-native-executorch — TFLite for lightweight models (classification, object detection), ExecuTorch for LLMs.

### Repo 4: stripe/stripe-react-native
**Gap addressed**: Native wallet payments — Apple Pay, Google Pay, payment sheet (Gap #4)
**GitHub**: https://github.com/stripe/stripe-react-native
**Stars**: 2,100+
**Why**: Official Stripe SDK. Covers Payment Sheet (single-call UI), Apple Pay, Google Pay, Link, and 3D Secure. Expo plugin available. Our `revenuecat-monetization` skill covers IAP but this addresses the separate gap for one-time payments, marketplace transactions, and non-subscription purchases. Critical for e-commerce, CRM deal payments, and healthcare billing.

### Repo 5: ReactVision/viro (ViroReact)
**Gap addressed**: AR / 3D product viewer (Gap #8)
**GitHub**: https://github.com/ReactVision/viro
**Stars**: 2,400+
**Why**: Leading AR/VR library for React Native, supporting ARKit (iOS) and ARCore (Android). Expo config plugin available. Enables 3D product placement in room (e-commerce), medical visualization (healthcare), and interactive demos (CRM). Includes starter kits for Expo + TypeScript.

### Repo 6: agencyenterprise/react-native-health
**Gap addressed**: HealthKit / Health Connect / fitness data integration (Gap #5)
**GitHub**: https://github.com/agencyenterprise/react-native-health
**Stars**: 1,600+
**Why**: Complete React Native package for Apple HealthKit (iOS). Combined with `react-native-fitness` or `kilohealth/rn-fitness-tracker` for Google Health Connect (Android), this pair enables passive health data collection — the foundational feature of any wellness or fitness app. Requires dev build (not Expo Go). Integrates steps, sleep, HRV, calories, workouts.

### Repo 7: AppsFlyerSDK/appsflyer-react-native-plugin
**Gap addressed**: Deep link attribution / install attribution (Gap #9)
**GitHub**: https://github.com/AppsFlyerSDK/appsflyer-react-native-plugin
**Stars**: 350+
**Why**: Official AppsFlyer SDK for React Native. Enables install attribution (which ad/campaign drove the install), deferred deep linking (user lands on a specific screen after install), re-attribution, and in-app event tracking for campaign ROI. Critical for any app running paid acquisition — without attribution, ad spend is untrackable. Alternative: `branch-io/rn-branch-deep-linking-attribution`.

### Repo 8: ImBIOS/RNWidget (+ Expo widgets approach via @bacons/apple-targets)
**Gap addressed**: Home screen widgets (Gap #3)
**GitHub**: https://github.com/ImBIOS/RNWidget
**Expo Config Plugin**: `@bacons/apple-targets` (https://github.com/EvanBacon/expo-apple-targets)
**Stars**: 200+ (RNWidget) / 800+ (EvanBacon's apple-targets)
**Why**: Widgets require native Swift (iOS) and Kotlin (Android) — React Native/JS cannot run inside a widget directly. Communication happens via App Groups (shared containers). This repo plus Expo's `@bacons/apple-targets` approach provides the reference patterns for iOS home screen widgets and Lock Screen widgets. Highest retention impact of all gaps — ambient presence without app open. Live Activity support is also covered by this pattern.

### Repo 9: SelfLender/react-native-biometrics
**Gap addressed**: Biometric authentication — Face ID, Touch ID, fingerprint (Gap #2)
**GitHub**: https://github.com/SelfLender/react-native-biometrics
**Stars**: 1,200+
**Why**: Creates cryptographic key pairs protected by biometrics (stored in iOS Secure Enclave / Android Keystore). Superior to expo-local-authentication for apps requiring cryptographic signing (banking, healthcare, enterprise CRM). Enables biometric-protected storage of tokens and credentials — the security pattern required by HIPAA-adjacent apps and B2B enterprise buyers.

### Repo 10: software-mansion/react-native-reanimated (+ react-native-gesture-handler)
**Gap addressed**: Advanced animation and gesture patterns for gamification, video editors, drag-and-drop (complements Gaps #15, #17)
**GitHub**: https://github.com/software-mansion/react-native-reanimated
**Stars**: 8,500+
**Why**: The foundational animation library for New Architecture React Native. Enables 60/120fps animations running on the UI thread, spring physics, shared element transitions, and swipeable gesture interactions. Required for any gamification system (animated streaks, confetti, badges), content creation tools (video timeline scrubbing, drag-and-drop), and high-polish UX moments. Works with react-native-gesture-handler (same org, 5,800+ stars).

---

## 5. Suggested New Skills to Build

Prioritized by combined gap score and strategic importance to the project portfolio.

### Priority 1 — Critical (Build First)

#### Skill: `mobile-on-device-ai`
**Addresses**: Gaps #1, #6 (on-device AI + AI streaming UI)
**Description**: On-device AI inference for React Native/Expo apps — ExecuTorch LLM execution, TFLite model integration, AI response streaming UI, voice-to-AI (STT input), typewriter/abort patterns. Local model management, model downloading with progress, and fallback to cloud API when model unavailable.
**Consumes repos**: `react-native-executorch`, `react-native-fast-tflite`, `react-native-vision-camera`
**Key modules**:
- `on-device-llm` — ExecuTorch Llama setup, token streaming, chat history
- `tflite-inference` — Classification, object detection, GPU delegates
- `ai-streaming-ui` — Typewriter component, partial render, abort controller
- `voice-ai-input` — expo-speech/Whisper STT, wake word, hands-free mode

#### Skill: `mobile-biometric-auth`
**Addresses**: Gap #2
**Description**: Biometric authentication patterns — Face ID / Touch ID / fingerprint with Secure Enclave key management, fallback PIN, HIPAA-appropriate credential storage, and enterprise SSO integration. Covers both expo-local-authentication (basic) and react-native-biometrics (cryptographic keypair) approaches.
**Consumes repos**: `SelfLender/react-native-biometrics`, `expo-local-authentication`
**Key modules**:
- `biometric-auth-basic` — Expo LocalAuthentication patterns
- `biometric-keypair` — Secure Enclave / Android Keystore key management
- `biometric-token-vault` — Secure encrypted token storage behind biometrics
- `biometric-enterprise` — SAML/SSO with biometric local unlock

#### Skill: `mobile-home-screen-widgets`
**Addresses**: Gap #3
**Description**: Home screen widget and Live Activity patterns for iOS and Android. iOS WidgetKit in Swift (via Expo Config Plugin + @bacons/apple-targets), Android App Widgets in Kotlin, shared data via App Groups / SharedPreferences, Live Activity for dynamic lock screen content (delivery tracking, workout metrics, live scores).
**Consumes repos**: `ImBIOS/RNWidget`, `EvanBacon/expo-apple-targets`
**Key modules**:
- `ios-widget-swift` — WidgetKit extension, timeline provider, App Group data bridge
- `android-widget-kotlin` — AppWidgetProvider, RemoteViews, data refresh
- `live-activity` — ActivityKit, Dynamic Island, lock screen content
- `widget-data-bridge` — JS → native data handoff patterns

### Priority 2 — High Value (Build Second)

#### Skill: `mobile-native-payments`
**Addresses**: Gap #4
**Description**: Native wallet payments for React Native/Expo — Stripe Payment Sheet, Apple Pay, Google Pay, BNPL (Afterpay/Klarna via Stripe), and marketplace payment splits. Complements existing `revenuecat-monetization` (which handles App Store IAP only).
**Consumes repos**: `stripe/stripe-react-native`
**Key modules**:
- `stripe-payment-sheet` — Complete payment UI in one call
- `apple-pay-setup` — Merchant ID, entitlements, presentation
- `google-pay-setup` — Google Pay API, test environment
- `marketplace-payments` — Stripe Connect for seller payouts, escrow

#### Skill: `mobile-health-fitness`
**Addresses**: Gaps #5, #11
**Description**: Health data integration for React Native/Expo — HealthKit (iOS), Health Connect (Android), passive workout tracking, sleep and HRV data, wearable device sync (Apple Watch via WatchConnectivity, Fitbit, Whoop API). Includes privacy-first patterns and HIPAA-relevant data handling.
**Consumes repos**: `agencyenterprise/react-native-health`, `kilohealth/rn-fitness-tracker`
**Key modules**:
- `healthkit-ios` — Read/write steps, sleep, HRV, workouts
- `health-connect-android` — Google Health Connect v2 API patterns
- `wearable-sync` — Apple Watch WatchConnectivity data bridge
- `health-data-visualization` — Trend charts, goal rings (Activity Ring model)

#### Skill: `mobile-voice-interface`
**Addresses**: Gap #7
**Description**: Voice input/output patterns — Speech-to-text (Expo Speech, Whisper API, on-device Whisper), text-to-speech (AVFoundation / TTS), wake word detection, voice commands navigation, dictation UX patterns. Hands-free mode for healthcare, productivity, and field CRM.
**Consumes repos**: `react-native-executorch` (Whisper model), `expo-speech`
**Key modules**:
- `speech-to-text` — Expo Speech Recognition, streaming transcription
- `text-to-speech` — Platform TTS, custom voice selection
- `voice-commands` — Intent parsing, navigation commands
- `dictation-ux` — Waveform visualization, word-by-word display

#### Skill: `mobile-ar-camera`
**Addresses**: Gaps #8, #12, #16
**Description**: AR product viewer, visual search, OCR / document scanning, and barcode/QR scanning using VisionCamera + ML Kit + ViroReact. Covers e-commerce product placement in room, business card OCR for CRM, receipt scanning, ID verification, and QR code deep links.
**Consumes repos**: `ReactVision/viro`, `mrousavy/react-native-vision-camera`, `mrousavy/react-native-fast-tflite`
**Key modules**:
- `ar-product-viewer` — ViroReact 3D model placement in ARKit/ARCore
- `visual-search` — VisionCamera + ML Kit image classification
- `ocr-document-scan` — ML Kit text recognition, document rectification
- `barcode-qr` — Camera barcode scanning, QR deep link routing

### Priority 3 — Medium (Build Third)

#### Skill: `mobile-attribution-analytics`
**Addresses**: Gaps #9, #10
**Description**: Install attribution (AppsFlyer / Branch), deferred deep linking, SKAdNetwork / App Tracking Transparency (ATT) consent flow, campaign ROI tracking, and mobile measurement partner (MMP) integration. Complements existing `analytics-universal` and `utm-attribution-tracking` (web-focused).
**Consumes repos**: `AppsFlyerSDK/appsflyer-react-native-plugin`
**Key modules**:
- `install-attribution` — AppsFlyer setup, first-open attribution, cohort tracking
- `deferred-deep-links` — Deferred link resolution after install
- `att-consent-flow` — iOS 14.5+ ATT permission request UX patterns
- `skadnetwork` — Conversion value configuration, postback handling

#### Skill: `mobile-gamification`
**Addresses**: Gap #15
**Description**: Gamification engine for mobile apps — streak tracking, XP/points systems, badge/achievement unlock, leaderboards, level progression, and reward animations. Patterns from Duolingo (streak + notifications), Headspace (mood rings), Strava (segments + challenges). Built on react-native-reanimated for 60fps reward animations.
**Consumes repos**: `software-mansion/react-native-reanimated`, `software-mansion/react-native-gesture-handler`
**Key modules**:
- `streak-engine` — Daily streak calculation, grace periods, freeze mechanics
- `points-levels` — XP accumulation, level-up logic, progress bars
- `badge-achievements` — Achievement unlock events, badge gallery
- `leaderboards` — Global/friends/cohort ranking with pagination
- `reward-animations` — Confetti, sparkle, shake, ring completion animations

#### Skill: `mobile-in-app-messaging`
**Addresses**: Gap #18
**Description**: In-app messaging campaign patterns without deployment — banners, modals, carousels, tooltips, and spotlight overlays that can be triggered remotely. Covers OneSignal in-app messaging, Braze Content Cards patterns, and a self-hosted alternative using Supabase remote config. Complements existing `mobile-communication` (push) and `mobile-ux-patterns` (remote config).
**Key modules**:
- `onesignal-in-app` — OneSignal in-app message templates and triggers
- `content-cards` — Braze/self-hosted content card feed
- `spotlight-overlay` — Feature discovery tooltips and coach marks
- `survey-nps` — In-app NPS, CSAT, and rating prompts

---

## 6. Strategic Summary

### Highest ROI Actions (Next 30 Days)

1. **Build `mobile-on-device-ai` skill** — Covers the fastest-growing revenue segment in mobile (GenAI apps +180% YoY). Applies to every project category.

2. **Build `mobile-biometric-auth` skill** — Required blocker for any health, finance, or enterprise CRM app. Currently missing entirely.

3. **Add `stripe/stripe-react-native` to knowledge-base sources** — One repo, immediate coverage of Apple Pay / Google Pay / payment sheet gap. Existing `revenuecat-monetization` skill should reference this explicitly.

4. **Build `mobile-home-screen-widgets` skill** — Highest retention impact of all gaps. Widgets are the #1 re-engagement surface in iOS and are now table stakes for AI productivity apps.

5. **Add `react-native-executorch` and `react-native-vision-camera` to `knowledge-base/repos.yaml`** — These are the two most strategically important repos not yet in the knowledge base.

### Projects Most Affected by Gaps

| Project (from PROJECTS.md) | Top Missing Capabilities |
|---------------------------|--------------------------|
| `potentialz-app` (health/wellness) | mobile-biometric-auth, mobile-health-fitness, mobile-gamification |
| `SeepAndroidApp` | mobile-on-device-ai, mobile-ar-camera, mobile-native-payments |
| `gts-marketplace-apps` | mobile-ar-camera, mobile-native-payments, mobile-attribution-analytics |
| `insta-based-shop` | mobile-native-payments, mobile-ar-camera, mobile-gamification |
| `cardgamepro` | mobile-gamification, mobile-on-device-ai |
| `claude-essay-agent` | mobile-on-device-ai, mobile-voice-interface, mobile-home-screen-widgets |

---

*Sources consulted for this assessment:*
- [State of Mobile AI Apps 2025 — Sensor Tower](https://sensortower.com/blog/2025-state-of-mobile-ai-is-everywhere-on-mobile)
- [App Monetization Statistics 2026 — AppVerticals](https://www.appverticals.com/blog/mobile-app-monetization-statistics/)
- [21 Advanced Mental Health App Features — AppInventiv](https://appinventiv.com/blog/mental-health-app-features/)
- [5 eCommerce Mobile App Trends 2026 — AppBrew](https://www.appbrew.com/blogs/ecommerce-mobile-app-trends)
- [Top Mobile Marketing Automation 2025 — Business of Apps](https://www.businessofapps.com/marketplace/marketing-automation/)
- [React Native ExecuTorch — Expo Blog](https://expo.dev/blog/how-to-run-ai-models-with-react-native-executorch)
- [react-native-executorch GitHub](https://github.com/software-mansion/react-native-executorch)
- [react-native-vision-camera GitHub](https://github.com/mrousavy/react-native-vision-camera)
- [stripe-react-native GitHub](https://github.com/stripe/stripe-react-native)
- [ReactVision/viro GitHub](https://github.com/ReactVision/viro)
- [agencyenterprise/react-native-health GitHub](https://github.com/agencyenterprise/react-native-health)
- [AppsFlyerSDK/appsflyer-react-native-plugin GitHub](https://github.com/AppsFlyerSDK/appsflyer-react-native-plugin)
- [ImBIOS/RNWidget GitHub](https://github.com/ImBIOS/RNWidget)
- [SelfLender/react-native-biometrics GitHub](https://github.com/SelfLender/react-native-biometrics)
- [Best Mobile CRM Apps 2026 — Zendesk](https://www.zendesk.com/sell/crm/mobile/)
- [Top Mental Health Apps 2025 — Digital Health Insider](https://www.digitalhealthinsider.org/p/top-mental-health-apps-in-2025)
- [14 AI Tools for Social Media Content Creation — Buffer](https://buffer.com/resources/ai-social-media-content-creation/)
