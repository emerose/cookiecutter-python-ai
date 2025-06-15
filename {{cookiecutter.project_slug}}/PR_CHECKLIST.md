# Pull Request Checklist

Use this checklist before submitting any PR to ensure code quality and consistency.

**For detailed coding standards, design principles, and testing guidelines, see [AGENTS.md](AGENTS.md).**

## Code Quality

### ✅ Design Principles (see [AGENTS.md](AGENTS.md))
- [ ] **YAGNI**: Only implemented what's required for current features
- [ ] **DRY**: Searched codebase thoroughly for existing similar functionality
- [ ] **Library Research**: For significant non-business logic, researched third-party libraries and got approval for any new dependencies

### ✅ Type Safety (see [AGENTS.md](AGENTS.md))
- [ ] **Strict typing**: All functions, methods, and variables have type annotations
- [ ] **No `Any` types**: Used specific types, generics, or unions instead of `Any`
- [ ] **Minimal `None` returns**: Used Optional, defaults, or exceptions instead of returning `None` where practical
- [ ] **Pyright passes**: No type checking errors in strict mode

### ✅ Exception Handling (see [AGENTS.md](AGENTS.md))
- [ ] **Domain-specific exceptions**: Used custom exceptions from `{{cookiecutter.project_slug}}.exceptions` when they add semantic value
- [ ] **Built-in exceptions**: Used `ValueError`, etc. for simple validation where appropriate
- [ ] **Error context**: Included error codes and context in custom exceptions
- [ ] **Narrow exception catching**: Only caught specific exceptions that are expected and can be recovered from
- [ ] **Let bugs propagate**: Avoided broad `except Exception:` or bare `except:` that hide unexpected errors

### ✅ Configuration & Dependencies (see [AGENTS.md](AGENTS.md))
- [ ] **Dependency injection**: Used `{{cookiecutter.project_class_name}}Config` and `RuntimeOptions` instead of parameter proliferation
- [ ] **Immutable config**: Configuration objects are frozen/immutable
- [ ] **No new dependencies**: No external dependencies added without approval process

## Documentation

### ✅ Code Documentation (see [AGENTS.md](AGENTS.md))
- [ ] **Google-style docstrings**: All public functions, methods, and classes documented
- [ ] **Type annotations**: Comprehensive typing throughout
- [ ] **Usage examples**: Complex functions include docstring examples
- [ ] **Updated documentation**: Documentation files updated if guidelines changed

## Testing

### ✅ Test Coverage (see [AGENTS.md](AGENTS.md))
- [ ] **Tests written**: All new functionality has corresponding tests
- [ ] **Test intention comments**: Every test includes clear English description of what it tests
- [ ] **Three-tier architecture**: Tests placed in correct directory (unit/integration/e2e)
- [ ] **Performance requirements**: Unit tests <100ms, integration tests <500ms, e2e tests <30s

### ✅ Test Quality (see [AGENTS.md](AGENTS.md))
- [ ] **Business logic focus**: Only tested business logic, not implementation details or framework code
- [ ] **Leverage strict typing**: Didn't test what pyright already validates (types, parameter validation)
- [ ] **No third-party testing**: Didn't test library code, only our business logic interactions
- [ ] **Quality over quantity**: Wrote fewer, meaningful tests rather than duplicative ones
- [ ] **Fakes over mocks**: Used lightweight fake implementations instead of `@patch` decorators
- [ ] **Test behavior, not implementation**: Avoided assertions on method calls, focused on outcomes
- [ ] **Test isolation**: Unit tests have no external dependencies (filesystem, network, APIs)

## Code Standards

### ✅ Quality Checks
- [ ] **`scripts/check` passes**: All static analysis, linting, and tests pass
- [ ] **Ruff formatting**: Code properly formatted
- [ ] **Ruff linting**: No linting errors
- [ ] **Pyright strict**: No type checking errors
- [ ] **Test coverage**: All new code covered by tests

### ✅ Git Standards
- [ ] **Conventional commits**: All commits follow `<type>(<scope>): <subject>` format
- [ ] **Atomic commits**: Each commit represents one logical change
- [ ] **Commit messages**: Clear, imperative mood, under 50 characters for subject
- [ ] **Branch naming**: Follows convention (`feature/`, `fix/`, `refactor/`, `docs/`, `test/`)

## Pull Request

### ✅ PR Description
- [ ] **Clear description**: Explains what changes were made and why
- [ ] **Linked issues**: References relevant GitHub issues
- [ ] **Breaking changes**: Any breaking changes clearly documented
- [ ] **Testing notes**: Explains how to test the changes

### ✅ CI/CD
- [ ] **GitHub Actions pass**: All CI checks are green
- [ ] **No conflicts**: Branch is up-to-date with main and has no merge conflicts
- [ ] **Reviewable size**: PR is focused and not too large to review effectively

## Final Verification

### ✅ Manual Testing
- [ ] **Local testing**: Changes tested locally in realistic scenarios
- [ ] **Edge cases**: Considered and tested error conditions and edge cases
- [ ] **Integration**: Verified changes work with existing functionality

### ✅ Documentation Sync (see [AGENTS.md](AGENTS.md))
- [ ] **Contributor docs aligned**: Documentation files reference AGENTS.md consistently
- [ ] **Comments accurate**: Code comments reflect actual behavior
- [ ] **Examples work**: All code examples in documentation are functional

### ✅ Significant Changes (see [AGENTS.md](AGENTS.md))
- [ ] **TODO.md process followed**: For complex changes, created TODO.md with user approval
- [ ] **All deviations documented**: Any changes from original plan documented and approved
- [ ] **Implementation plan completed**: All steps checked off in TODO.md
- [ ] **Original design verified**: Code matches planned design plus approved deviations

---

## Quick Commands

Before submitting, run these commands and ensure they all pass:

```bash
# Install and sync dependencies
uv sync --dev

# Run all quality checks
scripts/check

# Run specific check categories if needed
scripts/check static    # Static analysis only
scripts/check unit      # Unit tests only
scripts/check all       # Everything including e2e tests

# Manual type checking
uv run pyright

# Manual formatting and linting
uv run ruff format .
uv run ruff check .
```

## Review Process

- [ ] **Self-review**: Reviewed own changes line by line before requesting review
- [ ] **Ready for review**: All checklist items completed
- [ ] **Responsive to feedback**: Will address review comments promptly
- [ ] **Task completion**: Consider task complete only when PR is approved and merged