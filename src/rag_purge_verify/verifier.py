"""核心验证编排逻辑"""
from typing import Dict, Any, Optional
from .engines import BaseEngine, VerificationResult
from .ui import ScannerUI


class Verifier:
    """验证器类"""

    def __init__(self, engine: BaseEngine, ui: ScannerUI):
        self.engine = engine
        self.ui = ui

    def verify(
        self,
        collection: str,
        metadata_filter: Optional[Dict[str, str]] = None,
        text_search: Optional[str] = None
    ) -> Dict[str, Any]:
        """执行验证流程"""
        results = []

        with self.ui.scanning_context(collection):
            # 元数据检查
            if metadata_filter:
                self.ui.update_status(f"检查元数据: {metadata_filter}")
                for key, value in metadata_filter.items():
                    result = self.engine.verify_metadata(collection, key, value)
                    results.append({
                        'found_count': result.found_count,
                        'residue_items': result.residue_items,
                        'query_type': result.query_type
                    })

            # Payload 文本检查
            if text_search:
                self.ui.update_status(f"搜索文本: {text_search}")
                result = self.engine.verify_payload(collection, text_search)
                results.append({
                    'found_count': result.found_count,
                    'residue_items': result.residue_items,
                    'query_type': result.query_type
                })

        # 判定结果
        total_found = sum(r['found_count'] for r in results)

        if total_found == 0:
            self.ui.show_pass_stamp()
        else:
            self.ui.show_fail_alert(results)

        return {
            'passed': total_found == 0,
            'total_found': total_found,
            'results': results
        }
