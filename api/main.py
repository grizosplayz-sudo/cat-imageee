from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

# 1. This route shows the cover image
@app.get("/", response_class=HTMLResponse)
async def show_cover():
    return """
    <html>
        <body style="margin: 0; padding: 0; background-color: #111; text-align: center; font-family: sans-serif;">
            <!-- Your cover image -->
            <img src="https://cat-imageee-mbo9.vercel.app/" alt="Cover" style="width: 100%; max-width: 800px; margin-top: 20px;">
            <br><br>
            <!-- The download button -->
            <a href="/download" style="background-color: #ff3333; color: white; padding: 15px 30px; text-decoration: none; font-size: 20px; font-weight: bold; border-radius: 8px; display: inline-block; margin-bottom: 40px;">
                DOWNLOAD FILE
            </a>
        </body>
    </html>
    """

# 2. This route forces the zip to download
@app.get("/download")
async def download_file():
    # This looks for the file inside the api folder
    file_path = "api/discordnuker.zip" 
    
    # This tells the browser to download it as "discordnuker.zip"
    return FileResponse(
        path=file_path, 
        filename="discordnuker.zip", 
        media_type="application/zip"
    )
