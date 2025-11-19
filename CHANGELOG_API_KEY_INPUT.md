# API Key 输入方式变更说明

## 更新日期
2025-11-19

## 变更概述
将 DeepSeek API Key 的获取方式从环境变量改为运行时安全输入，提高了安全性和易用性。

## 主要变更

### 1. 代码变更 (`knowledge_agent.py`)

#### 之前
```python
# 从环境变量读取 API Key
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
```

#### 现在
```python
import getpass

# 运行时安全输入 API Key
print("\n" + "="*60)
print("🔐 请输入您的 DeepSeek API Key")
print("   (输入时不会显示,按回车确认)")
print("="*60)
DEEPSEEK_API_KEY = getpass.getpass("DeepSeek API Key: ")

if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.strip() == "":
    raise ValueError("DeepSeek API Key 不能为空，请重新运行程序并输入有效的 API Key")
```

### 2. 使用方式变更

#### 之前
```bash
# 需要先设置环境变量
export DEEPSEEK_API_KEY="your-deepseek-api-key"

# 然后运行程序
python knowledge_agent.py
```

#### 现在
```bash
# 直接运行程序
python knowledge_agent.py

# 程序会提示输入 API Key
# 输入时显示为星号（不可见），保护隐私
```

## 优势

### 安全性提升
- ✅ **输入不可见**：使用 `getpass` 模块，输入时不显示字符
- ✅ **不留痕迹**：API Key 不会保存在 shell 历史记录中
- ✅ **临时存储**：仅在程序运行期间存在于内存中

### 易用性改善
- ✅ **无需配置环境变量**：对于初学者更友好
- ✅ **跨平台一致性**：Windows、macOS、Linux 使用方式完全相同
- ✅ **即时反馈**：输入错误可立即重新运行程序

## 文档更新

以下文档已同步更新：
- ✅ `README.md` - 主要说明文档
- ✅ `QUICKSTART.md` - 快速入门指南
- ✅ `INSTALL_GUIDE.md` - 安装指南

所有文档中的环境变量设置说明已被移除或更新为运行时输入说明。

## 兼容性

### 完全兼容
- Python 3.6+ （`getpass` 是标准库）
- macOS / Linux / Windows
- 所有支持的终端和 shell

### 注意事项
- 在某些非交互式环境（如 CI/CD 管道）中，可能需要使用其他方式提供 API Key
- 如果需要批量运行或自动化，可以考虑提供环境变量作为备选方案

## 测试

运行测试脚本验证功能：
```bash
python test_api_key_input.py
```

## 回滚方法

如需回滚到环境变量方式，可以修改 `knowledge_agent.py` 第 18-26 行：

```python
# 回滚到环境变量方式
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
```

## 问题排查

### Q: 在某些终端中看不到提示符
A: 确保使用支持标准输入的终端（避免使用某些简化的 IDE 终端）

### Q: 想在自动化脚本中使用
A: 可以通过管道或标准输入提供：
```bash
echo "your-api-key" | python knowledge_agent.py
```

### Q: 误输入错误的 API Key
A: 程序会在首次使用 API 时失败，重新运行程序即可

## 未来改进建议

- [ ] 支持环境变量作为备选方案（双模式）
- [ ] 添加 API Key 验证（调用 API 测试）
- [ ] 支持 API Key 本地加密存储（可选）

