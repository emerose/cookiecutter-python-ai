# Claude Code Instructions for {{cookiecutter.project_name}} Project

## 🚨 CRITICAL REQUIREMENT

**Before submitting ANY pull request, you MUST complete every item in `PR_CHECKLIST.md`. This is mandatory and non-negotiable.**

## Project Overview
This is a Python application called "{{cookiecutter.project_slug}}" using modern Python tooling (uv, pytest, ruff, pyright).

## Quick Start
```bash
# Install dependencies
uv sync --dev

# Run quality checks
scripts/check

# Run application
uv run python -m {{cookiecutter.project_slug}}
```

## Comprehensive Guidelines

**For complete coding standards, design principles, testing philosophy, configuration patterns, command examples, and detailed implementation guidance, see [AGENTS.md](AGENTS.md).**

## Key Principles
- **YAGNI**: Build only what's needed for current features
- **DRY**: Search for existing functionality before implementing new code  
- **Type Safety**: Strict pyright mode, avoid `Any`, minimize `None` returns
- **Testing**: Three-tier architecture with fakes over mocks
- **Configuration**: Immutable dataclasses with dependency injection
- **Dependencies**: Get approval before adding libraries

## Development Workflow
1. **Plan**: For significant changes, create TODO.md with user approval
2. **Implement**: Write code following standards in [AGENTS.md](AGENTS.md)
3. **Test**: Add/update tests with clear intention comments
4. **Check**: Run `scripts/check` to ensure quality
5. **Commit**: Use conventional commit format
6. **Pull Request**: Complete [PR_CHECKLIST.md](PR_CHECKLIST.md) before submitting

## Quality Requirements
- **MANDATORY: Complete PR_CHECKLIST.md** - every item before submitting any PR
- **Google-style docstrings** on all public functions, methods, and classes
- **Type annotations everywhere** - comprehensive typing required
- **Test intention comments** - every test must explain what it's testing

---

**For detailed implementation guidance, code examples, command reference, security guidelines, project management practices, and comprehensive standards, refer to [AGENTS.md](AGENTS.md).**