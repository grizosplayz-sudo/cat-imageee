from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

# Vercel REQUIRES this exact line to work
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="background-color: #111; text-align: center; font-family: sans-serif; margin: 0; padding: 0;">
            <!-- REPLACE THE LINK BELOW with your actual image link if needed -->
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
    file_path = "api/discordnuker.zip"
    
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path, 
            filename="discordnuker.zip", 
            media_type="application/zip"
        )
    else:
        return {"error": "File not found. Make sure discordnuker.zip is inside the api folder."}
