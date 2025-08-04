# main.py 
# this is for a app for streamming the videos on web
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from Streaming.util.render_template import render_page
from Streaming.server.exceptions import InvalidHash, FIleNotFound

app = FastAPI()


@app.get("/watch/{file_id}", response_class=HTMLResponse)
async def stream_video(file_id: int, hash: str):
    try:
        return await render_page(file_id, hash)
    except (InvalidHash, FIleNotFound):
        raise HTTPException(status_code=403, detail="Invalid or expired stream link")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/{file_id}", response_class=HTMLResponse)
async def download_file(file_id: int, hash: str):
    try:
        return await render_page(file_id, hash)
    except (InvalidHash, FIleNotFound):
        raise HTTPException(status_code=403, detail="Invalid or expired download link")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
