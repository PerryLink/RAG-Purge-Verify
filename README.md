# RAG-Purge-Verify
Verifies complete user data deletion from vector databases after GDPR requests. While SQL records are easily deleted, embeddings may retain PII. This tool performs metadata and payload text checks on ChromaDB and Qdrant, displaying visual PASSED/FAILED results. Built with Python, Typer, and Rich for intuitive CLI verification.
