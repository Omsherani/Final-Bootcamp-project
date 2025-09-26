# backend/rag_pipeline.py
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load documents
loader = PyPDFLoader("docs/CS_Catalog_Fall_2025.pdf")
documents = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# Embeddings + Vector DB
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")

# Create Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# LLM


load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file!")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=google_api_key  # 👈 force API key from .env
)


# QA Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
