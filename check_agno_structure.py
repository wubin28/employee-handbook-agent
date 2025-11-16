#!/usr/bin/env python3
"""Check the actual structure of the agno package."""

import os
import sys

print("Checking agno package structure...\n")

try:
    import agno
    agno_path = os.path.dirname(agno.__file__)
    print(f"✅ agno package location: {agno_path}")
    print(f"✅ agno version: {agno.__version__}")
    
    # List all directories and files in agno package
    print("\n" + "="*60)
    print("Contents of agno package directory:")
    print("="*60)
    
    for item in sorted(os.listdir(agno_path)):
        item_path = os.path.join(agno_path, item)
        if os.path.isdir(item_path) and not item.startswith('__'):
            print(f"📁 {item}/")
            # Check if it's a Python package
            if os.path.exists(os.path.join(item_path, '__init__.py')):
                print(f"   └─ (Python package)")
        elif item.endswith('.py'):
            print(f"📄 {item}")
    
    # Try to find embedder-related modules
    print("\n" + "="*60)
    print("Searching for embedder-related modules:")
    print("="*60)
    
    for root, dirs, files in os.walk(agno_path):
        for file in files:
            if 'embed' in file.lower() and file.endswith('.py'):
                rel_path = os.path.relpath(os.path.join(root, file), agno_path)
                print(f"Found: {rel_path}")
    
    # Check for common submodules
    print("\n" + "="*60)
    print("Checking common submodules:")
    print("="*60)
    
    common_modules = [
        'agno.embedder',
        'agno.embedders', 
        'agno.embedding',
        'agno.embeddings',
        'agno.vectordb',
        'agno.knowledge',
        'agno.agent',
        'agno.models',
    ]
    
    for module_name in common_modules:
        try:
            __import__(module_name)
            print(f"✅ {module_name} - available")
        except ImportError as e:
            print(f"❌ {module_name} - not available: {e}")
    
    # Try importing knowledge to see what embedders it uses
    print("\n" + "="*60)
    print("Checking Knowledge class embedder parameter:")
    print("="*60)
    
    try:
        from agno.knowledge.knowledge import Knowledge
        import inspect
        sig = inspect.signature(Knowledge.__init__)
        print(f"Knowledge.__init__ parameters:")
        for param_name, param in sig.parameters.items():
            if param_name not in ['self']:
                print(f"  - {param_name}: {param.annotation if param.annotation != inspect.Parameter.empty else 'Any'}")
    except Exception as e:
        print(f"Error: {e}")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

