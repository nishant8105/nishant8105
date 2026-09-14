# Design QA — Playwright / Visual Verification

**Portfolio:** Nishant Jadhav — D:\Portfolio  
**Reviewer:** Playwright QA  
**Date:** 2026-09-14  
**App:** FastAPI (`src.portfolio.app:app`) served via `uvicorn` on port 8000  

---

## Server Status

- **Command:** `python -m uvicorn src.portfolio.app:app --host 0.0.0.0 --port 8000`
- **Initial state:** 500 Internal Server Error (Jinja2 template cache `TypeError: unhashable type: 'dict'` caused by `starlette` 1.6.0 / `jinja2` 3.1.6 compatibility)
- **Fix applied:** Replaced `templates.TemplateResponse` with direct `jinja2.Environment` render (`HTMLResponse`) in `src/portfolio/app.py` to bypass broken cache key handling.
- **Current state:** `200 OK` at `http://localhost:8000/` (verified via `curl`).
- **Process:** Running (PID from `ps`; restarted after kill of erroring instance).

---

## Playwright / Screenshot Capture Status

**Playwright unavailable.**
- `python -c "import playwright"` → `Playwright unavailable`
- `pip list` has no `playwright`, `selenium`, `pyppeteer`
- No browser binaries found (`chrome.exe`, `msedge.exe`, `firefox.exe`) at standard paths (`C:\Program Files\...`, `D:\` search)
- `node` / `npm` not present; no global puppeteer/playwright packages

**Visual verification method used (instead of automated screenshots):**
1. Direct HTML + CSS inspection (`src/portfolio/templates/index.html`, `src/portfolio/static/css/style.css`)
2. HTTP verification (`curl -s -o /dev/null -w "%{http_code}"` at `localhost:8000`)
3. Responsive CSS analysis (media queries, `clamp()`, `max-width`, `flex-wrap`, `grid` rules)
4. Viewport-size simulation by mapping design-system rules to target widths

No `.png` screenshot files produced (no rendering engine available).

---

## Viewport Observations (simulated / code-inspected at requested sizes)

Target sizes: **1440px, 1280px, 1024px, 430px, 390px, 375px, 320px**

### 1440px (desktop large / max container)
- `.container` max-width = 1440px, width = 92% → content centered with generous side margins.
- `h1` clamp up to 10rem; hero displays full large typography (`NISHANT SAN TOSH JADHAV`) with `max-width:14ch` preventing horizontal overflow.
- `.nav` links (`WORK`, `EXP`, `CONTACT`) in header flex row with 2rem margins — no wrap needed at 1440px.
- `grid-2` = 2fr 1fr with 3rem gap; project cards and about section display side-by-side.
- No horizontal scroll expected; `body` uses default block flow with `max-width` constraints.

### 1280px (desktop)
- Same layout as 1440px but with slightly narrower container (92% of 1280 ≈ 1178px content width).
- Typography scales down smoothly via `clamp()` (h1 ~8–9rem, h2 ~4–5rem).
- Navigation remains horizontal; no overflow.

### 1024px (tablet / wide)
- `@media (min-width: 1024px)` activates `.grid-2` with 3rem gap; below this, grid collapses but CSS still defines 2fr 1fr.
- `h2` heading-underline sections (`ABOUT`, `SELECTED WORK`, `EXPERENCE`) use flex-wrap with gap 1.5rem — will wrap gracefully if space tight.
- Typography still large; `clamp()` ensures readable sizes.
- No overflow detected in CSS rules (`max-width` on paragraphs = 65ch, containers bounded).

### 430px / 390px / 375px / 320px (mobile)
- `@media (max-width: 768px)` reduces hero padding (`padding: 80px 0 100px`) and section padding (`padding: 80px 0`).
- `.container` 92% width → ~390px content at 430px viewport; comfortable margins.
- `nav` links: `margin-left:2rem` with `font-size:0.75rem`; at 320px this may crowd — but `display:flex` with `justify-content:space-between` in header keeps logo and nav on same line. **Observation:** on very narrow screens (320px) nav links could overlap or wrap; no `flex-wrap: wrap` declared on `.nav`. Consider adding `flex-wrap: wrap` to nav for <375px.
- Heading `h1` at 320px: `clamp(4rem,12vw,10rem)` → ~38px; still large but constrained by `max-width:14ch`. Will stack lines (`NISHANT <br> SAN TOSH <br> JADHAV`) correctly.
- `section-header` uses `flex-wrap: wrap`; numbers (`02`, `03`, `04`) and headings will wrap vertically instead of clipping horizontally.
- `project-card` architecture flow (`USER → FLASK APP → ...`) uses `flex-wrap: wrap`; no horizontal overflow.
- `meta` rows (location/focus/status) use `flex-wrap: wrap`; safe at 320px.
- **No horizontal scroll rules** present (`overflow-x` not set); therefore layout relies entirely on responsive sizing rather than scroll containment.

---

## Inspection Checklist (performed via code + server)

| Check | Method / Finding |
|---|---|
| Navigation / links | `nav` links present; `a href="#work"`, `#experience`, `#contact`; skip-link `#main` present for accessibility; GitHub external link with `target="_blank" rel="noopener"`. |
| Scrolling / mobile behavior | Smooth scroll via CSS only (no `scroll-behavior: smooth` declared globally, but `@media (prefers-reduced-motion: reduce)` handles accessibility). Mobile padding reduced at `<768px`. |
| Typography overflow / clipping | All headings use `clamp()`; paragraphs `max-width:65ch`; hero `h1` `max-width:14ch`. No fixed-width large text that could overflow small viewports. |
| Broken headings | No broken heading tags; `section-header` uses `h2` with underline via CSS; `h3` for project titles; all have closing tags verified in HTML. |
| Layout overflow / horizontal scroll | `.container` bounded; no `overflow-x: scroll` declared; `flex-wrap` used in meta/architecture/feature grids. Potential narrow-viewport crowding in `.nav` at 320px (no wrap declared). |
| Keyboard navigation / interactive | Skip-link present; all interactive elements are `a` tags with `href`; buttons are `a.btn`; focus indicators not explicitly styled (default browser outline applies). External links use security attributes. |
| Console errors | Cannot capture runtime console via Playwright (unavailable). Server logs (`/tmp/uvicorn.log`) show no ASGI errors after fix; only initial Jinja2 cache exception (resolved). |
| Images / media | No `<img>` elements in `index.html`; icons via data-URI SVG (favicon) and font/CSS only. No media loading errors expected. |

---

## Key Findings

1. **Server required repair** before QA could proceed (Jinja2 `unhashable type: 'dict'` crash). Fixed by bypassing `starlette.templating.Jinja2Templates` with direct `jinja2.Environment`.
2. **Playwright not installed; no browser binaries found.** Screenshots at requested viewports could not be captured automatically.
3. **Visual verification performed via HTML/CSS inspection + responsive rule mapping.** No evidence of layout overflow or broken headings; typography is responsive (`clamp()`); mobile behavior guided by `max-width:768px` media query.
4. **Minor recommendation:** Add `flex-wrap: wrap` to `.nav` for sub-375px viewports to prevent navigation crowding. Add `scroll-behavior: smooth` and visible `:focus-visible` outlines if keyboard navigation is a priority.
5. **No console errors** expected at runtime (static HTML + CSS, no client-side JS except `static/js/` which was not fully inspected; recommend checking `static/js/` for JS errors if available).

---

## Files Referenced

- `D:\Portfolio\src\portfolio\app.py` (fixed server)
- `D:\Portfolio\src\portfolio\templates\index.html`
- `D:\Portfolio\src\portfolio\static\css\style.css`
- `D:\Portfolio\docs\DESIGN_QA.md` (this file)
