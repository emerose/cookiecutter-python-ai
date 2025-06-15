# Cookiecutter Python AI Template

An opinionated Python project template designed specifically for use with AI coding agents like Claude, Cursor, and other AI development tools.

## Features

🤖 **AI-Optimized**: Comprehensive documentation and configuration files designed to help AI agents understand and work with your codebase effectively

🏗️ **Modern Python Stack**: Built with cutting-edge Python tooling for 2024+
- Python 3.12+ with strict type checking
- [uv](https://github.com/astral-sh/uv) for fast dependency management
- [pytest](https://pytest.org/) with three-tier test architecture
- [ruff](https://github.com/astral-sh/ruff) for lightning-fast linting and formatting
- [pyright](https://github.com/microsoft/pyright) for comprehensive type checking

📋 **Comprehensive Guidelines**: Extensive documentation including:
- `AGENTS.md` - Detailed coding standards and patterns for AI agents
- `CLAUDE.md` - Claude-specific instructions and project context
- `DEVELOPERS.md` - Human developer onboarding guide
- `PR_CHECKLIST.md` - Mandatory checklist for all pull requests
- `.cursorrules` - Cursor IDE configuration for AI pair programming

🧪 **Three-Tier Testing**: Organized test architecture with performance requirements:
- **Unit tests** (`tests/unit/`) - <100ms, completely isolated
- **Integration tests** (`tests/integration/`) - <500ms, real filesystem access
- **E2E tests** (`tests/e2e/`) - <30s, full workflow testing
- **Static analysis** (`tests/static/`) - Code quality and type checking

⚙️ **Quality Gates**: Built-in quality assurance with `scripts/check` command
- Automated test execution with proper ordering
- Static analysis integration
- CI/CD ready with GitHub Actions

🔧 **Configuration Management**: Immutable configuration pattern with dependency injection using dataclasses

## Quick Start

### Prerequisites

- Python 3.12+
- [cookiecutter](https://cookiecutter.readthedocs.io/) installed

```bash
pip install cookiecutter
```

### Generate a New Project

```bash
# From GitHub (recommended)
cookiecutter gh:yourusername/cookiecutter-python-ai

# Or from local directory
cookiecutter /path/to/cookiecutter-python-ai
```

You'll be prompted for:
- **Project name**: Human-readable name (e.g., "My Awesome Project")
- **Project slug**: Package/directory name (auto-generated: "my_awesome_project")  
- **Project description**: Brief description of your project
- **Author name**: Your name
- **Author email**: Your email address
- **Python version**: Python version requirement (default: 3.12)
- **Version**: Initial version (default: 0.1.0)

### After Generation

1. **Navigate to your project**:
   ```bash
   cd your-project-name
   ```

2. **Install dependencies**:
   ```bash
   uv sync --dev
   ```

3. **Run quality checks**:
   ```bash
   scripts/check
   ```

4. **Start coding**! 🚀

## What You Get

### Project Structure
```
your-project/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── .claude/
│   └── settings.local.json     # Claude permissions
├── src/
│   └── your_project/
│       ├── __init__.py         # Package initialization  
│       ├── __main__.py         # CLI entry point
│       └── config.py           # Configuration management
├── tests/
│   ├── unit/                   # Fast, isolated tests
│   ├── integration/            # Filesystem integration tests  
│   ├── e2e/                    # End-to-end workflow tests
│   └── static/                 # Static analysis tests
├── scripts/
│   └── check                   # Quality gate runner
├── AGENTS.md                   # Comprehensive AI agent guidelines
├── CLAUDE.md                   # Claude-specific instructions
├── DEVELOPERS.md               # Human developer guide
├── PR_CHECKLIST.md            # Mandatory PR checklist
├── .cursorrules               # Cursor IDE configuration
├── .gitignore                 # Git ignore patterns
├── .gitmessage               # Commit message template
└── pyproject.toml            # Project configuration
```

### Key Commands

```bash
# Quality checks (run before every commit)
scripts/check                  # Standard workflow (unit + integration + static)
scripts/check unit             # Unit tests only  
scripts/check static           # Static analysis only
scripts/check all              # Everything including e2e tests

# Manual tools
uv run python -m your_project  # Run your application
uv run pyright                # Type checking
uv run ruff format .           # Code formatting
uv run ruff check .            # Linting
uv run pytest                 # Run tests directly
```

## AI Agent Integration

This template is specifically designed to work seamlessly with AI coding agents:

### For Claude/Claude Code:
- `CLAUDE.md` provides comprehensive project context and coding standards
- `PR_CHECKLIST.md` ensures consistent quality across AI-generated code
- Structured documentation helps Claude understand project patterns

### For Cursor:
- `.cursorrules` file configures Cursor's AI for your specific project
- Comprehensive type hints help AI understand code structure
- Clear testing patterns enable AI to write appropriate tests

### For Any AI Agent:
- `AGENTS.md` contains detailed coding standards, patterns, and examples
- Three-tier test architecture with clear performance requirements
- Immutable configuration patterns with dependency injection
- Domain-specific exception handling guidelines

## Philosophy

This template embodies several key principles:

- **AI-First**: Designed for human-AI collaboration in software development
- **Type Safety**: Comprehensive typing with strict pyright configuration
- **Quality Gates**: Automated quality assurance that must pass before commits
- **YAGNI**: Build only what's needed for current features
- **DRY**: Comprehensive search processes to avoid code duplication
- **Documentation-Driven**: Extensive documentation helps both humans and AI understand the codebase

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Test your changes with `cookiecutter .`
4. Submit a pull request

## License

This template is released under the MIT License. Projects generated from this template are not bound by this license.

---

**Happy coding with AI! 🤖✨**