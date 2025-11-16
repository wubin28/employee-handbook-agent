import os
from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb
from agno.models.deepseek import DeepSeek

# Try importing FastEmbedEmbedder (FREE local embedder)
try:
    from agno.knowledge.embedder.fastembed import FastEmbedEmbedder
    EMBEDDER_AVAILABLE = True
    print("✅ Using FastEmbedEmbedder (free local embedder)")
except ImportError as e:
    EMBEDDER_AVAILABLE = False
    print(f"⚠️  FastEmbedEmbedder not available: {e}")
    print("   Using default OpenAI embedder (requires OPENAI_API_KEY)")

# Load API keys from environment variables
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY environment variable is not set")

if not EMBEDDER_AVAILABLE and not OPENAI_API_KEY:
    raise ValueError(
        "Either install fastembed (pip install fastembed) "
        "or set OPENAI_API_KEY environment variable"
    )

# Create embedder (in LanceDb, not Knowledge!)
if EMBEDDER_AVAILABLE:
    # Use FREE local FastEmbedEmbedder
    # Note: id parameter is the model name
    # Using default model (already downloaded with fastembed)
    embedder = FastEmbedEmbedder()  # Uses default model
    print(f"   Using default FastEmbed model")
else:
    # Fallback to OpenAI embedder
    embedder = None  # LanceDb will use default OpenAI embedder

# Create a knowledge base with LanceDB
knowledge = Knowledge(
    vector_db=LanceDb(
        table_name="knowledge_documents",
        uri="tmp/lancedb",  # Local directory for storage
        embedder=embedder,  # embedder goes in LanceDb, not Knowledge!
    ),
)

# Add PDF file to knowledge base
knowledge.add_content(
    path="./jd-employee-handbook.pdf"
)

# Create an agent with knowledge
agent = Agent(
    model=DeepSeek(
        id="deepseek-reasoner",
        api_key=DEEPSEEK_API_KEY
    ),
    knowledge=knowledge,
    # Enable automatic knowledge search
    search_knowledge=True,
    instructions=[
        "Always search your knowledge base before answering questions",
        "Include source references in your responses when possible"
    ]
)

# Test your knowledge-powered agent
if __name__ == "__main__":
    # Your agent will automatically search its knowledge to answer
    agent.print_response(
        "What is the company policy on annual leave?",
        stream=True
    )