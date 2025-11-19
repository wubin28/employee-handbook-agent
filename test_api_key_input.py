#!/usr/bin/env python
"""
测试 DeepSeek API Key 输入功能
用于验证 getpass 模块是否正常工作
"""
import getpass

def test_api_key_input():
    """测试 API Key 输入"""
    print("\n" + "="*60)
    print("🧪 测试 DeepSeek API Key 输入功能")
    print("   (输入时不会显示，按回车确认)")
    print("="*60)
    
    api_key = getpass.getpass("DeepSeek API Key: ")
    
    if not api_key or api_key.strip() == "":
        print("\n❌ 错误：API Key 不能为空")
        return False
    
    # 显示部分 API Key 用于验证（隐藏大部分内容）
    masked_key = api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:] if len(api_key) > 8 else "*" * len(api_key)
    print(f"\n✅ 成功接收 API Key: {masked_key}")
    print(f"   长度: {len(api_key)} 字符")
    return True

if __name__ == "__main__":
    success = test_api_key_input()
    if success:
        print("\n✅ 测试通过！getpass 模块工作正常。")
        print("   您可以安全地运行 knowledge_agent.py")
    else:
        print("\n❌ 测试失败，请确保输入有效的 API Key")

