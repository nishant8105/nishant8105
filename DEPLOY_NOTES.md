# Deployment Notes — D:\Portfolio

## Placeholder URLs that MUST be updated after Render URL is confirmed

Files: `src/portfolio/app.py`

- `/sitemap.xml` contains `https://nishant-jadhav.onrender.com/`
- `/robots.txt` contains `https://nishant-jadhav.onrender.com/sitemap.xml`

These are placeholder URLs. Once the actual Render deployment URL is known, update the URLs in `app.py` (lines 31, 37) to match the real domain.

DO NOT hard-code a fake URL before deployment; update after the URL is confirmed.
