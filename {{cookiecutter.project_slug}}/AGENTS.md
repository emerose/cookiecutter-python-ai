# Instructions for AI Contributors

This repository welcomes contributions from AI-based tools. When acting as an agent, follow these comprehensive guidelines.

## 🚨 CRITICAL REQUIREMENT

**Before submitting ANY pull request, you MUST complete every item in `PR_CHECKLIST.md`. This is mandatory and non-negotiable. No exceptions.**

## Core Standards

1. **MANDATORY: Complete `PR_CHECKLIST.md`** - You MUST complete every single item in the checklist before submitting any PR. This is not optional.
2. **Run `scripts/check`** after making changes - all quality gates must pass.
3. **Keep commits atomic** and use the conventional commit format specified below.
4. **Do not introduce external dependencies** without approval - always propose library options first.
5. **Write tests for your changes** whenever feasible, especially for bug or regression fixes.
6. **Update documentation** before completing a task.
7. **Never commit secrets or generated files.**
8. **Use `uv run`** to ensure the project's virtual environment is active when running scripts or commands.
9. **Use `-v --tb=short`** with `scripts/check` to see detailed logs when debugging failing checks.

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

**Library Proposal Template:**

```
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

**Use libraries for:**

- HTTP requests, data validation, file parsing, date/time handling
- CLI frameworks, async utilities, cryptography
- Any complex functionality with many edge cases
- Standard formats (JSON, XML, CSV, etc.)

**Write custom code for:**

- Core business logic specific to {{cookiecutter.project_slug}}'s domain
- Simple utilities (1-3 lines of code)
- Integration/glue code between libraries
- Performance-critical paths needing optimization

**NEVER add dependencies without approval** - always propose first.

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

### Testing Requirements

**ALWAYS follow the three-tier testing architecture:**

#### General Rules

- **Test only business logic, not implementation details**
- **Don't test what type checking already covers** (rely on strict typing)
- **Never test third-party code** – only test your business logic
- **Fewer meaningful tests > many duplicative tests**
- **Behavior-driven tests are preferred**: focus on observable outcomes, not mechanics.

1. **Unit Tests** (`tests/unit/`):

   - Use dependency injection with configuration objects
   - Test business logic in isolation (<100ms per test)
   - No external dependencies, filesystem, or network calls
   - Include test intention comments

2. **Integration Tests** (`tests/integration/`):

   - Test component workflows with real filesystem + mocked external APIs
   - Total execution time <500ms per test
   - Test integration points, not individual components
   - Include test intention comments explaining the integration being tested

3. **E2E Tests** (`tests/e2e/`):
   - Real application scenarios with subprocess calls
   - Mock external services for cost control and deterministic results
   - Include test intention comments explaining the end-to-end scenario

### Test Naming and Structure

- Use descriptive test names in `snake_case`, describing the scenario and expectation.
- Each test should start with a docstring stating the **business behavior** it verifies.
- Prefer `Given/When/Then` structure in comments to guide test readability.

Example:

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

### Testing Philosophy

**Core Testing Principles:**

1. **Leverage Strict Typing** - Don't test what pyright already validates:

   - ❌ Don't test that functions accept correct parameter types
   - ❌ Don't test that functions return declared types
   - ❌ Don't test basic type validation that pyright catches
   - ✅ Do test business logic and behavior

2. **Test Business Logic, Not Implementation:**

   - ❌ Don't test internal method calls or implementation details
   - ❌ Don't test framework code, library code, or language features
   - ❌ Don't test getters/setters or simple property access
   - ✅ Do test algorithms, business rules, and domain logic

3. **Never Test Third-Party Code:**

   - ❌ Don't test that libraries work as documented
   - ❌ Don't test framework behavior (e.g., pytest, dataclasses)
   - ❌ Don't test standard library functions
   - ✅ Do test your code's interaction with libraries (integration tests)

4. **Quality Over Quantity:**
   - ❌ Avoid tests that duplicate type checking or obvious behavior
   - ❌ Avoid tests that just exercise code without asserting meaningful outcomes
   - ✅ Write fewer, focused tests that validate important business behavior
   - ✅ Each test should reflect a real-world expectation and fail only when behavior is incorrect

**Example of what NOT to test:**

```python
# ❌ Don't test this - type checking already validates it
def test_config_accepts_string_app_name():
    config = {{cookiecutter.project_class_name}}Config(app_name="test")  # pyright validates this
    assert config.app_name == "test"      # trivial assertion

# ❌ Don't test this - tests framework code
def test_dataclass_frozen():
    config = {{cookiecutter.project_class_name}}Config()
    with pytest.raises(AttributeError):
        config.app_name = "new"  # tests dataclass frozen behavior

# ✅ DO test this - business logic
def test_config_debug_flag_controls_logging_behavior():
    """Test that debug flag actually changes application behavior."""
    config = {{cookiecutter.project_class_name}}Config(debug=True)
    logger = create_logger(config)

    # Test actual business behavior, not just property access
    assert logger.level == logging.DEBUG
```

**Prefer fakes over mocks for better, more maintainable tests:**

**Note:** Excessive use of mocks leads to fragile tests and hides business logic. Use fakes where possible.

**✅ Use fakes and lightweight implementations:**

```python
class FakeDataStore:
    """Simple in-memory fake for testing."""
    def __init__(self):
        self._data = {}

    def get(self, key: str) -> Optional[str]:
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

**❌ Avoid heavy mocking with patches:**

```python
    # Don't do this - brittle and focused on implementation
    @patch('service.DataStore')
    @patch('service.Logger')
    def test_with_mocks(mock_logger, mock_store):
        mock_store.get.return_value = "value"
        service = DataService(mock_store, mock_logger)
        result = service.get_data("key")
        # Fragile - tests implementation, not behavior
        mock_store.get.assert_called_once_with("key")
```

**Guidelines:**

- **Create simple fake classes** that implement the same interface
- **Use dependency injection** to enable easy fake substitution
- **Test behavior, not implementation** – avoid asserting on method calls
- **Avoid `@patch` decorators** – they make tests fragile and slow
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

Before implementing any significant change, create a `TODO.md` file in the repository root containing:

**Required Sections:**
- **Title**: Clear name for the current change
- **Related Issue**: GitHub issue name and number (if any)
- **Goal**: Concise description of what you're trying to achieve
- **High-Level Plan**: Overall approach to accomplish the goal
- **Public API Changes**: Summary of intended API modifications
- **Testing Plan**: Strategy to ensure the change works correctly
- **Implementation Steps**: Detailed, checkable steps to complete the work

**Template:**
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
