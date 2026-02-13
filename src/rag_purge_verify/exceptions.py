"""自定义异常类"""


class RagVerifyError(Exception):
    """基础异常"""
    pass


class ConnectionError(RagVerifyError):
    """连接失败异常"""
    def __init__(self, db_type: str, details: str):
        self.db_type = db_type
        self.details = details
        super().__init__(
            f"无法连接到 {db_type}。\n"
            f"详情: {details}\n\n"
            f"故障排查:\n"
            f"1. 检查数据库服务是否运行\n"
            f"2. 验证连接参数（host/port/path）\n"
            f"3. 检查网络连接和防火墙设置"
        )


class CollectionNotFoundError(RagVerifyError):
    """集合不存在异常"""
    def __init__(self, collection_name: str):
        super().__init__(f"集合 '{collection_name}' 不存在")


class InvalidFilterError(RagVerifyError):
    """无效的过滤参数异常"""
    pass
