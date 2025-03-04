from fastapi import WebSocket
from langchain.llms import OpenAI

llm = OpenAI(model_name="gpt-4", temperature=0.7)

async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = llm.generate(data)
        await websocket.send_text(response)