"""CLI 命令定义"""
import typer
from typing import Optional
from rich.console import Console
from .engines.chroma import ChromaEngine
from .engines.qdrant import QdrantEngine
from .ui import ScannerUI
from .verifier import Verifier
from .exceptions import RagVerifyError

app = typer.Typer(help="RAG 系统 GDPR 合规验证工具")
console = Console()


@app.command()
def chroma(
    collection: str = typer.Option(..., "--collection", "-c", help="集合名称"),
    path: Optional[str] = typer.Option(None, "--path", "-p", help="ChromaDB 持久化路径"),
    user_id: Optional[str] = typer.Option(None, "--user-id", "-u", help="用户 ID（元数据过滤）"),
    text: Optional[str] = typer.Option(None, "--text", "-t", help="搜索文本（Payload 检查）"),
):
    """验证 ChromaDB 中的数据残留"""
    if not user_id and not text:
        console.print("[red]错误: 必须指定 --user-id 或 --text 参数[/red]")
        raise typer.Exit(1)

    try:
        engine = ChromaEngine()
        engine.connect(path=path)

        ui = ScannerUI()
        verifier = Verifier(engine, ui)

        metadata_filter = {"user_id": user_id} if user_id else None
        verifier.verify(collection, metadata_filter=metadata_filter, text_search=text)

        engine.close()
    except RagVerifyError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1)


@app.command()
def qdrant(
    collection: str = typer.Option(..., "--collection", "-c", help="集合名称"),
    host: str = typer.Option("localhost", "--host", "-h", help="Qdrant 主机"),
    port: int = typer.Option(6333, "--port", "-p", help="Qdrant 端口"),
    api_key: Optional[str] = typer.Option(None, "--api-key", "-k", help="API 密钥"),
    user_id: Optional[str] = typer.Option(None, "--user-id", "-u", help="用户 ID（元数据过滤）"),
    text: Optional[str] = typer.Option(None, "--text", "-t", help="搜索文本（Payload 检查）"),
):
    """验证 Qdrant 中的数据残留"""
    if not user_id and not text:
        console.print("[red]错误: 必须指定 --user-id 或 --text 参数[/red]")
        raise typer.Exit(1)

    try:
        engine = QdrantEngine()
        engine.connect(host=host, port=port, api_key=api_key)

        ui = ScannerUI()
        verifier = Verifier(engine, ui)

        metadata_filter = {"user_id": user_id} if user_id else None
        verifier.verify(collection, metadata_filter=metadata_filter, text_search=text)

        engine.close()
    except RagVerifyError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1)


@app.command()
def list_collections(
    db_type: str = typer.Argument(..., help="数据库类型 (chroma/qdrant)"),
    path: Optional[str] = typer.Option(None, "--path", "-p", help="ChromaDB 路径"),
    host: str = typer.Option("localhost", "--host", "-h", help="Qdrant 主机"),
    port: int = typer.Option(6333, "--port", help="Qdrant 端口"),
):
    """列出所有集合"""
    try:
        if db_type == "chroma":
            engine = ChromaEngine()
            engine.connect(path=path)
        elif db_type == "qdrant":
            engine = QdrantEngine()
            engine.connect(host=host, port=port)
        else:
            console.print(f"[red]不支持的数据库类型: {db_type}[/red]")
            raise typer.Exit(1)

        collections = engine.list_collections()
        console.print(f"\n[green]找到 {len(collections)} 个集合:[/green]")
        for coll in collections:
            console.print(f"  - {coll}")
        console.print()

        engine.close()
    except RagVerifyError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
