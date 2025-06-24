# Instructions for AI Contributors

This repository welcomes contributions from AI-based tools. When acting as an agent, follow these comprehensive guidelines.

## 🎯 Quick Reference for AI Agents

### Before Writing Any Code
1. **Search existing codebase first**: `grep -r "function_name" src/`
2. **Check common utilities**: config.py, services.py, exceptions.py
3. **Propose libraries if needed**: Use Library Proposal Template below

### Before Opening PR
1. **Complete PR_CHECKLIST.md entirely** - every single item
2. **Run `scripts/check`** - must pass completely
3. **Write test intention comments** - explain what each test validates
4. **Update documentation** for public API changes

### Code Quality Checklist
- [ ] Type annotations on all functions and methods
- [ ] Google-style docstrings on public APIs
- [ ] Tests focus on business logic, not type validation
- [ ] Configuration uses frozen dataclasses
- [ ] Search completed before implementing new functionality

### Common Commands
```bash
# Quality checks
scripts/check                    # Standard workflow (required before PR)
scripts/check unit              # Quick feedback during development
scripts/check static            # Type checking and linting only

# Code formatting
uv run ruff format .            # Format code
uv run ruff check .             # Lint code
uv run pyright                  # Type check
```

## 🚨 CRITICAL REQUIREMENTS (MUST DO)

These are non-negotiable requirements. Failure to follow these will result in PR rejection:

1. **Complete `PR_CHECKLIST.md`** - Every single item must be checked before submitting any PR
2. **Run `scripts/check`** - All quality gates must pass completely 
3. **Search existing code first** - Use `grep -r` to find similar functionality before implementing
4. **Get approval for dependencies** - Propose library options before adding any external dependencies
5. **Use conventional commits** - Follow the format: `type(scope): description`
6. **Never commit secrets** - No API keys, passwords, or generated files

## 📋 STANDARD PRACTICES (SHOULD DO)

Follow these practices for high-quality contributions:

1. **Write tests for changes** - Especially for bug fixes and new features
2. **Update documentation** - Keep docs current with code changes
3. **Use type annotations** - Annotate all functions, methods, and variables
4. **Use `uv run`** - Ensure virtual environment is active for all commands
5. **Add intention comments to tests** - Explain what behavior each test validates
6. **Use Google-style docstrings** - Document all public APIs
7. **Prefer frozen dataclasses** - For configuration and data structures

## 🔀 Decision Trees for Common Workflows

### Should I Add a New Dependency?

```
1. Is this core business logic for the {{cookiecutter.project_slug}} project?
   YES → Implement custom code
   NO  → Continue to step 2

2. Can this be implemented in <10 lines of simple code?
   YES → Implement custom code
   NO  → Continue to step 3

3. Does existing functionality in the codebase solve this?
   YES → Use/extend existing code
   NO  → Continue to step 4

4. Research libraries and create proposal
   → Use Library Proposal Template (see below)
   → Get approval before proceeding
```

### Should I Create New Code or Use Existing?

```
1. Search the codebase first:
   grep -r "function_name" src/
   grep -r "similar_pattern" src/
   
2. Found similar functionality?
   YES → Extend/refactor existing code
   NO  → Continue to step 3

3. Found partial solutions?
   YES → Compose existing functions
   NO  → Create new code following patterns

4. Always check these common locations:
   - src/{{cookiecutter.project_slug}}/config.py (configuration utilities)
   - src/{{cookiecutter.project_slug}}/services.py (service patterns)
   - src/{{cookiecutter.project_slug}}/exceptions.py (error types)
```

### What Should I Test?

```
✅ Test These:
- Business logic and algorithms
- Error handling and edge cases  
- Integration between components
- Configuration behavior changes

❌ Don't Test These:
- Type validation (pyright handles this)
- Framework code (pytest, dataclasses)
- Third-party library behavior
- Simple getters/setters
```

## Project Overview

**Technology Stack:**

- **Python 3.12+**: Primary language
- **uv**: Modern package installer and dependency management
- **pytest**: Testing framework with three-tier architecture (unit/integration/e2e)
- **ruff**: Fast Python linter and formatter
- **pyright**: Type checker for static analysis in strict mode

**Key Commands:**

- Install dependencies: `uv sync --dev`
- Run all checks: `scripts/check`
- Run specific tests: `scripts/check unit`, `scripts/check static`, `scripts/check all`
- Type check: `uv run pyright`
- Format code: `uv run ruff format .`
- Lint code: `uv run ruff check .`

## Code Quality Expectations

### Design Principles

