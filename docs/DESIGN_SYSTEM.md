# DESIGN SYSTEM — Nishant Jadhav Portfolio

> Brutalist structure + Editorial sophistication.  
> HTML/CSS/JS + Python + FastAPI only. No React/Next/Vue.

---

## 1. TYPOGRAPHY

### Font stack

| Role | Font | Source / Load | Weight | Usage |
|---|---|---|---|---|
| Display / Headings / Hero name | **Space Grotesk** | Google Fonts | 300–700 | H1, section titles, hero name, large editorial type |
| Body / Subheadings / Paragraphs | **DM Sans** | Google Fonts | 300–700 | All body copy, feature descriptions, navigation |
| Metadata / Tags / Monospace elements / Captions | **IBM Plex Mono** | Google Fonts | 400, 500 | Tech tags, dates, captions, architecture labels, code references |

### Type scale (desktop / base 16px)

```
Display / H1 (name):     96px / 110px (space grotesk, 300–400)
H2 (section):              48px / 52px (space grotesk, 400)
H3 (sub / feature):        24px / 28px (dm sans, 500)
Body:                      18px / 26px (dm sans, 400)
Caption / meta:            12px / 16px (ibm plex mono, 400)
Tech tag / label:          11px / 14px (ibm plex mono, 400)
```

### Type rules
- Large type is intentional — never shrink headings to "fit." Let them hang over edges if needed (asymmetric layout allows overflow).
- Line-height for display type is tight (1.05–1.1) to create editorial density.
- Body line-height is generous (1.45–1.6) for readability.
- No letter-spacing on body; slight negative tracking (-0.02em) on H1/H2 for editorial tension.

---

## 2. COLOR

### Palette

| Token | Hex | Role |
|---|---|---|
| INK (primary text / borders) | `#111111` | All text, hard borders, primary buttons |
| PAPER (background) | `#F2F0E9` | Page background, cards, sections |
| ACCENT (acid green) | `#D8FF38` | Hero underline, active nav, primary CTA highlight, critical labels only |
| SECONDARY TEXT | `#555555` | Captions, secondary metadata |
| BORDER | `#111111` | All borders — 1px solid, no light gray borders |

### Usage rules (non-negotiable)
- INK + PAPER = base. Always high contrast (min 10:1).
- ACCENT = sparingly. Only for: hero underline under name, active nav underline, one CTA highlight, very occasional key label.
- No gradients. No purple, no blue, no orange decorative colors.
- No background fills for tags — tags are black text on paper with 1px black border.

---

## 3. GRID

### Layout system
- **Desktop:** 12-column grid. Containers max-width 1440px, padding 24–48px side.
- **Split sections:** 8/4 or 4/8 — never equal 6/6 for editorial asymmetry.
- **Mobile:** 1 column (4-column concept collapsed).
- **Tablet (768–1023):** 2-column available, 8/4 with reduced padding.

### Grid rules
- Gutter: 24px between columns.
- No full-width images — images/content sit inside grid with hard borders.
- Asymmetric: left content can extend into right margin; right content can be flush to edge.

---

## 4. BORDERS

### Border rules (brutalist)
- All structural borders: `1px solid #111111`
- No rounded corners. Zero `border-radius`. All rectangles.
- Section dividers: full-width 1px line, no shadow.
- Card / block borders: 1px solid black around all content blocks. No drop shadow.
- Focus / active states: 2px solid #D8FF38 (accent) — only when focused, never decorative.

---

## 5. BUTTONS

### Primary button
- Text: DM Sans, 14px, 500, `#111111`
- Background: `#F2F0E9` (paper) for light mode / `#111111` for dark/contrast variant
- Border: `1px solid #111111`
- No rounded corners (`border-radius: 0`)
- Hover: background inverts to `#111111`, text to `#F2F0E9`; or accent underline appears
- Padding: 14px 28px (desktop), 12px 20px (mobile)

### Secondary / Link button
- No border, no background
- Underline on hover (hard 1px, `#111111`)
- Active / current page: underline + `#D8FF38` underline or left-border indicator

