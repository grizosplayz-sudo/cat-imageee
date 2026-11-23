from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Server is working!</h1><a href='/download'>Download ZIP</a>"

@app.get("/download")
def download():
    file_path = os.path.join("api", "discordnuker.zip")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            file_data = f.read()
        headers = {
            'Content-Disposition': 'attachment; filename="discordnuker.zip"',
            'Content-Type': 'application/zip'
        }
        return Response(content=file_data, headers=headers, media_type="application/zip")
    return {"error": "File not found on server."}
