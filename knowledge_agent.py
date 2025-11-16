from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb
from agno.models.deepseek import DeepSeek

# Create a knowledge base with LanceDB
# Local vector storage - no database setup required
knowledge = Knowledge(
    vector_db=LanceDb(
        table_name="knowledge_documents",
        uri="tmp/lancedb"  # Local directory for storage
    ),
)

# Create an agent with knowledge
agent = Agent(
    model=DeepSeek(id="deepseek-reasoner"),
    knowledge=knowledge,
    # Enable automatic knowledge search
    search_knowledge=True,
    instructions=[
        "Always search your knowledge base before answering questions",
        "Include source references in your responses when possible"
    ]
)