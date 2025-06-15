# Claude Code Instructions for {{cookiecutter.project_name}} Project

## 🚨 CRITICAL REQUIREMENT

**Before submitting ANY pull request, you MUST complete every item in `PR_CHECKLIST.md`. This is mandatory and non-negotiable.**

## Project Overview
This is a Python application called "{{cookiecutter.project_slug}}" using modern Python tooling (uv, pytest, ruff, pyright).

## Development Setup
- **Python 3.12+** required
- **uv** for dependency management  
- **Development dependencies**: pytest, ruff, pyright

## Key Commands
```bash
# Install dependencies
uv sync --dev

# Quality checks  
scripts/check              # Standard workflow (unit + integration + static)
scripts/check unit         # Unit tests only
scripts/check static       # Static analysis only
scripts/check all          # Everything including e2e tests

# Manual tools
uv run pytest             # Run tests directly
uv run ruff check .        # Lint code
uv run ruff format .       # Format code
uv run pyright            # Type check
uv run python -m {{cookiecutter.project_slug}}     # Run application
```

## Project Structure
```
{{cookiecutter.project_slug}}/
├── src/{{cookiecutter.project_slug}}/          # Main package
├── tests/              # Three-tier test architecture
│   ├── unit/          # <100ms, isolated
│   ├── integration/   # <500ms, real filesystem
│   └── e2e/           # <30s, full workflows
├── scripts/check      # Quality gate script
├── AGENTS.md          # AI contributor guidelines (comprehensive)
├── DEVELOPERS.md      # Human developer guide
├── .cursorrules       # Cursor IDE configuration
└── PR_CHECKLIST.md   # Pull request checklist
```

## Comprehensive Coding Standards

**For all coding standards, design principles, testing philosophy, type safety guidelines, exception handling, configuration patterns, and architecture patterns, see [AGENTS.md](AGENTS.md).**

Key principles:
- **YAGNI**: Build only what's needed for current features
- **DRY**: Search for existing functionality before implementing new code
- **Type Safety**: Strict pyright mode, avoid `Any`, minimize `None` returns
- **Testing**: Three-tier architecture with fakes over mocks
- **Configuration**: Immutable dataclasses with dependency injection
- **Dependencies**: Get approval before adding libraries

## Git Workflow

### Branch Creation & Commit Format
Follow conventional commits as detailed in [AGENTS.md](AGENTS.md):
```bash
# Branch naming
git checkout -b feature/description
git checkout -b fix/description

# Commit format  
feat(scope): description
fix(scope): description
docs(scope): description
test(scope): description
```

### Development Process
1. **Plan**: For significant changes, create TODO.md with user approval (see [AGENTS.md](AGENTS.md))
2. **Implement**: Write code following standards in [AGENTS.md](AGENTS.md)
3. **Test**: Add/update tests with clear intention comments
4. **Check**: Run `scripts/check` to ensure quality
5. **Commit**: Use conventional commit format
6. **Push**: Push branch to remote repository
7. **Pull Request**: Open PR on GitHub for review
8. **Review**: Address all review comments
9. **Complete**: Task complete when PR is approved and merged

### Quality Gates
Before pushing any changes:
```bash
scripts/check  # Must pass all tests and quality checks
```

## Documentation Requirements
- **Google-style docstrings** on all public functions, methods, and classes
- **Type annotations everywhere** - comprehensive typing required
- **Test intention comments** - every test must explain what it's testing
- **MANDATORY: Complete PR_CHECKLIST.md** - MUST complete every item before submitting any PR

## Configuration Management
Use immutable configuration objects and dependency injection as detailed in [AGENTS.md](AGENTS.md):

```python
from {{cookiecutter.project_slug}}.config import {{cookiecutter.project_class_name}}Config, RuntimeOptions

# Immutable static configuration
config = {{cookiecutter.project_class_name}}Config.from_env()

# Mutable runtime options  
runtime = RuntimeOptions(verbose=True, dry_run=False)

# Dependency injection
class MyService:
    def __init__(self, config: {{cookiecutter.project_class_name}}Config, runtime: RuntimeOptions):
        self.config = config
        self.runtime = runtime
```

## Exception Handling
Use domain-specific exceptions when they add semantic value, built-in exceptions for simple validation. See [AGENTS.md](AGENTS.md) for comprehensive guidelines on when to create custom exceptions vs using built-in ones like `ValueError`, `TypeError`, etc.

## Testing Architecture
Three-tier testing with performance requirements detailed in [AGENTS.md](AGENTS.md):

1. **Unit Tests** (`tests/unit/`) - <100ms, completely isolated
2. **Integration Tests** (`tests/integration/`) - <500ms, real filesystem  
3. **E2E Tests** (`tests/e2e/`) - <30s, full workflows

**Key Testing Principles:**
- **Leverage strict typing** - don't test what pyright already validates
- **Test business logic only** - not implementation details or framework code
- **Never test third-party code** - only test your business logic
- **Quality over quantity** - fewer meaningful tests are better
- **Use fakes over mocks** for better, more maintainable tests

## Project Management

### Issue Tracking
- **Use GitHub Issues** for all task tracking
- **Link PRs to issues** using "Fixes #123" or "Addresses #456"
- **Update issue status** with progress comments

### Versioning
- **Semantic Versioning**: Use vX.Y.Z format
- **Git tags**: Create tags for releases (`v0.1.0`, `v0.2.0`)
- **No dependencies without approval**: Propose library options first

### CI/CD
- GitHub Actions runs tests, linting, and type checking
- Tests run on Python 3.12
- All checks must pass for PRs

---

**For detailed implementation guidance, code examples, and comprehensive standards, refer to [AGENTS.md](AGENTS.md).**