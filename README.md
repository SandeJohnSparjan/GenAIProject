# GenAIProject Structre

📌 1. Backend (FastAPI)

This backend will:
✅ Handle real-time chat with WebSockets.
✅ Process enterprise search queries using LangChain + ChromaDB.
✅ Serve AI-generated responses via OpenAI GPT-4 API.


GenAI-Project/
│── backend/                # FastAPI Backend
│   ├── main.py             # API server
│   ├── search.py           # Search API
│   ├── chat.py             # Chat WebSockets
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Backend containerization
│── frontend/               # Next.js Frontend
│   ├── components/         # UI Components
│   ├── pages/              # Frontend pages
│   ├── public/             # Static assets
│   ├── package.json        # Frontend dependencies
│   ├── Dockerfile          # Frontend containerization
│── docker-compose.yml      # Container management
│── README.md               # Documentation