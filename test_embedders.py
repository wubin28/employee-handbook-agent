#!/usr/bin/env python3
"""Test which embedders are available in agno library."""

print("Testing available embedders in agno library...\n")

# Test 1: HuggingFace embedder
try:
    from agno.embedder.huggingface import HuggingfaceEmbedder
    print("✅ HuggingfaceEmbedder is available")
    print("   Import: from agno.embedder.huggingface import HuggingfaceEmbedder")
except ImportError as e:
    print(f"❌ HuggingfaceEmbedder not available: {e}")

# Test 2: Sentence Transformer embedder
try:
    from agno.embedder.sentence_transformer import SentenceTransformerEmbedder
    print("✅ SentenceTransformerEmbedder is available")
    print("   Import: from agno.embedder.sentence_transformer import SentenceTransformerEmbedder")
except ImportError as e:
    print(f"❌ SentenceTransformerEmbedder not available: {e}")

# Test 3: Ollama embedder
try:
    from agno.embedder.ollama import OllamaEmbedder
    print("✅ OllamaEmbedder is available")
    print("   Import: from agno.embedder.ollama import OllamaEmbedder")
except ImportError as e:
    print(f"❌ OllamaEmbedder not available: {e}")

# Test 4: OpenAI embedder
try:
    from agno.embedder.openai import OpenAIEmbedder
    print("✅ OpenAIEmbedder is available")
    print("   Import: from agno.embedder.openai import OpenAIEmbedder")
except ImportError as e:
    print(f"❌ OpenAIEmbedder not available: {e}")

# Test 5: Check agno.embedder module
print("\n" + "="*60)
try:
    import agno.embedder
    print("✅ agno.embedder module exists")
    print(f"   Available items: {dir(agno.embedder)}")
except ImportError as e:
    print(f"❌ agno.embedder module not found: {e}")
    print("   Trying to check agno package structure...")
    try:
        import agno
        print(f"   agno package location: {agno.__file__}")
        print(f"   agno package contents: {dir(agno)}")
    except Exception as e2:
        print(f"   Error: {e2}")

print("\n" + "="*60)
print("Recommendation:")
print("Try installing: pip install 'agno[embedders]' or 'agno[huggingface]'")

