"""数据库引擎抽象层"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class VerificationResult:
    """验证结果数据类"""
    found_count: int
    residue_items: List[Dict[str, Any]] = field(default_factory=list)
    collection_name: str = ""
    query_type: str = ""  # "metadata" 或 "payload"


class BaseEngine(ABC):
    """数据库引擎抽象基类"""

    @abstractmethod
    def connect(self, **kwargs) -> None:
        """建立数据库连接"""
        pass

    @abstractmethod
    def verify_metadata(
        self,
        collection: str,
        filter_key: str,
        filter_value: str
    ) -> VerificationResult:
        """验证元数据中是否存在残留"""
        pass

    @abstractmethod
    def verify_payload(
        self,
        collection: str,
        search_text: str
    ) -> VerificationResult:
        """在 Payload 文本中搜索残留"""
        pass

    @abstractmethod
    def list_collections(self) -> List[str]:
        """列出所有集合"""
        pass

    @abstractmethod
    def close(self) -> None:
        """关闭连接"""
        pass
