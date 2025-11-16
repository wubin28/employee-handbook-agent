# Employee Handbook Agent

一个基于 DeepSeek 和 LanceDB 的知识库问答 Agent，可以回答员工手册相关问题。

## 功能特性

- ✅ 使用 **DeepSeek Reasoner** 模型进行复杂推理
- ✅ 基于 **LanceDB** 的本地向量数据库（无需配置外部数据库）
- ✅ **完全免费的本地 embedding**（使用 FastEmbed，无需 OpenAI API）
- ✅ 自动读取和索引 PDF 文档
- ✅ 智能知识检索和引用
- ✅ 一键运行，4个命令即可启动

## 快速开始（macOS / iTerm2 / zsh）

### 步骤 1：创建虚拟环境

```bash
# 使用 uv 创建 Python 3.12 虚拟环境（推荐，更快）
uv venv --python 3.12

# 激活虚拟环境
source .venv/bin/activate
```

**如果没有安装 uv**，使用标准方式：
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 步骤 2：安装依赖

```bash
# 使用 uv（推荐，更快）
uv pip install -U agno pypdf pandas fastembed lancedb openai

# 或使用标准 pip
pip install -U agno pypdf pandas fastembed lancedb openai
```

**依赖说明**：
- `agno` - Agent 框架（包含 LanceDB）
- `pypdf` - PDF 文件读取
- `pandas` - 数据处理
- `fastembed` - **免费本地 embedder**（无需 OpenAI API key！）
- `lancedb` - 在本地存储数据，无须安装数据库
- `openai` - 虽然使用的是 DeepSeek 模型，但 embedding（文本向量化）功能仍然使用 OpenAI 的服务。这是 agno 库的默认配置，为了方便，这里也安装了OpenAI的库，但不会使用它

### 步骤 3：配置 API Key

获取 DeepSeek API Key：
1. 访问 [DeepSeek 平台](https://platform.deepseek.com/api_keys)
2. 注册并创建 API Key

设置环境变量：
```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

**提示**：可以将此命令添加到 `~/.zshrc` 以永久保存：
```bash
echo 'export DEEPSEEK_API_KEY="your-deepseek-api-key"' >> ~/.zshrc
source ~/.zshrc
```

### 步骤 4：运行程序

```bash
python knowledge_agent.py
```

**首次运行**会：
- ⬇️ 自动下载 FastEmbed 模型（约 60-100MB，仅首次）
- 📄 读取并处理 PDF 文件
- 🔢 生成向量并存储到本地数据库
- 💬 回答问题

**预期时间**：
- 首次运行：2-5 分钟（下载模型 + 处理 PDF）
- 后续运行：10-30 秒（使用缓存）

---

## 为什么只需要 DEEPSEEK_API_KEY？

本项目使用 **FastEmbed** 进行文本向量化，完全免费：
- ✅ 完全免费，无需 OpenAI API key
- ✅ 在本地运行，保护数据隐私
- ✅ 无使用限制和配额
- ✅ 自动下载和缓存模型

---

## Windows Powershell 用户

```bash
# 1. 创建虚拟环境
python -m venv .venv
.venv\Scripts\activate

# 2. 安装依赖
pip install -U agno pypdf pandas fastembed lancedb openai

# 3. 设置 API Key
setx DEEPSEEK_API_KEY "your-deepseek-api-key"

# 4. 运行程序
python knowledge_agent.py
```

## Output

```markdown
(employee-handbook-agent) ➜  employee-handbook-agent (main))python knowledge_agent.py
✅ Using FastEmbedEmbedder (free local embedder)
   Using default FastEmbed model
INFO Creating table: knowledge_documents
[2025-11-16T08:20:38Z WARN  lance::dataset::write::insert] No existing dataset at /Users/binwu/temp/employee-handbook-agent/tmp/lancedb/knowledge_documents.lance, it will be created
INFO skip_if_exists is disabled, disabling upsert
INFO Loading content: 6131b000-d846-59f3-ac46-b703a2e91f37
INFO Adding content from path, 6131b000-d846-59f3-ac46-b703a2e91f37, None,
     ./jd-employee-handbook.pdf, None
