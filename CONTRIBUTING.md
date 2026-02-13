# Contributing to RAG Purge Verify | 贡献指南

## Project Status | 项目状态

This is currently a personal project maintained by [@PerryLink](https://github.com/PerryLink). While contributions are welcome, please note that this is an early-stage project and development priorities may change.

这是一个由 [@PerryLink](https://github.com/PerryLink) 个人维护的项目。虽然欢迎贡献，但请注意这是一个早期阶段的项目，开发优先级可能会发生变化。

---

## How to Report Issues | 如何报告问题

If you encounter a bug or have a feature request, please:

如果你遇到 bug 或有功能请求，请：

1. Check if the issue already exists in the [Issues](https://github.com/PerryLink/rag-purge-verify/issues) section
2. If not, create a new issue with:
   - A clear, descriptive title
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, database version)
   - Relevant logs or error messages

1. 检查 [Issues](https://github.com/PerryLink/rag-purge-verify/issues) 中是否已存在该问题
2. 如果没有，创建新 issue 并包含：
   - 清晰、描述性的标题
   - 重现步骤（针对 bug）
   - 期望行为 vs 实际行为
   - 你的环境（操作系统、Python 版本、数据库版本）
   - 相关日志或错误信息

---

## Development Environment Setup | 开发环境搭建

### Prerequisites | 前置要求

- Python 3.9 or higher | Python 3.9 或更高版本
- Git
- Docker (optional, for testing Qdrant) | Docker（可选，用于测试 Qdrant）

### Setup Steps | 搭建步骤

1. Fork and clone the repository | Fork 并克隆仓库:

```bash
git clone https://github.com/YOUR_USERNAME/rag-purge-verify.git
cd rag-purge-verify
```

2. Create a virtual environment | 创建虚拟环境:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies | 安装依赖:

```bash
pip install -e ".[dev]"
```

4. (Optional) Start Qdrant for testing | （可选）启动 Qdrant 用于测试:

```bash
docker-compose up -d
```

5. Run tests to verify setup | 运行测试验证安装:

```bash
pytest tests/
```

---

## Code Standards | 代码规范

### Python Style | Python 风格

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide
- Use type hints where appropriate
- Maximum line length: 100 characters

- 遵循 [PEP 8](https://peps.python.org/pep-0008/) 风格指南
- 适当使用类型提示
- 最大行长度：100 字符

### Code Formatting | 代码格式化

Before submitting, format your code with:

提交前，使用以下工具格式化代码：

```bash
# Format code
black src/

# Check for issues
ruff check src/
```

### Testing | 测试

- Write unit tests for new features
- Ensure all tests pass before submitting
- Aim for meaningful test coverage

- 为新功能编写单元测试
- 提交前确保所有测试通过
- 追求有意义的测试覆盖率

```bash
pytest tests/ -v
```

---

## Pull Request Process | Pull Request 流程

1. **Create a feature branch | 创建功能分支**:

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes | 进行修改**:
   - Write clean, documented code
   - Add tests for new functionality
   - Update documentation if needed

   - 编写清晰、有文档的代码
   - 为新功能添加测试
   - 如需要，更新文档

3. **Commit your changes | 提交修改**:

```bash
git add .
git commit -m "feat: add your feature description"
```

Commit message format | 提交信息格式:
- `feat:` for new features | 新功能
- `fix:` for bug fixes | bug 修复
- `docs:` for documentation | 文档
- `refactor:` for code refactoring | 代码重构
- `test:` for adding tests | 添加测试

4. **Push to your fork | 推送到你的 fork**:

```bash
git push origin feature/your-feature-name
```

5. **Create a Pull Request | 创建 Pull Request**:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template with:
     - Description of changes
     - Related issue number (if applicable)
     - Testing performed
     - Screenshots (if UI changes)

   - 前往原始仓库
   - 点击 "New Pull Request"
   - 选择你的分支
   - 填写 PR 模板，包含：
     - 修改描述
     - 相关 issue 编号（如适用）
     - 执行的测试
     - 截图（如有 UI 变更）

---

## Development Guidelines | 开发指南

### Adding Support for New Vector Databases | 添加新向量数据库支持

To add a new database adapter:

添加新数据库适配器：

1. Create a new file in `src/rag_purge_verify/engines/`
2. Implement the `BaseEngine` abstract class
3. Add tests in `tests/`
4. Update documentation

1. 在 `src/rag_purge_verify/engines/` 创建新文件
2. 实现 `BaseEngine` 抽象类
3. 在 `tests/` 添加测试
4. 更新文档

### Project Structure | 项目结构

```
src/rag_purge_verify/
├── engines/          # Database adapters
├── cli.py            # CLI commands
├── verifier.py       # Core verification logic
├── ui.py             # Terminal UI
└── exceptions.py     # Custom exceptions
```

---

## Questions? | 有问题？

Feel free to:
- Open an issue for discussion
- Email: novelnexusai@outlook.com
- Check existing issues and PRs

随时可以：
- 开启 issue 进行讨论
- 发送邮件：novelnexusai@outlook.com
- 查看现有的 issues 和 PRs

---

Thank you for contributing! | 感谢你的贡献！

[@PerryLink](https://github.com/PerryLink)
