from fastapi import FastAPI, WebSocket
from tools import time
import asyncio

app = FastAPI()

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_text(time.currentTime())
        await asyncio.sleep(0.01)
        


