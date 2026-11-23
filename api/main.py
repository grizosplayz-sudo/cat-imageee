from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="background-color: #111; text-align: center; font-family: sans-serif;">
            <h1 style="color: white;">Server is working!</h1>
            <a href="/download" style="background-color: red; color: white; padding: 15px 30px; text-decoration: none; font-size: 20px; border-radius: 8px;">
                DOWNLOAD ZIP
            </a>
        </body>
    </html>
    """

@app.get("/download")
def download():
    file_path = "api/discordnuker.zip"
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path, 
            filename="discordnuker.zip", 
            media_type="application/zip"
        )
    return {"error": "File not found on server."}
