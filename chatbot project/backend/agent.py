import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from backend.rag_pipeline import rag_retriever
from tavily import TavilyClient

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not set in .env")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not set in .env")

# LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Tools
retriever_tool = Tool(
    name="Course Retriever",
    func=rag_retriever,
    description="Retrieve course info from catalog."
)

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def web_search_tool(query: str):
    return tavily_client.search(query)

search_tool = Tool(
    name="Web Search",
    func=web_search_tool,
    description="Search the web for general questions."
)

# Agent
agent = initialize_agent(
    tools=[retriever_tool, search_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)


