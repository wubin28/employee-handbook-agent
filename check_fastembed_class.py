#!/usr/bin/env python3
"""Check what's available in the fastembed module."""

import inspect

print("Checking agno.knowledge.embedder.fastembed module...\n")

try:
    import agno.knowledge.embedder.fastembed as fastembed_module
    
    print("✅ Module imported successfully")
    print("\nAvailable classes and functions:")
    print("="*60)
    
    for name in dir(fastembed_module):
        if not name.startswith('_'):
            obj = getattr(fastembed_module, name)
            obj_type = type(obj).__name__
            print(f"  - {name} ({obj_type})")
            
            # If it's a class, show its init parameters
            if inspect.isclass(obj):
                try:
                    sig = inspect.signature(obj.__init__)
                    print(f"      __init__ parameters: {list(sig.parameters.keys())}")
                except:
                    pass
    
    # Try to find embedder classes
    print("\n" + "="*60)
    print("Looking for Embedder classes:")
    print("="*60)
    
    for name in dir(fastembed_module):
        if not name.startswith('_'):
            obj = getattr(fastembed_module, name)
            if inspect.isclass(obj):
                # Check if it looks like an embedder
                if 'embed' in name.lower():
                    print(f"✅ Found: {name}")
                    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