INFO Using Reader: PDFReader
INFO Reading: jd-employee-handbook.pdf
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 146653.99it/s]
Fetching 5 files: 100%|██████████████████████████████████████| 5/5 [00:00<00:00, 8727.22it/s]
Fetching 5 files: 100%|██████████████████████████████████████| 5/5 [00:00<00:00, 8609.00it/s]
Fetching 5 files: 100%|██████████████████████████████████████| 5/5 [00:00<00:00, 7872.19it/s]
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 171897.70it/s]
Fetching 5 files: 100%|████████████████████████████████████████| 5/5 [00:00<00:00, 55.26it/s]
Fetching 5 files: 100%|█████████████████████████████████████| 5/5 [00:00<00:00, 77101.18it/s]
Fetching 5 files: 100%|██████████████████████████████████████| 5/5 [00:00<00:00, 9023.89it/s]
Fetching 5 files: 100%|█████████████████████████████████████| 5/5 [00:00<00:00, 67650.06it/s]
Fetching 5 files: 100%|█████████████████████████████████████| 5/5 [00:00<00:00, 18379.95it/s]
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 167772.16it/s]
Fetching 5 files: 100%|██████████████████████████████████████| 5/5 [00:00<00:00, 1516.05it/s]
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 192399.27it/s]
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 179243.76it/s]
Fetching 5 files: 100%|█████████████████████████████████████| 5/5 [00:00<00:00, 43062.67it/s]
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 101803.50it/s]
Fetching 5 files: 100%|██████████████████████████████████████| 5/5 [00:00<00:00, 7051.62it/s]
Fetching 5 files: 100%|█████████████████████████████████████| 5/5 [00:00<00:00, 14037.16it/s]
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 185588.67it/s]
Fetching 5 files: 100%|██████████████████████████████████████| 5/5 [00:00<00:00, 7863.34it/s]
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 171897.70it/s]
Fetching 5 files: 100%|████████████████████████████████████████| 5/5 [00:00<00:00, 68.62it/s]
Fetching 5 files: 100%|███████████████████████████████████████| 5/5 [00:00<00:00, 616.23it/s]
Fetching 5 files: 100%|█████████████████████████████████████| 5/5 [00:00<00:00, 47233.15it/s]
Fetching 5 files: 100%|█████████████████████████████████████| 5/5 [00:00<00:00, 31254.13it/s]
Fetching 5 files: 100%|██████████████████████████████████████| 5/5 [00:00<00:00, 1455.65it/s]
Fetching 5 files: 100%|█████████████████████████████████████| 5/5 [00:00<00:00, 15185.75it/s]
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 171897.70it/s]
Fetching 5 files: 100%|████████████████████████████████████| 5/5 [00:00<00:00, 166440.63it/s]
Fetching 5 files: 100%|█████████████████████████████████████| 5/5 [00:00<00:00, 23912.79it/s]
WARNING  Contents DB not found for knowledge base: None
▰▱▱▱▱▱▱ Thinking...
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                           ┃
┃ What is the company policy on annual leave?                                               ┃
┃                                                                                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
To disable this warning, you can either:
	- Avoid using `tokenizers` before the fork if possible
	- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)
