from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector
from agno.models.openai import OpenAIChat

# Create a knowledge base with PgVector
knowledge = Knowledge(
    vector_db=PgVector(
        table_name="knowledge_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"
    ),
)

# Create an agent with knowledge
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    knowledge=knowledge,
    # Enable automatic knowledge search
    search_knowledge=True,
    instructions=[
        "Always search your knowledge base before answering questions",
        "Include source references in your responses when possible"
    ]
)