import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response
from starlette.requests import Request
from pathlib import Path

app = FastAPI(title="Nishant Jadhav — Portfolio")

BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

from jinja2 import Environment, FileSystemLoader
jinja_env = Environment(loader=FileSystemLoader(str(BASE_DIR / "templates")))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    template = jinja_env.get_template("index.html")
    return HTMLResponse(content=template.render(request=request))

@app.get("/health")
async def health():
    return {"status": "ok", "service": "portfolio", "version": "1.0.0"}

@app.get("/sitemap.xml")
async def sitemap():
    content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://nishant-jadhav.onrender.com/</loc><lastmod>2026-09-14</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>
</urlset>"""
    return Response(content=content, media_type="application/xml")

@app.get("/robots.txt")
async def robots():
    content = "User-agent: *\nAllow: /\nSitemap: https://nishant-jadhav.onrender.com/sitemap.xml\n"
    return Response(content=content, media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("src.portfolio.app:app", host="0.0.0.0", port=port)
