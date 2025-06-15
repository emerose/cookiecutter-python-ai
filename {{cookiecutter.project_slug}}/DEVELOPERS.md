# Developer Guide

This guide is for human developers working on the {{cookiecutter.project_slug}} project. For AI agent guidelines, see [AGENTS.md](AGENTS.md).

## Quick Start

1. **Clone and setup**:
   ```bash
   git clone <repository-url>
   cd {{cookiecutter.project_slug}}
   uv sync --dev
   ```

2. **Run tests and checks**:
   ```bash
   scripts/check          # Run standard checks (unit + integration + static)
   scripts/check all      # Run everything including e2e tests
   ```

3. **Development workflow**:
   - Create feature branch: `git checkout -b feature/my-feature`
   - Make changes following coding standards in [AGENTS.md](AGENTS.md)
   - Run `scripts/check` to ensure quality
   - Commit using conventional format: `feat(scope): description`
   - Push and create PR on GitHub

## Project Structure

```
{{cookiecutter.project_slug}}/
├── src/{{cookiecutter.project_slug}}/              # Main package
│   ├── __init__.py         # Package initialization  
│   ├── __main__.py         # CLI entry point
│   ├── config.py           # Configuration classes
│   ├── exceptions.py       # Custom exception hierarchy
│   └── services.py         # Core business logic
├── tests/                  # Three-tier test architecture
│   ├── unit/              # Unit tests (<100ms, isolated)
│   ├── integration/       # Integration tests (<500ms, real filesystem)
│   ├── e2e/               # End-to-end tests (<30s, full workflows)
│   └── static/            # Static analysis tests
├── scripts/               # Development tools
│   └── check              # Quality gate script
└── .github/workflows/     # CI/CD automation
```

## Development Tools

### Testing
- **pytest**: Test framework with three performance tiers
- **Coverage**: Track test coverage with `--cov`
- **Timeouts**: Automatic test timeouts prevent hanging

### Code Quality
- **ruff**: Fast linting and formatting
- **pyright**: Type checking in strict mode
- **uv**: Modern Python package management

### Commands
```bash
# Testing
scripts/check              # Standard workflow (unit + integration + static)
scripts/check unit         # Unit tests only
scripts/check integration  # Integration tests only  
scripts/check static       # Static analysis only
scripts/check all          # Everything including e2e tests

# Manual quality checks
uv run pyright            # Type checking
uv run ruff format .       # Code formatting
uv run ruff check .        # Linting

# Package management
uv add package-name        # Add runtime dependency
uv add --dev package-name  # Add development dependency
uv sync                    # Install all dependencies
uv sync --dev              # Install with dev dependencies
```

## Configuration Management

The project uses a structured configuration system:

### Static Configuration (`{{cookiecutter.project_class_name}}Config`)
- Immutable dataclass for application settings
- Loaded from environment variables
- Type-safe with validation

### Runtime Options (`RuntimeOptions`)  
- Mutable settings for runtime behavior
- Debug flags, logging levels, etc.
- Separate from static config

### Usage Pattern
```python
# Load configuration
config = {{cookiecutter.project_class_name}}Config.from_env()

# Runtime options
runtime = RuntimeOptions(verbose=True, dry_run=False)

# Dependency injection
service = MyService(config, runtime)
```

## Testing Philosophy

### Three-Tier Architecture

1. **Unit Tests** (`tests/unit/`):
   - **<100ms execution time**
   - **Completely isolated** - no external dependencies
   - **Test business logic** in isolation
   - **Use fakes** instead of mocks for dependencies

2. **Integration Tests** (`tests/integration/`):
   - **<500ms execution time**  
   - **Real filesystem** with temporary directories
   - **Mock external APIs** but use real internal components
   - **Test component interactions**

3. **End-to-End Tests** (`tests/e2e/`):
   - **<30s execution time**
   - **Real CLI scenarios** with subprocess calls
   - **Mock external services** for determinism
   - **Test complete user workflows**

### Test Requirements
- **Test intention comments** - every test must explain what it's testing
- **Given/When/Then structure** for clarity
- **Fakes over mocks** - create lightweight implementations
- **Behavior testing** - focus on outcomes, not implementation details

## Git Workflow

### Branch Naming
- `feature/description` - New features
- `fix/description` - Bug fixes  
- `refactor/description` - Code refactoring
- `docs/description` - Documentation updates
- `test/description` - Test improvements

### Commit Format
Follow conventional commits:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples**:
- `feat(config): add environment variable loading`
- `fix(exceptions): correct error inheritance hierarchy`  
- `test(services): add integration test coverage`

### Pull Request Process
1. **Create PR** on GitHub when ready for review
2. **Complete PR_CHECKLIST.md** - ensure all quality gates pass
3. **Address review comments** - respond to all feedback
4. **Merge when approved** - task complete only when merged

## Issue Tracking

- **Use GitHub Issues** for all task tracking
- **Link PRs to issues** using "Fixes #123" or "Addresses #456"
- **Update issue status** with progress comments
- **Close issues** when work is complete

## Code Standards

All coding standards and conventions are documented in [AGENTS.md](AGENTS.md). Key principles:

- **YAGNI** - Build only what's needed for current features
- **DRY** - Search for existing functionality before implementing new code
- **Type safety** - Comprehensive type annotations, avoid `Any`
- **Exception handling** - Use domain-specific exceptions with context
- **Testing** - Prefer fakes over mocks, test behavior not implementation

## Documentation

- **Docstrings** - Google-style for all public APIs
- **Type annotations** - Comprehensive typing throughout
- **Usage examples** - Include examples in complex function docstrings
- **Keep docs in sync** - Update documentation when changing guidelines

## Getting Help

- **Local testing**: Run `scripts/check` before committing
- **CI failures**: Check GitHub Actions for detailed error messages
- **Code standards**: Refer to [AGENTS.md](AGENTS.md) for comprehensive guidelines
- **Pull request checklist**: Use [PR_CHECKLIST.md](PR_CHECKLIST.md) before submitting

## Performance Guidelines

- **Unit tests**: Must complete in <100ms each
- **Integration tests**: Must complete in <500ms each  
- **E2E tests**: Must complete in <30s each
- **Code quality**: All checks must pass before merging

## Security

- **Never commit secrets** - use environment variables
- **Validate inputs** - especially from external sources
- **Handle exceptions** - don't expose internal details in error messages
- **Review dependencies** - get approval before adding new packages