"""ChromaDB 适配器实现"""
from typing import List
import chromadb
from chromadb.config import Settings
from .import BaseEngine, VerificationResult
from ..exceptions import ConnectionError, CollectionNotFoundError


class ChromaEngine(BaseEngine):
    """ChromaDB 引擎实现"""

    def __init__(self):
        self.client = None

    def connect(self, path: str = None, **kwargs) -> None:
        """连接到 ChromaDB"""
        try:
            if path:
                self.client = chromadb.PersistentClient(path=path)
            else:
                self.client = chromadb.Client()
        except Exception as e:
            raise ConnectionError("ChromaDB", str(e))

    def verify_metadata(
        self,
        collection: str,
        filter_key: str,
        filter_value: str
    ) -> VerificationResult:
        """验证元数据中是否存在残留"""
        try:
            coll = self.client.get_collection(collection)
        except Exception:
            raise CollectionNotFoundError(collection)

        results = coll.get(where={filter_key: filter_value})

        found_count = len(results['ids'])
        residue_items = []

        for i, doc_id in enumerate(results['ids']):
            item = {'id': doc_id}
            if results.get('metadatas') and i < len(results['metadatas']):
                item['metadata'] = results['metadatas'][i]
            residue_items.append(item)

        return VerificationResult(
            found_count=found_count,
            residue_items=residue_items,
            collection_name=collection,
            query_type="metadata"
        )

    def verify_payload(
        self,
        collection: str,
        search_text: str
    ) -> VerificationResult:
        """在 Payload 文本中搜索残留"""
        try:
            coll = self.client.get_collection(collection)
        except Exception:
            raise CollectionNotFoundError(collection)

        results = coll.query(
            query_texts=[search_text],
            n_results=100
        )

        found_count = len(results['ids'][0]) if results['ids'] else 0
        residue_items = []

        if results['ids']:
            for i, doc_id in enumerate(results['ids'][0]):
                item = {'id': doc_id}
                if results.get('documents') and results['documents'][0]:
                    item['text'] = results['documents'][0][i][:100]
                residue_items.append(item)

        return VerificationResult(
            found_count=found_count,
            residue_items=residue_items,
            collection_name=collection,
            query_type="payload"
        )

    def list_collections(self) -> List[str]:
        """列出所有集合"""
        collections = self.client.list_collections()
        return [c.name for c in collections]

    def close(self) -> None:
        """关闭连接"""
        self.client = None
