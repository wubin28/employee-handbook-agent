# 快速入门指南

## 安装和运行（5分钟）

### 步骤 1：安装 FastEmbed

```bash
pip install fastembed
```

或使用 uv（更快）：

```bash
uv pip install fastembed
```

### 步骤 2：运行程序

```bash
python knowledge_agent.py
```

**程序运行时会提示您输入 DeepSeek API Key**（输入时显示为星号，保护隐私）。

## 首次运行

首次运行时，程序会：

1. 🔐 提示输入 DeepSeek API Key（输入时不会显示）
2. ✅ 检测 FastEmbed 是否可用
3. ⬇️ 自动下载 `BAAI/bge-small-en-v1.5` 模型（约 50MB，只需一次）
4. 📄 读取 PDF 文件
5. 🔢 生成向量并存储到 LanceDB
6. 💬 回答你的问题

**示例输出**：

```
✅ Using FastEmbedEmbedder (free local embedder)

============================================================
🔐 请输入您的 DeepSeek API Key
   (输入时不会显示，按回车确认)
============================================================
DeepSeek API Key: 
   Using default FastEmbed model
INFO Creating table: knowledge_documents
INFO Loading content: ...
INFO Adding content from path, ..., ./jd-employee-handbook.pdf
INFO Using Reader: PDFReader
INFO Reading: jd-employee-handbook.pdf
[下载模型...]
[生成向量...]
[Agent 回答问题...]
```

## 预期时间

- **首次运行**：2-5 分钟（下载模型 + 处理 PDF）
- **后续运行**：10-30 秒（使用缓存的向量）

## 验证安装

运行测试脚本确认一切正常：

```bash
python check_lancedb.py
```

应该看到：

```
✅ LanceDb imported successfully
✅ FastEmbed imported successfully
```

## 常见问题

### Q: 显示 "FastEmbed not available"
**解决**：安装 fastembed
```bash
pip install fastembed
```

### Q: 下载模型很慢
**解决**：这是正常的，模型只需下载一次。如果中断，删除 `.fastembed_cache` 目录重新运行。

### Q: "DeepSeek API Key 不能为空"
**解决**：在程序提示时输入有效的 API Key。如果意外按下回车，请重新运行程序。

### Q: 想使用 OpenAI embedder 而不是 FastEmbed
**解决**：不要安装 fastembed，程序会自动回退到 OpenAI embedder。需要设置：
```bash
export OPENAI_API_KEY="your-openai-key"
```

## 下一步

- 修改问题：编辑 `knowledge_agent.py` 第 78 行
- 添加更多 PDF：在 `knowledge.add_content()` 后面添加更多文件
- 查看完整文档：`README.md`
- 安装问题排查：`INSTALL_GUIDE.md`

## 清理

如果需要重新开始：

```bash
# 删除向量数据库
rm -rf tmp/

# 删除模型缓存
rm -rf .fastembed_cache/
```

## 技术支持

遇到问题？
1. 查看 `INSTALL_GUIDE.md`
2. 运行 `python check_agno_structure.py`
3. 运行 `python check_lancedb.py`
4. 查看 agno 官方文档

---

**提示**：第一次运行最慢，但后续会很快！

