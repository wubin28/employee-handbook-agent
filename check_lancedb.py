#!/usr/bin/env python3
"""Check LanceDb configuration options."""

import inspect

print("Checking LanceDb configuration...\n")

try:
    from agno.vectordb.lancedb import LanceDb
    
    print("✅ LanceDb imported successfully")
    print("\nLanceDb.__init__ parameters:")
    print("="*60)
    
    sig = inspect.signature(LanceDb.__init__)
    for param_name, param in sig.parameters.items():
        if param_name != 'self':
            default = param.default if param.default != inspect.Parameter.empty else 'Required'
            annotation = param.annotation if param.annotation != inspect.Parameter.empty else 'Any'
            print(f"  - {param_name}")
            print(f"      Type: {annotation}")
            print(f"      Default: {default}")
            print()
    
    # Check if there's an embedder attribute or method
    print("\nLanceDb attributes and methods related to 'embed':")
    print("="*60)
    for attr in dir(LanceDb):
        if 'embed' in attr.lower() and not attr.startswith('_'):
            print(f"  - {attr}")
    
    # Try to check the source or docstring
    print("\nLanceDb docstring:")
    print("="*60)
    if LanceDb.__doc__:
        print(LanceDb.__doc__)
    else:
        print("No docstring available")
    
    # Check fastembed embedder
    print("\n" + "="*60)
    print("Checking FastEmbed embedder:")
    print("="*60)
    try:
        from agno.knowledge.embedder.fastembed import FastEmbed
        print("✅ FastEmbed imported successfully")
        print("\nFastEmbed.__init__ parameters:")
        sig = inspect.signature(FastEmbed.__init__)
        for param_name, param in sig.parameters.items():
            if param_name != 'self':
                default = param.default if param.default != inspect.Parameter.empty else 'Required'
                annotation = param.annotation if param.annotation != inspect.Parameter.empty else 'Any'
                print(f"  - {param_name}: {annotation} = {default}")
    except ImportError as e:
        print(f"❌ FastEmbed not available: {e}")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

