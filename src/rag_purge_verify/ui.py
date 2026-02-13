"""Rich UI 动画效果"""
from contextlib import contextmanager
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.text import Text
from typing import List, Dict, Any


class ScannerUI:
    """扫描器 UI 类"""

    def __init__(self):
        self.console = Console()
        self.progress = None
        self.task_id = None

    @contextmanager
    def scanning_context(self, collection_name: str):
        """扫描进度上下文管理器"""
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        )
        self.progress.start()
        self.task_id = self.progress.add_task(
            f"正在扫描集合 '{collection_name}'...",
            total=None
        )
        try:
            yield self
        finally:
            self.progress.stop()

    def update_status(self, message: str):
        """更新扫描状态"""
        if self.progress and self.task_id is not None:
            self.progress.update(self.task_id, description=message)

    def show_pass_stamp(self):
        """显示 PASSED 盖章"""
        stamp = Text()
        stamp.append("\n")
        stamp.append("  ██████╗  █████╗ ███████╗███████╗███████╗██████╗ \n", style="bold green")
        stamp.append("  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗\n", style="bold green")
        stamp.append("  ██████╔╝███████║███████╗███████╗█████╗  ██║  ██║\n", style="bold green")
        stamp.append("  ██╔═══╝ ██╔══██║╚════██║╚════██║██╔══╝  ██║  ██║\n", style="bold green")
        stamp.append("  ██║     ██║  ██║███████║███████║███████╗██████╔╝\n", style="bold green")
        stamp.append("  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═════╝ \n", style="bold green")
        stamp.append("\n")

        panel = Panel(
            stamp,
            title="✓ 验证通过",
            border_style="green",
            padding=(1, 2)
        )
        self.console.print(panel)
        self.console.print("[green]未发现数据残留，符合 GDPR 合规要求。[/green]\n")

    def show_fail_alert(self, results: List[Dict[str, Any]]):
        """显示 FAILED 警报"""
        alert = Text()
        alert.append("\n")
        alert.append("  ███████╗ █████╗ ██╗██╗     ███████╗██████╗ \n", style="bold red")
        alert.append("  ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗\n", style="bold red")
        alert.append("  █████╗  ███████║██║██║     █████╗  ██║  ██║\n", style="bold red")
        alert.append("  ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║\n", style="bold red")
        alert.append("  ██║     ██║  ██║██║███████╗███████╗██████╔╝\n", style="bold red")
        alert.append("  ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ \n", style="bold red")
        alert.append("\n")

        panel = Panel(
            alert,
            title="✗ 验证失败",
            border_style="red",
            padding=(1, 2)
        )
        self.console.print(panel)

        # 显示详情
        total_count = sum(r['found_count'] for r in results)
        self.console.print(f"[red]发现 {total_count} 条数据残留！[/red]\n")

        for result in results:
            if result['found_count'] > 0:
                self.console.print(f"[yellow]检查类型:[/yellow] {result['query_type']}")
                self.console.print(f"[yellow]残留数量:[/yellow] {result['found_count']}")

                if result.get('residue_items'):
                    self.console.print("[yellow]残留样本:[/yellow]")
                    for idx, item in enumerate(result['residue_items'][:3], 1):
                        self.console.print(f"  {idx}. {item}")
                self.console.print()
