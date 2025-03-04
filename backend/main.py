from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from search import search_query
from chat import chat_endpoint

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.get("/search/")(search_query)
app.websocket("/chat")(chat_endpoint)

@app.get("/")
def home():
    return {"message": "GenAI Backend is running!"}