---

## 6. SPACING

### Scale (8pt base, editorial)

```
XS:   8px
S:    16px
M:    24px
L:    48px
XL:   80px
XXL:  120px
```

### Rules
- Section padding top/bottom: 80–120px (editorial whitespace is part of the design).
- Between major sections: full-width 1px border divider, plus 80px spacing.
- Between heading and body: 24px.
- Between elements in a feature list: 16px.
- No arbitrary padding — spacing derives from the scale.

---

## 7. RESPONSIVE

### Breakpoints
- `640px` — small / mobile
- `1024px` — tablet
- `1440px` — desktop wide

### Behavior
- Single column below 640px.
- 2-column sections activate at 768px (8/4 splits).
- Typography scales at each breakpoint: H1 from 96px → 64px → 48px → 36px.
- Navigation collapses to inline links at 640px; no hamburger required (minimal nav items).
- Images / diagrams scale to 100% width with hard borders preserved.

---

## 8. MOTION

### Principles
- Minimal, structural, not decorative.
- `prefers-reduced-motion: reduce` disables all animation.

### Specifics
- **Section entrance:** `opacity` 0→1 + `translateY(16px)`→0 over 0.5s ease-out (only when scrolled into view, one per section).
- **Nav links:** No hover animation except underline; active state gets `#D8FF38` underline.
- **Tech tags:** No scale, no shadow on hover — only opacity shift (`0.7`→`1`) and border color stays black.
- **No auto-play, no bounce, no decorative motion.**

---

## 9. ACCESSIBILITY

### Requirements
- Color contrast: minimum 10:1 for all text/body (INK on PAPER exceeds this).
- Focus indicators: visible 2px `#D8FF38` outline on interactive elements.
- Semantic HTML: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`.
- Skip-link: visible on focus for keyboard users.
- No content hidden behind hover-only states.
- All images / diagrams have `alt` text describing content (not decorative).
- Font sizes never below 16px for body (respects browser zoom).
- `aria-label` on nav links and buttons.

---

## 10. COMPONENT REFERENCE

### Section block
- Background: `#F2F0E9`
- Border: `1px solid #111111` bottom (divider)
- Padding: `120px 48px` desktop / `80px 24px` mobile
- Max-width: 1440px centered

### Feature / architecture list item
- Left: label (IBM Plex Mono, 11px, black)
- Right: description (DM Sans, 16px, black)
- Bottom border: `1px solid #111111` (light weight)
- No cards — flat list with hard rules

### Hero identity block
- Large name: Space Grotesk, 96px, 300, `#111111`, line-height 1.0
- Role stack: DM Sans, 18px, 400, `#555555` or `#111111`
- Underline: 4px solid `#D8FF38`, width 60% of name width, positioned below name
- No background image

### Project hero (CareerMate.AI)
- Large title: Space Grotesk, 48px
- Tech tags: IBM Plex Mono, 11px, black border, black text, no fill
- Architecture diagram: CSS grid / SVG, bordered, black lines only
- Feature list: hard-border blocks or flat list with dividers
- No equal-weight cards — asymmetric layout (diagram left 8/4, text right 4/8 or reverse)

---

## 11. IMPLEMENTATION NOTES

- Load fonts via `<link>` in `<head>` (Google Fonts: Space Grotesk, DM Sans, IBM Plex Mono).
- No CSS frameworks — vanilla CSS / minimal build.
- FastAPI serves static HTML/CSS/JS from `src/portfolio/` (or `static/`).
- All assets embedded or served from same origin — no external dependencies beyond fonts.
- CSS uses custom properties (`--ink`, `--paper`, `--accent`) for token consistency.

---

*Document version: Phase 3 — Design System*  
*Follows Phase 1 (DESIGN_BRIEF.md) and Phase 2 (execution planning)*  
*Constraints validated: Stack = HTML/CSS/JS + Python + FastAPI. Resume = sole source. CareerMate.AI = hero. Brutalist + Editorial. Acid green #D8FF38. Large typography. Hard borders. Asymmetric. No fabricated metrics.*
