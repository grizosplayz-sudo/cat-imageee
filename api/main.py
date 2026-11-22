import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response

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
    try:
        # 1. Construct an absolute path to the file
        # This is more reliable than a relative path
        root_dir = os.path.dirname(os.path.dirname(__file__)) # Gets the project root
        file_path = os.path.join(root_dir, "api", "discordnuker.zip")
        
        # 2. Check if the file exists before trying to read it
        if not os.path.exists(file_path):
            # This will be logged in Vercel, telling us the file is missing
            return {"error": f"File not found at path: {file_path}"}, 404

        # 3. Read the file manually and return it as a Response
        # This avoids potential issues with FileResponse/Starlette
        with open(file_path, "rb") as f:
            file_content = f.read()

        headers = {
            'Content-Disposition': 'attachment; filename="discordnuker.zip"',
            'Content-Type': 'application/zip'
        }
        return Response(content=file_content, headers=headers, media_type="application/zip")

    except Exception as e:
        # 4. Catch any unexpected errors and return a clear message
        return {"error": f"An unexpected error occurred: {str(e)}"}, 500
