# 安装指南

如果你遇到 `ModuleNotFoundError: No module named 'agno.embedder'` 错误，请按照以下步骤操作。

## 问题原因

`agno` 库的基础安装不包含所有的 embedder。你需要额外安装 embedding 支持。

## 解决方案

### 方案 1：安装 HuggingFace embedder（推荐）

```bash
pip install 'agno[huggingface]'
```

这会安装 `agno` 的 HuggingFace embedder 支持，可以使用 Sentence Transformers 模型。

### 方案 2：安装所有 embedders

```bash
pip install 'agno[embedders]'
```

这会安装所有可用的 embedder（包括 HuggingFace, Ollama 等）。

### 方案 3：检查可用的 embedders

运行测试脚本查看你的环境中哪些 embedder 可用：

```bash
python test_embedders.py
```

输出示例：
```
Testing available embedders in agno library...

✅ HuggingfaceEmbedder is available
   Import: from agno.embedder.huggingface import HuggingfaceEmbedder
❌ SentenceTransformerEmbedder not available: No module named 'agno.embedder.sentence_transformer'
✅ OpenAIEmbedder is available
   Import: from agno.embedder.openai import OpenAIEmbedder
```

## 完整安装步骤

1. **安装基础依赖**：
   ```bash
   pip install agno pypdf pandas
   ```

2. **安装 embedding 支持**：
   ```bash
   pip install 'agno[huggingface]'
   ```

3. **设置环境变量**：
   ```bash
   export DEEPSEEK_API_KEY="your-deepseek-api-key"
   ```

4. **运行程序**：
   ```bash
   python knowledge_agent.py
   ```

## 注意事项

### 如果使用 HuggingFace embedder
- ✅ 完全免费，无需 API key
- ✅ 首次运行会下载模型（约 90MB）
- ✅ 模型会缓存到本地，之后无需重新下载

### 如果回退到 OpenAI embedder
如果安装失败，程序会使用默认的 OpenAI embedder，此时你需要：
1. 确保有可用的 OpenAI API key
2. 设置环境变量：`export OPENAI_API_KEY="your-openai-api-key"`
3. 确保账户有足够的配额

## 常见错误及解决方法

### 错误 1: `ModuleNotFoundError: No module named 'agno.embedder'`
**解决**：安装 embedder 支持
```bash
pip install 'agno[huggingface]'
```

### 错误 2: `ModuleNotFoundError: No module named 'sentence_transformers'`
**解决**：安装 sentence-transformers
```bash
pip install sentence-transformers
```

### 错误 3: OpenAI API quota exceeded (429)
**解决**：确保安装了本地 embedder，不要使用 OpenAI embedder
```bash
pip install 'agno[huggingface]'
```

## 验证安装

成功安装后，运行测试脚本：
```bash
python test_embedders.py
```

应该看到至少一个 embedder 可用（推荐使用 HuggingfaceEmbedder）。

## 需要帮助？

如果上述方法都不起作用，请：
1. 检查 Python 版本（推荐 3.8+）
2. 尝试在新的虚拟环境中安装
3. 查看 agno 库的官方文档

```bash
# 创建新虚拟环境
python -m venv .venv
source .venv/bin/activate  # MacOS/Linux
# .venv\Scripts\activate   # Windows

# 重新安装
pip install agno pypdf pandas 'agno[huggingface]'
```

