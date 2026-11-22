from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def show_cat():
    # This shows your cover image AND a download button
    return """
    <html>
        <body style="background-color: #1a1a1a; color: white; text-align: center; font-family: sans-serif;">
            <h1>Here is the Cover</h1>
            <!-- Put your cat image here -->
            <img src="YOUR_CAT_IMAGE_LINK_OR_FILE" style="max-width: 100%; height: auto;">
            
            <br><br>
            
            <!-- The download button -->
            <a href="/discordnuke.zip" style="background-color: red; color: white; padding: 15px 30px; text-decoration: none; font-size: 20px; border-radius: 5px; font-weight: bold;">
                DOWNLOAD ZIP
            </a>
        </body>
    </html>
    """
