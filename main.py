from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.get("/style.css")
async def serve_css():
    with open("style.css", "r") as f:
        css_content = f.read()
    return Response(content=css_content, media_type="text/css")c