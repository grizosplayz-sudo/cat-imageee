from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="background-color: #111; text-align: center; font-family: sans-serif; margin: 0; padding: 0;">
            <img src="https://cat-imageee-mbo9.vercel.app/" alt="Cover" style="width: 100%; max-width: 800px; margin-top: 20px;">
            <br><br>
            <a href="/download" style="background-color: red; color: white; padding: 15px 30px; text-decoration: none; font-size: 20px; font-weight: bold; border-radius: 8px;">
                DOWNLOAD ZIP
            </a>
        </body>
    </html>
    """

@app.get("/download")
def download():
    # The path should be relative to the project root
    file_path = "api/discordnuker.zip"
    
    # Check if the file exists to prevent a 500 crash
    if not os.path.exists(file_path):
        return {"error": "File not found on server. The ZIP may not have been included in the build."}, 404

    return FileResponse(
        path=file_path, 
        filename="discordnuker.zip", 
        media_type="application/zip"
    )
