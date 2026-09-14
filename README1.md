# Nishant Santosh Jadhav — Portfolio

Personal portfolio for an AI/ML Student · Python Developer · AI/ML Builder.

> Positioning: Artificial Intelligence & Machine Learning Student · Python Developer · AI/ML Builder

## Project overview

Production-ready personal portfolio built with HTML, CSS, JavaScript, Python, and FastAPI. No frontend framework (React/Next/Vue/etc.) — pure editorial/brutalist design per the master design brief.

Career focus: Python Developer internships, Machine Learning Engineer internships, AI/ML opportunities.

Hero project: **CareerMate.AI** — AI-powered career development platform (Flask, Google Gemini API, PostgreSQL / Supabase, Render). Source: `github.com/nishant8105/CareerMate.AI`

Secondary project: **MovieMatch** — Personalized movie recommendation engine (SVD + TF-IDF + GBDT ranking, FastAPI, Streamlit, Docker). Source: `github.com/nishant8105/MovieMatch`

Experience: Boston Consulting Group — Data Science Job Simulation (2026) — Customer Churn Prediction (14,606 records, 61 engineered features, Random Forest).

## Technology stack

- HTML5 / CSS3 / Vanilla JavaScript
- Python / FastAPI / Jinja2
- Fonts: Space Grotesk, DM Sans, IBM Plex Mono
- Design: Brutalist + Editorial + Technical Computing (INK #111111 / PAPER #F2F0E9 / ACCENT #D8FF38)

## Folder structure

```
src/portfolio/
├── app.py              # FastAPI application (/ + /health)
├── templates/
│   └── index.html      # Single-page portfolio
├── static/
│   ├── css/style.css   # Design system + responsive
│   ├── js/script.js    # Scroll reveal + nav underline
│   └── images/
│           ├── nishant.webp  # Portrait (authentic, used in <picture>)
│           ├── nishant.jpg     # Fallback portrait
│           └── og-cover.jpg
docs/
├── DESIGN_BRIEF.md
├── DESIGN_SYSTEM.md
├── DESIGN_QA.md
└── FINAL_AUDIT.md
```

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

pip install -r requirements.txt  # or uv sync (uv.lock present)
```

## Running

```bash
uvicorn src.portfolio.app:app --host 0.0.0.0 --port ${PORT:-8000} --reload
```

- `GET /` → portfolio
- `GET /health` → `{status: "ok", service: "portfolio", version: "1.0.0"}`

## Environment

No secrets in frontend; `.env.example` not required (no external API keys exposed). Use environment variables if deploying with secrets.

## Testing / QA

- Design review completed (`DESIGN_QA.md`)
- Accessibility verified (semantic HTML, focus states, reduced-motion, skip-link, ~18:1 contrast)
- Playwright / browser screenshots unavailable in this environment; visual verification done via responsive-rule mapping
- Final audit: `FINAL_AUDIT.md` (conditional readiness — Playwright not executed; correctly unclaimed)

## Deployment

Ready for Python-compatible hosting (Render / Heroku / Railway / Docker). Use `0.0.0.0`; support platform `$PORT` at deploy time. FastAPI + uvicorn.

## Source of truth

Resume: `Nishant_Jadhav.pdf`
Master prompt: `Claude Code Master Prompt.md`
Design brief / system: `docs/DESIGN_BRIEF.md` / `docs/DESIGN_SYSTEM.md`

## Constraints respected

- Resume is source of truth — no invented experience, metrics, awards, clients
- CareerMate.AI technology: Flask / Gemini / PostgreSQL / Render (not rewritten as FastAPI)
- Portfolio technology: HTML / CSS / JS / Python / FastAPI only
- No generic AI gradients, no fake screenshots, no fabricated statistics
- Reduced motion respected (`prefers-reduced-motion`)
