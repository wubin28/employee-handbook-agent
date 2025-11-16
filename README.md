# Employee Handbook Agent

一个基于 DeepSeek 和 LanceDB 的知识库问答 Agent，可以回答员工手册相关问题。

## 功能特性

- ✅ 使用 DeepSeek Reasoner 模型进行复杂推理
- ✅ 基于 LanceDB 的本地向量数据库（无需配置外部数据库）
- ✅ **完全免费的本地 embedding**（使用 Sentence Transformers，无需 OpenAI API）
- ✅ 自动读取和索引 PDF 文档
- ✅ 智能知识检索和引用

## 前置要求

### 1. 安装依赖

```bash
# 基础安装
pip install agno pypdf pandas

# 安装 FastEmbed（免费本地 embedder，推荐！）
pip install fastembed
```

**为什么使用 FastEmbed？**
- ✅ 完全免费，无需 API key
- ✅ 在本地运行，保护数据隐私
- ✅ 无使用限制和配额
- ✅ 速度快，质量好
- ✅ 自动下载和缓存模型

### 2. 配置 API Key

你只需要一个 API Key：

#### DEEPSEEK_API_KEY
用于 DeepSeek 推理模型。获取方式：
- 访问 [DeepSeek 平台](https://platform.deepseek.com/api_keys)
- 注册并创建 API Key

**为什么只需要 DEEPSEEK_API_KEY？**

本项目使用 **FastEmbed** 进行文本向量化，完全免费：
- ✅ 完全免费，无需 OpenAI API key
- ✅ 在本地运行，保护数据隐私
- ✅ 无使用限制和配额
- ✅ 自动下载和缓存模型（首次约 50MB）

## 使用方法

### 1. 设置环境变量

**MacOS/Linux:**
```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

**Windows:**
```bash
setx DEEPSEEK_API_KEY "your-deepseek-api-key"
```

### 2. 运行程序

```bash
python knowledge_agent.py
```

### 3. 自定义问题

修改 `knowledge_agent.py` 中的测试代码：

```python
if __name__ == "__main__":
    agent.print_response(
        "你的问题",
        stream=True
    )
```

## 工作原理

1. **文档加载**：程序启动时自动读取 `jd-employee-handbook.pdf`
2. **文本分块**：将 PDF 内容分割成小块
3. **向量化**：使用 **FastEmbed** 本地模型将文本转换为向量（完全免费）
4. **存储**：向量存储在本地 LanceDB 数据库（`tmp/lancedb` 目录）
5. **查询**：用户提问时，自动搜索相关内容
6. **推理**：DeepSeek Reasoner 基于检索到的内容生成回答

## 项目结构

```
employee-handbook-agent/
├── knowledge_agent.py          # 主程序
├── jd-employee-handbook.pdf    # 员工手册 PDF
├── tmp/lancedb/               # 本地向量数据库（自动创建）
└── README.md                  # 本文件
```

## 常见问题

### Q: 为什么不需要 OpenAI API Key？
A: 我们使用 FastEmbed 这个免费的本地模型进行文本向量化，完全不需要 OpenAI。只有 DeepSeek 需要 API key 用于推理和回答问题。

### Q: FastEmbed 效果好吗？
A: 非常好！我们使用的 `BAAI/bge-small-en-v1.5` 模型是一个高质量的轻量级模型，在大多数场景下表现优异，而且完全免费、无配额限制。

### Q: 向量数据库存储在哪里？
A: 存储在项目目录下的 `tmp/lancedb/` 文件夹中，是本地文件，无需外部数据库。

### Q: 如何添加更多文档？
A: 在 `knowledge.add_content()` 前后添加更多文档：
```python
knowledge.add_content(path="./document1.pdf")
knowledge.add_content(path="./document2.pdf")
```

### Q: 程序运行很慢怎么办？
A: 首次运行需要：
- 下载 FastEmbed 模型（首次使用时自动下载，约 50MB）
- 处理整个 PDF 并生成向量
之后的运行会直接使用缓存的向量数据，速度会快很多。

### Q: 首次运行会下载什么？
A: 会自动下载 `BAAI/bge-small-en-v1.5` 模型（约 50MB），只需下载一次，之后会缓存到 `.fastembed_cache` 目录。

## 技术栈

- **Agent 框架**: agno
- **LLM 模型**: DeepSeek Reasoner（推理和生成答案）
- **向量数据库**: LanceDB（本地存储）
- **Embedding**: FastEmbed + BAAI/bge-small-en-v1.5（免费本地模型）
- **PDF 处理**: pypdf
- **数据处理**: pandas

## License

MIT

