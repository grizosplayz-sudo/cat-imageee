@app.get("/download")
async def download_file():
    # Changed path to look in the root 'api' folder
    file_path = "api/discordnuker.zip" 
    
    # Check if the file exists to prevent a 500 error
    import os
    if not os.path.exists(file_path):
        # If it doesn't exist, return a clearer error message
        return {"error": "File not found on server. Check bundle."}, 404

    return FileResponse(
        path=file_path, 
        filename="discordnuker.zip", 
        media_type="application/zip"
    )
