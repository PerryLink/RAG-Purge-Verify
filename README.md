# RAG Purge Verify

**GDPR Compliance Tool: Verify Complete Data Deletion in RAG Systems**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Core Value

Transform from "I deleted the data" to "I can prove the data is deleted."

When users exercise their GDPR "right to be forgotten," developers can delete records from relational databases, but embedding data in vector databases may still contain user privacy information. This tool provides a dual verification mechanism to ensure data is completely removed and avoid compliance risks.

## 核心价值

从"我删除了数据"到"我能证明数据已删除"的转变。

当用户行使 GDPR "被遗忘权"时，开发者可以删除关系数据库中的记录，但向量数据库中的嵌入数据（embeddings）可能仍然残留用户的隐私信息。本工具提供双重验证机制，确保数据被彻底清除，避免合规风险。

---

## Features | 功能特性

- ✅ **Dual Verification Mechanism | 双重验证机制**
  - Metadata Check: Verify if user IDs and other metadata remain
  - Payload Text Check: Search for PII (Personally Identifiable Information) in document content
  - 元数据检查：验证用户 ID 等元数据是否残留
  - Payload 文本检查：搜索文档内容中的 PII（个人身份信息）

- ✅ **Support for Mainstream Vector Databases | 支持主流向量数据库**
  - ChromaDB
  - Qdrant

- ✅ **Visual Experience | 视觉化体验**
  - Radar scanning animation | 雷达扫描动画
  - PASSED/FAILED stamp effects | PASSED/FAILED 盖章效果
  - Detailed residue data reports | 详细的残留数据报告

---

## Quick Start | 快速开始

### Installation | 安装

```bash
pip install rag-purge-verify
```

Or install from source | 或从源码安装:

```bash
git clone https://github.com/PerryLink/rag-purge-verify.git
cd rag-purge-verify
pip install -e .
```

### ChromaDB Verification | ChromaDB 验证

```bash
# Verify if user data remains in metadata | 验证元数据中是否残留用户数据
rag-verify chroma --collection user_docs --user-id user_123

# Verify if PII remains in document content | 验证文档内容中是否残留 PII
rag-verify chroma --collection chat_history --text "alice@example.com"

# Specify ChromaDB path | 指定 ChromaDB 路径
rag-verify chroma --collection user_docs --path ./chroma_db --user-id user_123
```

### Qdrant Verification | Qdrant 验证

```bash
# Verify metadata | 验证元数据
rag-verify qdrant --collection user_docs --user-id user_123

# Verify document content | 验证文档内容
rag-verify qdrant --collection chat_history --text "alice@example.com"

# Specify Qdrant server | 指定 Qdrant 服务器
rag-verify qdrant --collection user_docs --host localhost --port 6333 --user-id user_123
```

### List All Collections | 列出所有集合

```bash
# ChromaDB
rag-verify list-collections chroma

# Qdrant
rag-verify list-collections qdrant --host localhost --port 6333
```

---

## Usage Scenarios | 使用场景

### Scenario 1: Verification After GDPR Deletion Request | 场景 1: GDPR 删除请求后验证

```bash
# 1. User requests data deletion | 用户请求删除数据
# 2. Delete user records from relational database | 从关系数据库删除用户记录
# 3. Delete related data from vector database | 从向量数据库删除相关数据
# 4. Run verification tool to confirm successful deletion | 运行验证工具确认删除成功

rag-verify chroma --collection user_embeddings --user-id user_12345
```

**Expected Result | 预期结果**: Display green PASSED stamp, confirming no residual data | 显示绿色 PASSED 盖章，确认无残留数据。

### Scenario 2: Detect PII Leakage | 场景 2: 检测 PII 泄露

```bash
# Search for email addresses remaining in documents | 搜索是否有邮箱地址残留在文档中
rag-verify qdrant --collection support_tickets --text "customer@example.com"
```

**Expected Result | 预期结果**: If residue is found, display red FAILED alert with details | 如果发现残留，显示红色 FAILED 警报并列出详情。

---

## Project Structure | 项目结构

```
rag-purge-verify/
├── src/rag_purge_verify/
│   ├── __init__.py
│   ├── __main__.py           # Entry point | 入口点
│   ├── cli.py                # CLI command definitions | CLI 命令定义
│   ├── engines/              # Database adapter layer | 数据库适配器层
│   │   ├── __init__.py       # BaseEngine abstract class | BaseEngine 抽象类
│   │   ├── chroma.py         # ChromaDB implementation | ChromaDB 实现
│   │   └── qdrant.py         # Qdrant implementation | Qdrant 实现
│   ├── verifier.py           # Core verification logic | 核心验证逻辑
│   ├── ui.py                 # Rich animation effects | Rich 动画效果
│   └── exceptions.py         # Exception system | 异常体系
├── tests/                    # Unit tests | 单元测试
├── pyproject.toml            # Project configuration | 项目配置
├── docker-compose.yml        # Local Qdrant test environment | 本地 Qdrant 测试环境
├── LICENSE                   # Apache 2.0 License
├── CONTRIBUTING.md           # Contribution guidelines | 贡献指南
└── README.md                 # This file | 本文件
```

---

## Tech Stack | 技术栈

- **Python 3.9+**: Main development language | 主要开发语言
- **typer**: CLI framework | CLI 框架
- **rich**: Terminal UI animations | 终端 UI 动画
- **chromadb**: ChromaDB client | ChromaDB 客户端
- **qdrant-client**: Qdrant client | Qdrant 客户端
- **pydantic**: Data validation | 数据验证

---

## Development | 开发

### Install Development Dependencies | 安装开发依赖

```bash
pip install -e ".[dev]"
```

### Run Tests | 运行测试

```bash
pytest tests/
```

### Code Formatting | 代码格式化

```bash
black src/
ruff check src/
```

### Local Test Environment | 本地测试环境

Use Docker Compose to start Qdrant test environment | 使用 Docker Compose 启动 Qdrant 测试环境:

```bash
docker-compose up -d
```

---

## Notes | 注意事项

1. **Performance | 性能**: Current version is suitable for small to medium-scale datasets. Large datasets may require longer processing time. | 当前版本适用于中小规模数据集。大规模数据集可能需要较长时间。
2. **Accuracy | 准确性**: Text search is based on simple string matching and may produce false positives or negatives. | 文本搜索基于简单的字符串匹配，可能产生误报或漏报。
3. **Security | 安全性**: This tool is for verification only and does not perform deletion operations. | 本工具仅用于验证，不执行删除操作。

---

## Roadmap | 路线图

- [ ] Support for more vector databases (Pinecone, Milvus, Weaviate) | 支持更多向量数据库
- [ ] PDF compliance report export | PDF 合规报告导出
- [ ] Regular expression support | 正则表达式支持
- [ ] Batch verification of multiple collections | 批量验证多个集合
- [ ] Web UI interface | Web UI 界面

---

## License | 许可证

Apache License 2.0 - see [LICENSE](LICENSE) file for details

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

---

## Contributing | 贡献

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

欢迎贡献！详情请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## Contact | 联系方式

- GitHub: [@PerryLink](https://github.com/PerryLink)
- Email: novelnexusai@outlook.com
- Project: [rag-purge-verify](https://github.com/PerryLink/rag-purge-verify)
