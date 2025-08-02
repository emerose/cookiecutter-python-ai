# Claude Code Instructions for {{cookiecutter.project_name}} Project

## 🛑 STOP: Planning is MANDATORY

**Before writing ANY code for non-trivial tasks:**
1. **READ** [Planning Guide](docs/coding-agents/PLANNING.md) 
2. **CREATE** TODO.md following the planning process
3. **GET APPROVAL** - User must explicitly approve TODO.md
4. **ONLY THEN** proceed to implementation

**This includes:** refactoring, new features, multi-file changes, architecture changes, or any task estimated > 30 minutes.

## 🚨 CRITICAL REQUIREMENT

**Before submitting ANY pull request, you MUST complete the comprehensive PR checklist in the [Submission Guide](docs/coding-agents/SUBMISSION.md). This is mandatory and non-negotiable.**

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

**For detailed guidance, follow the workflow-based documentation:**

1. **[Planning Guide](docs/coding-agents/PLANNING.md)** - Before you code: GitHub issues, research, TODO.md process
2. **[Development Guide](docs/coding-agents/DEVELOPMENT.md)** - While you code: standards, patterns, testing  
3. **[Submission Guide](docs/coding-agents/SUBMISSION.md)** - Before you submit: PR checklist, quality gates

**Quick reference: [AGENTS.md](AGENTS.md)**

## Key Principles

- **YAGNI**: Build only what's needed for current features
- **DRY**: Search for existing functionality before implementing new code
- **Type Safety**: Strict pyright mode, avoid `Any`, minimize `None` returns
- **Testing**: Three-tier architecture with fakes over mocks
- **Configuration**: Immutable dataclasses with dependency injection
- **Dependencies**: Get approval before adding libraries
- **Fail Early**: Adhere to the design principle of failing early. It's important to raise errors as soon as they are detected to prevent the system from falling back to alternative behaviors that could obfuscate the problem.

## Development Workflow

1. **Plan (MANDATORY for non-trivial tasks)**: 
   - Read [Planning Guide](docs/coding-agents/PLANNING.md) FIRST
   - Create TODO.md and get explicit user approval
   - NO CODING until TODO.md is approved!
2. **Implement**: Write code following standards (see [Development Guide](docs/coding-agents/DEVELOPMENT.md))
3. **Test**: Add/update tests with clear intention comments
4. **Check**: Run `scripts/check` to ensure quality
5. **Commit**: Use conventional commit format
6. **Pull Request**: Complete PR checklist in [Submission Guide](docs/coding-agents/SUBMISSION.md) before submitting

## Quality Requirements

- **MANDATORY: Complete PR checklist** - every item before submitting any PR (see [Submission Guide](docs/coding-agents/SUBMISSION.md))
- **Google-style docstrings** on all public functions, methods, and classes
- **Type annotations everywhere** - comprehensive typing required
- **Test intention comments** - every test must explain what it's testing

---

**For detailed implementation guidance, see the workflow guides in [docs/coding-agents/](docs/coding-agents/). For quick reference, see [AGENTS.md](AGENTS.md).**