**Follow YAGNI (You Aren't Gonna Need It):**

- Build only what's required for current features
- Avoid premature abstraction and over-engineering
- Start with the simplest solution that works
- Add complexity only when requirements demand it
- Don't create frameworks for single-use features

**Follow DRY (Don't Repeat Yourself) - MANDATORY SEARCH PROCESS:**

**Before implementing ANY new functionality, you MUST:**

1. **Search the entire codebase** for similar functionality:

   - Use keyword searches for function names, parameter types, patterns
   - Look for `validate_*`, `process_*`, `handle_*`, `create_*` functions
   - Search for similar parameter types (`timeout: int`, `config: {{cookiecutter.project_class_name}}Config`)
   - Check for existing error handling patterns

2. **Review existing modules** that might solve the problem:

   - Check `config.py`, `services.py`, `exceptions.py` for related functionality
   - Look at imports in similar files to find utility functions
   - Review test files to understand existing behavior patterns

3. **Only create new code if nothing similar exists**:
   - If you find similar code, extend/refactor it instead
   - If you find partial solutions, compose them rather than rewrite
   - If you find exact duplicates, consolidate into shared utilities

**Example Search Process:**

```bash
# Before creating a new validation function, search for existing ones:
grep -r "def validate" src/
grep -r "ValueError.*positive" src/
grep -r "timeout.*int" src/

# Before creating a new service, check existing patterns:
grep -r "class.*Service" src/
grep -r "__init__.*config.*runtime" src/
```

**When you find existing functionality:**

- **Extend existing functions** with optional parameters if needed
- **Refactor common code** into shared utilities
- **Compose existing functions** rather than duplicating logic
- **Import and reuse** existing implementations

This keeps the codebase small and prevents unnecessary duplication.

**Prefer Third-Party Libraries for Non-Business Logic - MANDATORY PROPOSAL PROCESS:**

**Before implementing any significant infrastructure code, you MUST:**

1. **Research existing libraries** that solve the problem
2. **Find 2-3 alternatives minimum** and compare them
3. **Present a proposal** with pros/cons for each option
4. **Get explicit approval** before adding any dependencies
5. **Only implement custom code** if no suitable library exists

**Library Proposal Process:**

1. Research 2-3 library options
2. Use Library Proposal Template (see Appendix A4)
3. Include pros/cons, maintenance status, license
4. Get approval before proceeding

**Use libraries for:** HTTP requests, data validation, file parsing, cryptography, standard formats
**Write custom code for:** Core business logic, simple utilities (<10 lines), domain-specific integration

**NEVER add dependencies without approval** - always propose first.

### No Legacy or Backward Compatible Code Without Approval

**Don't leave "legacy" or "backward compatible" methods in the code unless explicitly asked to do so.** All code and tests should use the new interfaces and APIs before a refactor is considered complete.

#### What Constitutes Legacy Code

Remove all of the following unless explicitly approved:
- Old method names kept for compatibility
- Deprecated parameters or function signatures
- Old import paths or module aliases
- Wrapper functions that just call new implementations
- Any code marked as "deprecated" or "for backward compatibility"

#### Definition of a Complete Refactor

A refactor is **only complete** when:
1. ✅ All internal code uses the new APIs/interfaces
2. ✅ All tests are updated to test the new implementation
3. ✅ All documentation reflects the new approach
4. ✅ No references to old methods remain (except in migration docs if approved)

#### Examples

*See Appendix A1 for detailed code examples*

#### Refactoring Checklist

When refactoring, ensure:
- [ ] All calling code updated to use new API
- [ ] All tests updated to test new API (not through legacy wrappers)
- [ ] All imports updated to new paths
- [ ] All documentation updated
- [ ] All examples in docstrings updated
- [ ] No "deprecated" markers remain
- [ ] No compatibility shims remain

#### When Exceptions May Be Granted

**Exceptions require explicit user approval.** Valid reasons might include:
- Public APIs with external consumers who need migration time
- Complex system-wide changes requiring phased rollout
- Critical production systems needing gradual migration

#### Requesting an Exception

If you believe legacy code must be kept, request approval:

```
I need to keep a legacy method during this refactor:

Current situation:
- Refactoring `OldClassName.old_method()` to `NewClassName.new_method()`
- Found 47 call sites across 12 modules
- 3 of these are in critical production workflows

Why legacy code might be needed:
- The production workflows run every hour and need careful testing
- Full migration would require coordinated deployment across 3 services
- Gradual migration would reduce risk

Proposed approach:
- Keep old method with deprecation warning for 1 sprint
- Add TODO comment with removal date
- Create tracking issue for complete removal

May I keep the legacy method with clear deprecation marking?
```

#### Important Notes

- **Default is removal**: Always remove legacy code unless told otherwise
- **Update everything**: A partial refactor is not a complete refactor
- **No silent compatibility**: If approved to keep legacy code, it must have clear deprecation warnings

## Git Commit Standards

Follow conventional commit format for consistency:

**Format:**

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**

```
feat(config): add environment variable loading
fix(exceptions): correct error code inheritance
docs(readme): update setup instructions
test(services): add integration test coverage
chore(deps): update development dependencies
```

**Rules:**

- Subject line ≤50 characters
- No capital letter at start of subject
- No period at end of subject
- Use imperative mood ("add" not "added")
- Body lines ≤72 characters
- Blank line between subject and body

## Development Workflow

Follow this structured process for all changes:

### 1. Branch Creation

```bash
# Feature branches
git checkout -b feature/descriptive-name
git checkout -b fix/issue-description
git checkout -b refactor/component-name
git checkout -b docs/topic-name
git checkout -b test/component-name
```

### 2. Development Process

1. **Plan**: Review requirements and create implementation plan
2. **Implement**: Write code following project standards
3. **Test**: Add/update tests for new functionality
4. **Check**: Run `scripts/check` to ensure quality
5. **Commit**: Use conventional commit format
6. **Push**: Push branch to remote repository
7. **Pull Request**: Open PR on GitHub for review
8. **Review**: Address all review comments
9. **Complete**: Task is complete when PR is approved and merged

### 3. Quality Gates

Before pushing any changes:

```bash
scripts/check  # Must pass all tests and quality checks
```

### 4. Pull Request Process

- **MANDATORY: Complete PR checklist**: You MUST complete every single item in `PR_CHECKLIST.md` before submitting any PR
- Open PR with clear description of changes
- Link to relevant GitHub issues
- Ensure CI checks pass
- Address all review comments
- Task is not complete until PR is merged

## Configuration Management

Use immutable configuration objects and dependency injection:

```python
from {{cookiecutter.project_slug}}.config import {{cookiecutter.project_class_name}}Config, RuntimeOptions

# Immutable static configuration
config = {{cookiecutter.project_class_name}}Config.from_env()  # Load from environment
config = config.with_overrides(debug=True)  # Create modified copy

# Mutable runtime options
runtime = RuntimeOptions(verbose=True, dry_run=False)

# Dependency injection - pass config objects, not individual parameters
class MyService:
    def __init__(self, config: {{cookiecutter.project_class_name}}Config, runtime: RuntimeOptions):
        self.config = config
        self.runtime = runtime
```

**✅ Use configuration dataclasses:**

```python
@dataclass(frozen=True)
class ServiceConfig:
    """Configuration for service behavior."""
    timeout: int = 30
    retries: int = 3
    batch_size: int = 100

def test_service_with_config():
    """Test service behavior with custom configuration."""
    # Given: Custom configuration
    config = ServiceConfig(timeout=60, batch_size=50)
    service = MyService(config)

    # When/Then: Service uses configuration values
    assert service.config.timeout == 60
```

**❌ Avoid parameter proliferation:**

```python
# Don't do this - hard to test and maintain
def process_data(data, timeout, retries, batch_size, max_workers, debug):
```

Benefits:

- No parameter proliferation
- Easy testing with mock configs
- Clear separation of static vs runtime settings
- Immutable config prevents accidental modification

### Type Safety Standards

**Use pyright in strict mode with comprehensive type annotations:**

1. **Avoid `Any` type** - use specific types, generics, or unions instead
2. **Minimize `None` returns** - prefer Optional, defaults, or exceptions
3. **Type everything** - functions, methods, variables, class attributes
4. **Use modern typing** - Union, Generic, TypeVar, Protocol

**Type-safe patterns:**

```python
# ✅ Good - specific types, no None returns
from typing import List, Dict, Optional, Union, TypeVar

T = TypeVar('T')

def process_items(items: List[str], config: {{cookiecutter.project_class_name}}Config) -> Dict[str, int]:
    """Process items and return counts."""
    return {item: len(item) for item in items}

def get_first_or_default(items: List[T], default: T) -> T:
    """Get first item or return default - never None."""
    return items[0] if items else default

# ❌ Avoid - Any types and unclear None returns
def process_items(items: Any) -> Any:  # Too vague
    return something

def get_first(items):  # No return type, unclear None behavior
    return items[0] if items else None
```

### Never Ignore Lint or Typing Errors Without Explicit Approval

**CRITICAL**: Agents must NEVER suppress lint or typing errors without explicit user approval. This includes:
- `# type: ignore` comments
- `# pyright: ignore` comments  
- `# noqa` comments for ruff
- Disabling rules in pyproject.toml
- Any other form of error suppression

#### Approval Process

When encountering an error that seems impossible to fix, agents must:

1. **Show the problematic code with context**:
   ```python
   # Show 5-10 lines of surrounding code
   def process_third_party_data(client: SomeClient) -> ProcessedData:
       # This line has a type error:
       result = client.get_data()  # pyright: Unknown return type
       return ProcessedData(result)
   ```

2. **Explain why the ignore is necessary**:
   - "The third-party library 'some-client' doesn't provide type stubs"
   - "Pyright false positive due to complex generic inference"
   - "Temporary workaround for upstream bug (link to issue)"

3. **Document alternative approaches considered**:
   - "Tried creating a Protocol but the API is too dynamic"
   - "Attempted runtime type checking but performance impact too high"
   - "Considered switching libraries but no alternatives exist"

4. **Wait for explicit approval** before adding any ignore directive

#### Exceptional Circumstances Where Approval May Be Granted

- **Third-party library limitations**: Library lacks type annotations and creating comprehensive stubs is impractical
- **Known tool false positives**: Documented pyright/ruff bugs with open issues
- **Temporary workarounds**: Time-sensitive fixes with clear tracking issues for proper resolution
- **Framework quirks**: Well-known patterns in frameworks like Django/FastAPI that confuse type checkers

#### Example Request for Approval

```
I need to add a type ignore for this third-party API call:

```python
from untrusted_analytics import Analyzer  # No type stubs available

class DataProcessor:
    def analyze(self, data: dict[str, Any]) -> AnalysisResult:
        analyzer = Analyzer()
        # Type error: Unknown return type, no stubs for this library
        raw_result = analyzer.process(data)  # <- Need to ignore this
        
        # Our typed wrapper
        return AnalysisResult(
            score=float(raw_result['score']),
            categories=list(raw_result['categories'])
        )
```

Why ignore is necessary:
- The 'untrusted_analytics' package has no type annotations or stubs
- Creating full stubs would require reverse-engineering their entire API
- We only use this one method, so a targeted ignore is more practical

Alternatives considered:
- Searched for typed alternatives - none exist for our use case
- Tried creating a minimal Protocol - their API uses dynamic attributes
- Considered runtime validation - already doing that with our wrapper

May I add `# type: ignore[no-any-return]` to line 6?
```

#### Important Notes

- **Existing ignores**: Leave existing `# type: ignore` comments untouched unless specifically asked to address them
- **PR readiness**: Never submit code with unapproved ignore directives
- **Documentation**: When approval is granted, add a comment explaining why the ignore was necessary

### Wrapping Untyped Third-Party Libraries

When adding third-party libraries that lack type annotations, **always create type-safe wrappers** to insulate first-party code from untyped interfaces.

#### Approach Priority

1. **Prefer Pydantic models** for data structures returned by third-party libraries
2. **Use typed wrapper classes** when Pydantic models aren't suitable (e.g., for stateful objects or complex APIs)
3. **Never expose untyped interfaces** directly to the rest of the codebase

#### Implementation Pattern

```python
# ❌ Bad - Exposing untyped library directly
from some_untyped_lib import Client  # No type annotations

def get_user_data(user_id: str) -> Any:  # Forced to use Any
    client = Client()
    return client.fetch_user(user_id)  # Unknown return type

# ✅ Good - Wrapped with Pydantic models
from pydantic import BaseModel
from some_untyped_lib import Client  # No type annotations

class UserData(BaseModel):
    """Type-safe representation of user data from external API."""
    id: str
    name: str
    email: str
    created_at: datetime
    metadata: dict[str, Any]  # Even nested data gets some typing

class TypedClient:
    """Type-safe wrapper around untyped client library."""
    
    def __init__(self) -> None:
        self._client = Client()  # Hide untyped client as private
    
    def fetch_user(self, user_id: str) -> UserData:
        """Fetch user data with full type safety."""
        raw_data = self._client.fetch_user(user_id)
        return UserData.model_validate(raw_data)  # Validates and types

# Now the rest of the codebase has type safety
def get_user_data(user_id: str) -> UserData:
    client = TypedClient()
    return client.fetch_user(user_id)  # Fully typed!
```

#### Benefits of This Approach

- **Type safety throughout the codebase** - No `Any` types leak beyond the wrapper
- **Runtime validation** - Pydantic validates data structure at runtime
- **Clear interface boundaries** - Easy to see what external data looks like
- **Easier testing** - Can mock typed interfaces more easily
- **Documentation** - Pydantic models serve as clear documentation

#### When to Use Wrapper Classes

Use typed wrapper classes instead of (or in addition to) Pydantic models when:

```python
# For stateful objects or complex APIs
class TypedDatabaseConnection:
    """Type-safe wrapper around untyped database library."""
    
    def __init__(self, connection_string: str) -> None:
        self._conn = untypeddb.connect(connection_string)
    
    def query(self, sql: str, params: list[Any]) -> list[dict[str, Any]]:
        """Execute query with typed return value."""
        return self._conn.execute(sql, params).fetchall()
    
    def transaction(self) -> ContextManager[None]:
        """Typed context manager for transactions."""
        return self._conn.transaction()
```

#### Important Notes

- **Existing code**: Leave existing untyped library usage alone unless specifically asked to refactor
- **Minimal wrapping**: Only wrap the parts of the library you actually use
- **Type specificity**: Be as specific as possible with types, avoid `Any` where you can

### Documentation Requirements

**ALWAYS provide comprehensive documentation:**

1. **Google-style docstrings** on all public functions, methods, and classes:

   ```python
   def process_data(items: List[str], config: {{cookiecutter.project_class_name}}Config) -> Dict[str, Any]:
       """Process a list of items according to configuration.

       This function takes raw string items and processes them according
       to the settings defined in the configuration object.

       Args:
           items: List of string items to process
           config: Configuration object containing processing settings

       Returns:
           Dictionary containing processed results with keys:
           - 'count': Number of items processed
           - 'results': List of processed items

       Raises:
           ValueError: If items list contains invalid data

       Example:
           >>> config = {{cookiecutter.project_class_name}}Config(debug=True)
           >>> result = process_data(['a', 'b'], config)
           >>> result['count']
           2
       """
   ```

2. **Type annotations everywhere**:

   ```python
   # Good
   def calculate_score(data: Dict[str, int], threshold: float = 0.5) -> Optional[float]:

   # Bad
   def calculate_score(data, threshold=0.5):
   ```

3. **Usage examples in docstrings** for complex functions

### 🧪 Comprehensive Testing Guide

**CRITICAL: All tests must pass before opening any PR. No exceptions.**

#### Three-Tier Testing Architecture

1. **Unit Tests** (`tests/unit/`) - <100ms each
   - Business logic in complete isolation
   - No filesystem, network, or external dependencies
   - Use dependency injection with config objects

2. **Integration Tests** (`tests/integration/`) - <500ms each  
   - Component workflows with real filesystem
   - Mock external APIs only
   - Test integration points between components

3. **E2E Tests** (`tests/e2e/`) - <30s each
   - Full application scenarios
   - Mock external services for cost control
   - Test complete user workflows

#### What to Test vs. What NOT to Test

```
✅ DO Test:
- Business logic and algorithms
- Error handling and edge cases
- Component integration behavior
- Configuration effects on behavior

❌ DON'T Test:
- Type validation (pyright handles this)
- Framework behavior (pytest, dataclasses)  
- Third-party library functionality
- Simple getters/setters or property access
```

#### Required Test Structure

```python
def test_service_handles_empty_input():
    """Service returns empty results when input is empty."""
    # Given: A configured service
    config = {{cookiecutter.project_class_name}}Config(debug=True)
    service = MyService(config)
    
    # When: Processing empty input
    result = service.process([])
    
    # Then: Returns empty list without error
    assert result == []
```

#### Test Execution Workflow

**During Development:**
```bash
scripts/check unit         # Quick feedback while coding
scripts/check static       # Check types and linting
scripts/check              # Standard workflow
```

**Before PR (MANDATORY):**
1. Run `scripts/check` - must pass completely
2. Fix ALL failures - tests, lint, type errors
3. No temporary skips without approval
4. Verify CI compatibility

#### Fakes vs Mocks - Prefer Fakes

**✅ Use simple fake implementations:**
```python
class FakeDataStore:
    """Simple in-memory fake for testing."""
    def __init__(self):
        self._data = {}
    
    def get(self, key: str) -> str | None:
        return self._data.get(key)
    
    def set(self, key: str, value: str) -> None:
        self._data[key] = value

def test_service_behavior():
    """Test service stores and retrieves data correctly."""
    # Given: Service with fake dependencies
    fake_store = FakeDataStore()
    service = DataService(fake_store)
    
    # When: Using the service
    service.store_data("key", "value")
    result = service.get_data("key")
    
    # Then: Behavior works as expected
    assert result == "value"
```

**❌ Avoid heavy mocking:**
- Don't use `@patch` decorators - makes tests fragile
- Don't test method calls - test behavior outcomes
- Don't mock what you own - use dependency injection

#### Key Testing Principles
- **Trust strict typing** – don't test what pyright already validates
- **Focus on business logic** – don't test framework code or third-party libraries
- **Quality over quantity** – write fewer, more meaningful tests

✅ Summary: Write fewer, well-named tests that validate behavior, not types or implementation details. Treat tests as documentation for business rules.

### Exception Handling Standards

**Create domain-specific exceptions** when they add semantic value, **use built-in exceptions** for simple validation (e.g., `ValueError` for basic input checks).

**Guidelines for custom exceptions:**

- Create custom exceptions when you need error codes, context, or domain-specific handling
- Use descriptive names that indicate the type of error (e.g., `InvalidConfigurationError`, `DataProcessingError`)
- Include relevant context and error codes when helpful for debugging or handling

**Catch exceptions narrowly** - only catch specific exceptions you expect and can recover from.

**✅ Proper exception testing:**

```python
def test_invalid_config_raises_proper_error():
    """Test that invalid configuration raises appropriate error."""
    # When: Creating config with invalid timeout
    with pytest.raises(ValueError) as exc_info:
        validate_timeout(-1)

    # Then: Should raise with clear error message
    error = exc_info.value
    assert "Timeout must be positive" in str(error)
```

**✅ Narrow exception catching:**

```python
def load_data(path: str) -> str:
    """Load data with expected error handling."""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        # Expected - file might not exist
        return ""
    except PermissionError as e:
        # Expected - might not have access
        raise ValueError(f"Cannot access file: {path}") from e
    # Let other exceptions (OSError, etc.) propagate

# ❌ Avoid broad catching
try:
    result = process_data(data)
except Exception:  # Too broad - hides bugs
    return None
```

**✅ Use appropriate exceptions:**

```python
# Use built-in exceptions for simple validation
def validate_positive(value: int) -> None:
    if value <= 0:
        raise ValueError("Value must be positive")

# Create custom exceptions when you need context/error codes
class InvalidUserDataError(ValueError):
    def __init__(self, message: str, field: str, value: Any):
        super().__init__(message)
        self.field = field
        self.value = value
```

### Configuration Management

**✅ Use configuration dataclasses:**

```python
@dataclass(frozen=True)
class ServiceConfig:
    """Configuration for service behavior."""
    timeout: int = 30
    retries: int = 3
    batch_size: int = 100

def test_service_with_config():
    """Test service behavior with custom configuration."""
    # Given: Custom configuration
    config = ServiceConfig(timeout=60, batch_size=50)
    service = MyService(config)

    # When/Then: Service uses configuration values
    assert service.config.timeout == 60
```

**❌ Avoid parameter proliferation:**

```python
# Don't do this - hard to test and maintain
def process_data(data, timeout, retries, batch_size, max_workers, debug):
```

## Architecture Patterns

### Protocol-Based Interfaces

Prefer Python protocols over abstract base classes for flexibility:

```python
from typing import Protocol

class DataProcessor(Protocol):
    def process(self, data: str) -> str: ...
    def is_ready(self) -> bool: ...

# Any class with these methods automatically satisfies the protocol
# No inheritance required - enables duck typing and easier testing
```

**Benefits:**

- No inheritance required - any compatible class works
- Easier testing with mock objects
- Better for dependency injection
- More flexible than ABC inheritance
- Third-party classes can satisfy protocols naturally

**Use protocols for:**

- Service interfaces
- Plugin systems
- Dependency injection contracts
- Testing boundaries

### Async-First Design

Design for async by default, provide sync compatibility:

```python
# Async-first interface
class AsyncDataProcessor(Protocol):
    async def process(self, data: str) -> str: ...
    async def is_ready(self) -> bool: ...

# Provide sync wrapper when needed
class SyncDataProcessor:
    def __init__(self, async_processor: AsyncDataProcessor):
        self.async_processor = async_processor

    def process(self, data: str) -> str:
        return asyncio.run(self.async_processor.process(data))
```

**Guidelines:**

- Core services should be async by default
- Provide sync wrappers for CLI/compatibility
- Use `asyncio` for I/O operations
- Batch operations for efficiency
- Consider backpressure and rate limiting

**Benefits:**

- Better performance for I/O-bound operations
- Natural concurrency support
- Future-proof architecture
- Easier to add sync wrapper than retrofit async

## Code Organization Guidelines

Follow these standards for structuring and organizing Python code for clarity, maintainability, and testability.

### Project Directory Layout

Use the **src layout** for all projects:

```
{{cookiecutter.project_slug}}/
├── src/
│   └── {{cookiecutter.project_slug}}/
│       ├── __init__.py         # Public API re-exports (avoid logic)
│       ├── __main__.py         # CLI entry point
│       ├── config.py           # Configuration classes
│       ├── exceptions.py       # Custom exception classes
│       ├── services.py         # Business logic entry points
│       ├── utils/              # Domain-specific utilities
│       │   ├── __init__.py
│       │   ├── date_utils.py
│       │   └── string_utils.py
│       ├── repositories.py     # Data access abstractions
│       └── models/             # Domain/data classes
│           ├── __init__.py
│           └── user.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── fakes/                  # Reusable test doubles
│       ├── fake_repository.py
│       └── fake_email_client.py
├── scripts/
│   └── check
├── pyproject.toml
└── README.md
```

### Module-Level Guidelines

**When to create a new module (file):**

- ✅ Existing file exceeds **250–300 lines**
- ✅ Class or functions represent a **distinct responsibility**
- ✅ Code is reused across multiple components

**When to create a submodule (folder):**

- ✅ You have ≥ 3 closely related modules
- ✅ Need to group files by domain or feature
- ✅ Need to isolate functionality for testing or versioning

### File Organization Conventions

| Filename          | Contains                                                       |
| ----------------- | -------------------------------------------------------------- |
| `__init__.py`     | Public API re-exports (avoid logic)                            |
| `models.py`       | Domain/data classes (split when large)                         |
| `services.py`     | Business logic entry points                                    |
| `utils/`          | Domain-specific utilities (`date_utils.py`, `string_utils.py`) |
| `repositories.py` | Data access abstractions                                       |
| `exceptions.py`   | Custom exception classes                                       |
| `__main__.py`     | CLI entry points                                               |

### Test Support Structure

**Rules:**

- ✅ Co-locate **unit tests** in `tests/`
- ✅ Use `fakes/`, `fixtures/`, or `test_support/` folders for reusable test doubles
- ❌ Do not place fakes or mocks in production code paths

### Method and Function Guidelines

**✅ Keep functions small and focused:**

- Prefer 5–15 lines per method
- Each function should do **one thing only**
- If a function has **multiple logical steps**, extract sub-functions:

```python
def process_user_signup(user_data: Dict[str, Any]) -> User:
    """Process user registration with validation and welcome email."""
    validate_user_data(user_data)
    user = create_user_account(user_data)
    send_welcome_email(user)
    return user

def validate_user_data(user_data: Dict[str, Any]) -> None:
    """Validate user registration data."""
    if not user_data.get('email'):
        raise ValueError("Email is required")
    # Additional validation logic

def create_user_account(user_data: Dict[str, Any]) -> User:
    """Create user account in database."""
    return User.create(user_data)

def send_welcome_email(user: User) -> None:
    """Send welcome email to new user."""
    # Email sending logic
```

**✅ Use descriptive names:**

- Names should describe **intent**, not mechanics:

```python
# ✅ Good - describes intent
def normalize_url(url: str) -> str: ...
def save_user_to_database(user: User) -> None: ...

# ❌ Avoid - describes mechanics
def strip_and_lower(url: str) -> str: ...
def db_insert(user: User) -> None: ...
```

**❌ Avoid deeply nested logic:**

- Extract conditional branches to named helpers
- Use guard clauses instead of nesting if/else:

```python
# ✅ Good - guard clauses and helper functions
def process_payment(payment_data: PaymentData) -> PaymentResult:
    """Process payment with validation and fraud checks."""
    if not payment_data.is_valid():
        return PaymentResult.error("Invalid payment data")

    if is_suspicious_transaction(payment_data):
        return PaymentResult.error("Transaction flagged for review")

    return charge_payment(payment_data)

# ❌ Avoid - deeply nested
def process_payment(payment_data: PaymentData) -> PaymentResult:
    if payment_data.is_valid():
        if not is_suspicious_transaction(payment_data):
            result = charge_payment(payment_data)
            if result.success:
                return result
            else:
                return PaymentResult.error("Charge failed")
        else:
            return PaymentResult.error("Transaction flagged")
    else:
        return PaymentResult.error("Invalid data")
```

### Design Patterns to Encourage

| Pattern            | Use Case                          | Example                |
| ------------------ | --------------------------------- | ---------------------- |
| Factory pattern    | Decouple instantiation logic      | `UserFactory.create()` |
| Adapter pattern    | Normalize inconsistent interfaces | `DatabaseAdapter`      |
| Command pattern    | Encapsulate user actions or tasks | `ProcessOrderCommand`  |
| Strategy pattern   | Plug different behaviors          | `RankingStrategy`      |
| Repository pattern | Abstract database or storage APIs | `UserRepository`       |

### Clean Imports and Reusability

**✅ Use absolute imports from project root:**

```python
from {{cookiecutter.project_slug}}.utils.string_utils import slugify
from {{cookiecutter.project_slug}}.services.user_service import UserService
from {{cookiecutter.project_slug}}.models.user import User
```

**✅ Re-export clean interfaces in `__init__.py` if needed:**

```python
# src/{{cookiecutter.project_slug}}/__init__.py
from .services import UserService, OrderService
from .models import User, Order
from .exceptions import {{cookiecutter.project_class_name}}Error, ConfigurationError

__all__ = ['UserService', 'OrderService', 'User', 'Order', '{{cookiecutter.project_class_name}}Error', 'ConfigurationError']
```

**❌ Avoid:**

- Wildcard imports (`from x import *`)
- Logic inside `__init__.py` files
- Relative imports in production code

### Code Organization Summary

| Guideline             | Recommendation                               |
| --------------------- | -------------------------------------------- |
| **Class structure**   | One file per "core" class; avoid clutter     |
| **File size**         | Refactor when > 300 lines                    |
| **Method size**       | Prefer < 15 lines; break into helpers        |
| **Import hygiene**    | Use absolute imports, no `*`                 |
| **Logic grouping**    | Use submodules when domains emerge           |
| **Test organization** | Keep production and test-only code separated |
| **Documentation**     | Use docstrings for public APIs and key logic |

## Significant Task Implementation Process

For **complex, multi-step changes** (simple changes don't need this process), follow this structured approach:

### 1. Create TODO.md Planning Document

For significant changes, create a `TODO.md` file with:

**Required Sections:** Title, Goal, High-Level Plan, API Changes, Testing Plan, Implementation Steps

*See Appendix A4 for complete TODO.md template*

### 2. Seek User Approval and Check In Plan

**For interactive sessions:**
- Share the complete TODO.md plan with the user
- **Get explicit approval** before starting implementation
- Do not begin work until the plan is approved

**After approval:**
- **Check in TODO.md as the first commit** of the topic branch
- This provides a clear record of the planned work
- Makes the plan visible to reviewers and team members

### 3. Implementation Rules

**Once approved:**
- ✅ **Follow the plan exactly** - do not change without approval
- ✅ **Check off steps** as you complete them
- ✅ **Add implementation steps** if needed (but don't change the overall plan)
- ❌ **Never modify** the goal, API changes, or testing plan without approval

### 4. Handle Deviations

**If you discover needed changes during implementation:**

1. **Stop implementation** immediately
2. **Record in "Deviations" section** of TODO.md:
   ```markdown
   ## Deviations
   ### Deviation 1: [Brief description]
   **Reason**: Why this change is needed
   **Impact**: What this affects (APIs, testing, etc.)
   **Proposed Solution**: How to address it
   ```
3. **Present to user** with justification
4. **Get explicit approval** before implementing the deviation
5. **Update relevant sections** of TODO.md after approval

### 5. Completion Verification

**When all tasks are finished:**
- [ ] All implementation steps checked off
- [ ] All deviations properly documented and approved
- [ ] Code matches original design (plus approved deviations)
- [ ] Testing plan executed successfully
- [ ] Documentation updated as planned
- [ ] **Delete TODO.md as the final step** before creating the PR
- [ ] TODO.md should be removed in the last commit of the topic branch

### 6. Always Include

**Every plan must include sections for:**
- ✅ **Testing strategy** - how to verify the change works
- ✅ **Documentation updates** - what docs need to be updated
- ✅ **API considerations** - impact on public interfaces
- ✅ **Migration strategy** - if breaking changes are involved

**This process applies to:**
- ✅ New feature implementation
- ✅ Significant refactoring
- ✅ Architecture changes
- ✅ Breaking API changes
- ❌ Simple bug fixes (unless they require design changes)
- ❌ Documentation-only updates
- ❌ Trivial code changes

## Working with GitHub Issues

The project uses GitHub issues for task tracking:

1. **Link commits to issues**: Include issue numbers in commit messages when relevant
2. **Reference issues in PRs**: Use "Fixes #123" or "Addresses #456" in PR descriptions
3. **Update issue status**: Comment on progress and close issues when complete

## Security Guidelines

- **Never use MD5. Always use sha256 instead**
- **Never commit secrets or keys to the repository**
- **Never expose or log secrets and keys in code**
- **Follow security best practices for authentication and data handling**

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

## Detailed Command Examples

### Quality Check Commands
```bash
# Install dependencies
uv sync --dev

# Run standard workflow (unit + integration + static)
scripts/check

# Run specific test categories
scripts/check unit         # Unit tests only
scripts/check static       # Static analysis only
scripts/check integration  # Integration tests only
scripts/check e2e          # E2E tests only
scripts/check all          # Everything including e2e tests

# Run static analysis except specific tools
scripts/check static not ruff       # Static except ruff
scripts/check unit integration      # Unit OR integration tests

# Pass pytest flags through
scripts/check unit -x               # Stop on first failure
scripts/check all -v --tb=short     # Verbose with short traceback

# Manual tools
uv run pytest             # Run tests directly
uv run ruff check .        # Lint code
uv run ruff format .       # Format code
uv run pyright            # Type check
uv run python -m {{cookiecutter.project_slug}}     # Run application
```

### Configuration Examples
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

---

# 📚 APPENDIX: Detailed Examples and Reference Material

*This section contains comprehensive examples and detailed guidance for complex scenarios. Refer to these when you need detailed implementation patterns.*

## A1. Comprehensive Code Examples

### Legacy Code Refactoring Examples

```python
# ❌ Bad - Leaving legacy methods after refactoring
class DataProcessor:
    def process_data(self, items: list[str]) -> dict[str, Any]:
        """New implementation."""
        return self._process_items_v2(items)
    
    def process_items(self, items: list[str]) -> dict[str, Any]:
        """DEPRECATED: Use process_data instead."""
        # Don't leave this here!
        return self.process_data(items)
    
    @deprecated("Use process_data")
    def processItems(self, items):  # Old camelCase name
        # Don't leave this here either!
        return self.process_data(items)

# ✅ Good - Clean refactor with no legacy code
class DataProcessor:
    def process_data(self, items: list[str]) -> dict[str, Any]:
        """Process items and return results."""
        return self._process_items_v2(items)
    # That's it - no legacy methods!
```

## A2. Extended Configuration Patterns

### Advanced Configuration Examples

```python
@dataclass(frozen=True)
class ServiceConfig:
    """Configuration for service behavior."""
    timeout: int = 30
    retries: int = 3
    batch_size: int = 100
    api_key: str = field(repr=False)  # Hide secrets from repr
    
    def with_overrides(self, **kwargs) -> "ServiceConfig":
        """Create new config with overrides."""
        return replace(self, **kwargs)

# Usage patterns
config = ServiceConfig.from_env()
test_config = config.with_overrides(timeout=5, retries=1)
```

## A3. Advanced Testing Scenarios

### Complex Test Examples

```python
def test_service_with_multiple_dependencies():
    """Service integrates correctly with multiple components."""
    # Given: Complex service setup
    fake_db = FakeDatabase()
    fake_cache = FakeCache()
    config = ServiceConfig(timeout=30)
    service = ComplexService(fake_db, fake_cache, config)
    
    # When: Performing complex operation
    result = service.process_with_caching("test_data")
    
    # Then: All components work together
    assert result.status == "success"
    assert fake_cache.was_accessed()
    assert fake_db.was_queried()
```

## A4. Complete Project Templates

### Library Proposal Template

```markdown
## Library Proposal: [Feature/Functionality]

**Problem**: [What you're trying to solve]

**Options Considered**:

### Option 1: [Library Name]
- **Pros**: [Benefits, features, community size]
- **Cons**: [Limitations, size, dependencies]
- **Maintenance**: [Last update, stars, contributors]
- **License**: [License type]

### Option 2: [Library Name]
- **Pros**: [Benefits, features, community size]
- **Cons**: [Limitations, size, dependencies]
- **Maintenance**: [Last update, stars, contributors]
- **License**: [License type]

### Option 3: Custom Implementation
- **Pros**: [No dependencies, exact fit, control]
- **Cons**: [Maintenance burden, testing, edge cases]

**Recommendation**: [Your choice with reasoning]
**Impact**: [Size, performance, maintenance implications]
```

### TODO.md Template

```markdown
# [Change Title]

**Related Issue**: #123 - Issue description

## Goal
Brief description of what this change accomplishes.

## High-Level Plan
Overall approach and strategy.

## Public API Changes
- New functions/classes to be added
- Existing APIs to be modified
- Breaking changes (if any)

## Testing Plan
- Unit tests to be added/modified
- Integration tests needed
- Manual testing steps

## Implementation Steps
- [ ] Step 1: Specific task
- [ ] Step 2: Another specific task
- [ ] Step 3: Documentation updates
- [ ] Step 4: Test implementation

## Deviations
(Added during implementation if needed)
```