INFO Found 10 documents
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                           ┃
┃ What is the company policy on annual leave?                                               ┃
┃                                                                                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (26.1s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                           ┃
┃ I'll search our knowledge base to find information about the company's annual leave       ┃
┃ policy.Based on the search results from the employee handbook, here is the company policy ┃
┃ on annual leave (年休假):                                                                 ┃
┃                                                                                           ┃
┃ ## Annual Leave Policy                                                                    ┃
┃                                                                                           ┃
┃ ### Types of Annual Leave                                                                 ┃
┃ Annual leave includes two components:                                                     ┃
┃ - **法定年假 (Legal Annual Leave)**: Mandatory annual leave according to Chinese labor    ┃
┃ law                                                                                       ┃
┃ - **福利年假 (Welfare Annual Leave)**: Additional company-provided annual leave           ┃
┃                                                                                           ┃
┃ ### Legal Annual Leave Entitlement                                                        ┃
┃ - **1-10 years of total work experience**: 5 days per year                                ┃
┃ - **10-20 years of total work experience**: 10 days per year                              ┃
┃ - **20+ years of total work experience**: 15 days per year                                ┃
┃                                                                                           ┃
┃ *Note: Work experience is calculated based on total social work experience across all     ┃
┃ employers, verified at the time of employment.*                                           ┃
┃                                                                                           ┃
┃ ### Welfare Annual Leave (for specific employee levels)                                   ┃
┃ - **M3/P7/T7 level and above**: Up to 10 days annual cap (including legal leave)          ┃
┃ - **M4/P9/T9 level**: Up to 15 days annual cap                                            ┃
┃ - **M5/P12/T12 level and above**: Up to 20 days annual cap                                ┃
┃                                                                                           ┃
┃ *Welfare annual leave is only available after probation period completion.*               ┃
┃                                                                                           ┃
┃ ### Key Policy Details                                                                    ┃
┃                                                                                           ┃
┃ 1. **Calculation Unit**: Annual leave is calculated in 1-hour increments, with less than  ┃
┃ 1 hour counted as 1 hour                                                                  ┃
┃                                                                                           ┃
┃ 2. **Annual Leave Restrictions**: Employees cannot take annual leave if they:             ┃
┃    - Have taken more than 20 days of paid personal leave                                  ┃
┃    - Have taken extended sick leave (2+ months for <10 years experience, 3+ months for    ┃
┃ 10-20 years, 4+ months for 20+ years)                                                     ┃
┃                                                                                           ┃
┃ 3. **Annual Cycle**: The leave year runs from January 1st to December 31st                ┃
┃                                                                                           ┃
┃ 4. **Usage Order**: Employees must use annual leave in this sequence:                     ┃
┃    - Previous year's remaining legal annual leave                                         ┃
┃    - Previous year's remaining welfare annual leave                                       ┃
┃    - Current year's legal annual leave                                                    ┃
┃    - Current year's welfare annual leave                                                  ┃
┃                                                                                           ┃
┃ 5. **Carry-over**: Annual leave generally cannot be carried over to the next year, but if ┃
┃ work prevents taking leave, the company may arrange for it to be taken by August 31st of  ┃
┃ the following year                                                                        ┃
┃                                                                                           ┃
┃ 6. **Payment**: Annual leave is paid leave (带薪扣减福利假)                               ┃
┃                                                                                           ┃
┃ 7. **Pro-rated Leave**: For employees who join during the year, annual leave is pro-rated ┃
┃ based on remaining calendar days in the year                                              ┃
┃                                                                                           ┃
┃ **Source**: JD Employee Handbook, pages 23-24 (jd-employee-handbook.pdf)                  ┃
┃                                                                                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
(employee-handbook-agent) ➜  employee-handbook-agent (main))
```

---

## 自定义问题

修改 `knowledge_agent.py` 中的测试代码：

```python
if __name__ == "__main__":
    agent.print_response(
        "你的问题",  # 修改这里
        stream=True
    )
```

---

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
A: 非常好！FastEmbed 使用的默认模型是高质量的轻量级模型，在大多数场景下表现优异，而且完全免费、无配额限制。

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
- 下载 FastEmbed 模型（首次使用时自动下载，约 60-100MB）
- 处理整个 PDF 并生成向量
之后的运行会直接使用缓存的向量数据，速度会快很多。

### Q: 首次运行会下载什么？
A: 会自动下载 FastEmbed 的默认 embedding 模型（约 60-100MB），只需下载一次，之后会缓存到本地。

---

## 故障排除

### 问题：HuggingFace rate limit 错误

**错误信息**：
```
429 Client Error: Too Many Requests
We had to rate limit your IP
```

**解决方法**：
1. 等待几分钟后重试（rate limit 会自动重置）
2. 或使用默认模型（代码已配置为使用默认模型，应该不会遇到此问题）

### 问题：找不到 PDF 文件

**错误信息**：
```
FileNotFoundError: ./jd-employee-handbook.pdf
```

**解决方法**：
确保 `jd-employee-handbook.pdf` 在项目根目录。

### 问题：DEEPSEEK_API_KEY 未设置

**错误信息**：
```
ValueError: DEEPSEEK_API_KEY environment variable is not set
```

**解决方法**：
```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

### 问题：清除缓存重新开始

如果需要重新开始：
```bash
# 删除向量数据库
rm -rf tmp/

# 删除模型缓存（如果需要）
rm -rf ~/.cache/fastembed/
```

---

## 技术栈

- **Agent 框架**: agno
- **LLM 模型**: DeepSeek Reasoner（推理和生成答案）
- **向量数据库**: LanceDB（本地存储）
- **Embedding**: FastEmbed（免费本地模型）
- **PDF 处理**: pypdf
- **数据处理**: pandas

## License

MIT

