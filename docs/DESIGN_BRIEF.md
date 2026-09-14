# DESIGN BRIEF — Nishant Santosh Jadhav Portfolio

## 1. PERSONAL BRAND

**Name:** Nishant Santosh Jadhav
**Tagline:** AI/ML Student · Python Developer · AI/ML Builder
**Voice:** Precise, technical, unstyled, direct. No marketing fluff. No "passionate about technology" padding.
**Positioning:** A student who builds and deploys real software — not a tutorial-following learner. The portfolio proves capability through a production-grade project (CareerMate.AI) and a documented build process.
**Brand promise:** "Here is what I have actually built, deployed, and can explain."

## 2. TARGET AUDIENCE

Primary: Hiring managers / technical recruiters for Python Developer and ML Engineer internships (India / remote).
Secondary: Technical mentors, peer engineers, and evaluators for academic/project reviews.
Tertiary: Potential collaborators on AI/LLM application work.

Audience needs: Evidence of real code, deployment experience, conceptual understanding, and ability to work end-to-end (not just notebooks).

## 3. CAREER POSITIONING

Current title (resume-grounded): B.E. Artificial Intelligence & Machine Learning Student, Babasaheb Naik College of Engineering, Amravati University. Expected 2028.
Prior education: HSC 81% (2024), SSC 85% (2022).
Experience: BCG Data Science Job Simulation — Customer Churn Prediction (14,606 records, 61 predictive features, Random Forest, evaluated accuracy / recall / ROC-AUC / F1, identified model improvements).

Positioning statement:
> Nishant is an AI/ML student at an accredited engineering college who has already built and deployed a full-stack AI career platform (CareerMate.AI) using Flask, Gemini API, PostgreSQL/Supabase, and Render — and who has completed a production-style data-science simulation at BCG.

No fabricated metrics, no invented companies, no fake awards.

## 4. CENTRAL STORY (Career Arc)

The portfolio follows the master-story progression. Each section reinforces the next.

```text
AI/ML Student
↓
Python Developer
↓
AI/ML Builder
↓
Real Projects  (CareerMate.AI + BCG Simulation)
↓
Production-style Deployment (Render / Supabase / PostgreSQL)
↓
Internship Ready
```

Narrative payoff: By the time a visitor reaches the project section, they have seen education, skills, and experience — then they see a deployed platform with a real architecture diagram and feature list, followed by a clear "internship-ready" closing statement.

## 5. INFORMATION ARCHITECTURE

Single-page experience with anchored sections (navigation via hard-border links):

1. Header / Identity (name + 3-line positioning)
2. The Arc (story progression — 6 stages as visual sequence)
3. Education & Credentials (B.E., HSC/SSC — factual, no embellishment)
4. Experience (BCG Data Science Job Simulation — resume-accurate details)
5. Skills (languages, frameworks, libraries, tools — from resume only)
6. Hero Project — CareerMate.AI (tech stack, architecture, features, deployment)
7. Project Details / Architecture (modular Flask, Gemini API, PostgreSQL, Render)
8. Call to Action / Intern-ready closing

No hidden subpages. No generic "portfolio template" sections. Navigation is minimal and hard-edged.

## 6. VISUAL IDENTITY

**Aesthetic:** Brutalist + Editorial.
- Brutalist: hard borders, exposed grid, raw typography, no decorative softness, no rounded cards, no gradients.
- Editorial: large display type, tight leading, caption-style metadata, asymmetric layouts, deliberate whitespace, text-as-image.

**Hero identity:** Large name (Space Grotesk, ~8-10rem), stacked with the three roles, over a hard-rule divider. No hero image, no background video — the typography is the hero.

**Project identity:** CareerMate.AI gets the largest project block, with architecture diagram, tech tags in monospace, and a hard-border feature list — never buried among equal cards.

**Color identity:** Black ink (#111111) on paper (#F2F0E9) with acid-green accent (#D8FF38) used sparingly — only for critical highlights (hero underline, active state, CTAs). Not used for decorative backgrounds.

## 7. CONTENT HIERARCHY

Hierarchy is enforced by size, weight, and position — not by color alone.
- H1: Name (display scale, regular or bold)
- H2: Section titles (editorial caps or sentence case, large, hard rule below)
- H3: Sub-sections / feature titles (medium, aligned to grid)
- Body: DM Sans, readable at 16-18px on desktop, 16px mobile
- Metadata / captions: IBM Plex Mono, 11-12px, gray/black, always paired with a headline
- Tags / tech labels: IBM Plex Mono, 10-11px, black border, black text, no background fill

Asymmetry rule: No centered hero. Left-aligned content blocks with intentional offset — some sections have content flush-left with a large right-margin; others use a 2-column split with unequal widths (8/4 or 4/8).

## 8. UX STRATEGY

- Navigation: Minimal sticky top bar with section links, hard bottom border. No hamburger on desktop; simple inline links.
- Scroll: Smooth scroll to anchors, but no progress-bar decoration.
- Focus: High-contrast black/white; acid-green only for interactive states and the hero underline. Focus rings visible.
- Scanning: Large headings, short paragraphs, clear metadata captions. No walls of text.
- CTA clarity: One primary closing CTA — "Internship Ready — Let's Talk" (or similar direct statement) — hard-bordered, black background or accent underline.

No popups, no chat widgets, no cookie banners, no generic "subscribe" modules.

## 9. PROJECT STORYTELLING STRATEGY (CareerMate.AI)

CareerMate.AI is the hero project — it must dominate visually and narratively.

Story beats (in order):
- What it is (AI Career Development Platform)
- Why it matters (addresses resume analysis, skill-gap identification, job matching, interview prep)
- How it is built (Flask services, Gemini API, PostgreSQL/Supabase, Render)
- What it proves (full-stack deployment, real database work, API integration, production-style architecture)

Format: One large block, not a card. Architecture diagram (SVG / CSS grid) positioned left or top, feature list right or bottom — never equal-weight cards side-by-side.

No fake user counts, no "500+ users" claims. Only named technologies and named features from the resume.

## 10. RESPONSIVE STRATEGY

- Mobile (~320-480px): Single column. Typography scales down: name ~3.5rem, headings ~1.75rem, body 16px. Hard borders remain; grid collapses to 1 col. Navigation becomes minimal inline or simple list.
- Tablet (~481-1024px): 2-column available. Sections can split 8/4 or 4/8. Typography at desktop scale with tighter margins.
- Desktop (1025px+): 12-column grid, 8/4 or 4/8 splits, large display typography, full editorial spacing.

Breakpoints: 640px / 1024px / 1440px.

No horizontal scroll. No fixed-width containers that break on wide screens.

## 11. MOTION STRATEGY

Minimal and structural — not decorative.
- Entrance: Sections fade in + slide up slightly (0.5s ease-out) when scrolled into view. Only one animation per section, not per element.
- Navigation: No hover animations beyond underline. Links get hard underline on hover (not fade). Active link gets accent underline.
- Hover on tech tags: No scale, no shadow — only a 1px border shift or subtle opacity change.
- No auto-playing animations, no bouncy interactions, no decorative particle effects.
- Respect `prefers-reduced-motion`: All motion disabled when preference is set.

Motion communicates structure, not personality.

---

*Document version: Phase 1 — Design Brief*  
*Source of truth: Nishant_Jadhav.pdf, Claude Code Master Prompt.md (sections 47, 61, 79), prompt.md*  
*Constraints: HTML/CSS/JS + Python + FastAPI only; resume as source of truth; CareerMate.AI hero; Brutalist + Editorial; acid green #D8FF38; hard borders; large typography.*
