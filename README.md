AI Chatbot with RAG
An AI-powered chatbot built with FastAPI, LangChain, and Google Gemini API. It uses Retrieval-Augmented Generation (RAG) to answer student queries from PDF catalogs and provides accurate, user-friendly responses.
 Features
1) RAG-powered course catalog search
2) Google Gemini API for natural conversation
3) PDF document loading & retrieval
4) FastAPI backend with REST API
5) Easy to run locally
🛠️ Tech Stack
Backend: FastAPI, Python
AI/ML: LangChain, Google Gemini API, HuggingFace Embeddings
Database/Storage: Local file storage for documents
Frontend (optional): React

project structure
chatbot-project/
│── backend/
│   ├── main.py           # FastAPI entry point
│   ├── agent.py          # AI agent logic
│   ├── rag_pipeline.py   # RAG pipeline (embeddings + retriever)
│── .env                  # API keys & configs
│── requirements.txt      # Python dependencies

Use this command to run the app
uvicorn backend.main:app --reload

