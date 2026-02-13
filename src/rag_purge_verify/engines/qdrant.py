"""Qdrant 适配器实现"""
from typing import List
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue, MatchText
from .import BaseEngine, VerificationResult
from ..exceptions import ConnectionError, CollectionNotFoundError


class QdrantEngine(BaseEngine):
    """Qdrant 引擎实现"""

    def __init__(self):
        self.client = None

    def connect(self, host: str = "localhost", port: int = 6333, api_key: str = None, **kwargs) -> None:
        """连接到 Qdrant"""
        try:
            self.client = QdrantClient(host=host, port=port, api_key=api_key)
            # 测试连接
            self.client.get_collections()
        except Exception as e:
            raise ConnectionError("Qdrant", str(e))

    def verify_metadata(
        self,
        collection: str,
        filter_key: str,
        filter_value: str
    ) -> VerificationResult:
        """验证元数据中是否存在残留"""
        try:
            filter_condition = Filter(
                must=[FieldCondition(key=filter_key, match=MatchValue(value=filter_value))]
            )

            results = self.client.scroll(
                collection_name=collection,
                scroll_filter=filter_condition,
                limit=100
            )

            points = results[0]
            found_count = len(points)
            residue_items = []

            for point in points:
                item = {'id': str(point.id), 'metadata': point.payload}
                residue_items.append(item)

            return VerificationResult(
                found_count=found_count,
                residue_items=residue_items,
                collection_name=collection,
                query_type="metadata"
            )
        except Exception as e:
            if "not found" in str(e).lower():
                raise CollectionNotFoundError(collection)
            raise

    def verify_payload(
        self,
        collection: str,
        search_text: str
    ) -> VerificationResult:
        """在 Payload 文本中搜索残留"""
        try:
            # 使用 scroll 搜索包含文本的 payload
            results = self.client.scroll(
                collection_name=collection,
                limit=100
            )

            points = results[0]
            matching_points = []

            # 在 payload 中搜索文本
            for point in points:
                payload_str = str(point.payload)
                if search_text.lower() in payload_str.lower():
                    matching_points.append(point)

            found_count = len(matching_points)
            residue_items = []

            for point in matching_points:
                item = {'id': str(point.id), 'payload': point.payload}
                residue_items.append(item)

            return VerificationResult(
                found_count=found_count,
                residue_items=residue_items,
                collection_name=collection,
                query_type="payload"
            )
        except Exception as e:
            if "not found" in str(e).lower():
                raise CollectionNotFoundError(collection)
            raise

    def list_collections(self) -> List[str]:
        """列出所有集合"""
        collections = self.client.get_collections()
        return [c.name for c in collections.collections]

    def close(self) -> None:
        """关闭连接"""
        if self.client:
            self.client.close()
