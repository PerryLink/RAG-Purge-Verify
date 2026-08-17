<div align="center">

# RAG-Purge-Verify

**A GDPR compliance tool that verifies whether user data has been completely removed from a RAG system's vector database.**

*Ported into [dsh-library](https://github.com/PerryLink/dsh-library) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

When a user exercises the GDPR "right to be forgotten", deleting records from a relational database is not enough — embeddings in a vector database can still hold their data. RAG-Purge-Verify checks a vector database for residual user data and reports PASSED or FAILED, so "we deleted the data" becomes "we can prove the data is deleted".

## Features

- Two verification modes:
  - Metadata check — search by user ID
  - Payload text check — search document contents for PII
- Supports ChromaDB and Qdrant
- Radar scanning animation with PASSED / FAILED result stamps and residue reports
- Lists available collections

## Quick start

Requires Python 3.9+.

```bash
git clone https://github.com/PerryLink/RAG-Purge-Verify.git
cd RAG-Purge-Verify
pip install -e .
```

## Usage

Each check requires either `--user-id` (metadata check) or `--text` (payload check).

```bash
# ChromaDB — check for a user ID in metadata
rag-verify chroma --collection user_docs --user-id user_123

# ChromaDB — search document contents for PII
rag-verify chroma --collection chat_history --text "alice@example.com"

# ChromaDB — specify a persistence path
rag-verify chroma --collection user_docs --path ./chroma_db --user-id user_123

# Qdrant — check a remote server
rag-verify qdrant --collection user_docs --host localhost --port 6333 --user-id user_123

# List collections
rag-verify list-collections chroma
rag-verify list-collections qdrant --host localhost --port 6333
```

### Typical scenarios

After a GDPR deletion request, delete the user's records and then confirm nothing remains:

```bash
rag-verify chroma --collection user_embeddings --user-id user_12345
```

A green PASSED stamp means no residual data was found.

To detect PII that may still be in document content:

```bash
rag-verify qdrant --collection support_tickets --text "customer@example.com"
```

If residue is found, a red FAILED alert lists the details.

## Notes

- **Performance** — built for small to medium datasets; large datasets may take longer.
- **Accuracy** — text search uses simple string matching and can produce false positives or negatives.
- **Safety** — this tool only verifies; it never deletes data.

Built with Typer, Rich, chromadb, qdrant-client, and pydantic.

## Development

```bash
pip install -e ".[dev]"
pytest tests/
```

A local Qdrant instance for testing can be started with `docker-compose up -d`.

## Related

- [dsh-library](https://github.com/PerryLink/dsh-library) — the DSH plugin this tool was ported into
- [PerryLink](https://github.com/PerryLink) — the PerryLink DSH Plugin Family

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
