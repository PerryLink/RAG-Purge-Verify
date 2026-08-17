<div align="center">

# RAG-Purge-Verify

**用于验证用户数据是否已从 RAG 系统的向量数据库中彻底删除的 GDPR 合规工具。**

*已移植到 [dsh-library](https://github.com/PerryLink/dsh-library) —— PerryLink DSH 插件家族的一员。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

当用户行使 GDPR「被遗忘权」时，仅从关系数据库中删除记录是不够的——向量数据库中的嵌入数据仍可能残留其信息。RAG-Purge-Verify 会检查向量数据库中是否残留用户数据，并给出 PASSED 或 FAILED 结论，让「我们删除了数据」变成「我们能证明数据已删除」。

## 功能特性

- 两种验证模式：
  - 元数据检查——按用户 ID 检索
  - Payload 文本检查——在文档内容中搜索 PII
- 支持 ChromaDB 与 Qdrant
- 雷达扫描动画与 PASSED / FAILED 结果盖章
- 列出可用集合

本工具仅做验证，不执行任何删除操作。

## 快速开始

需要 Python 3.9+。

```bash
git clone https://github.com/PerryLink/RAG-Purge-Verify.git
cd RAG-Purge-Verify
pip install -e .
```

## 使用方法

每次检查需提供 `--user-id`（元数据检查）或 `--text`（Payload 检查）之一。

```bash
# ChromaDB——检查元数据中是否残留用户 ID
rag-verify chroma --collection user_docs --user-id user_123

# ChromaDB——在文档内容中搜索 PII
rag-verify chroma --collection chat_history --text "alice@example.com"

# Qdrant——检查远程服务器
rag-verify qdrant --collection user_docs --host localhost --port 6333 --user-id user_123

# 列出集合
rag-verify list-collections chroma
```

## 开发

```bash
pip install -e ".[dev]"
pytest tests/
```

可使用 `docker-compose up -d` 启动本地 Qdrant 测试实例。

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
