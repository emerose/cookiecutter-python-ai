# Development Guide - While You Code

This guide covers coding standards, patterns, and practices to follow **while writing code**.

## When to Use This Guide

- Writing new code or modifying existing code
- Setting up your development environment
- Making architectural decisions
- Writing tests alongside code
- Configuring services and dependencies

## Following the TODO.md Plan

**CRITICAL: If a TODO.md file exists, you MUST follow it exactly.**

### TODO.md Workflow During Development

1. **Check for TODO.md** in the project root before starting
2. **Follow the implementation steps** in order
3. **Check off tasks** as you complete them:
   ```markdown
   - [x] Step 1: Write failing tests for user validation
   - [x] Step 2: Implement user validation logic
   - [ ] Step 3: Add integration tests
   ```
4. **Document any deviations** that arise during implementation
5. **Get approval** before implementing significant changes to the plan

### Handling Deviations from Plan

If you discover the plan needs changes:

```markdown
## Deviations

### Deviation 1: Additional validation needed
**Discovered**: Step 2 implementation revealed need for email validation
**Impact**: Adds ~20 lines to validation module
**Proposed**: Add email regex validation before database check
**Approved**: [User approval required]
```

**Never** make significant changes without documenting and getting approval.

## Quick Command Reference

```bash
# Development workflow
uv sync --dev                  # Install dependencies
scripts/check unit             # Quick test feedback
scripts/check static           # Type check and lint (MUST PASS)
scripts/check                  # Full quality check (MUST PASS)

# Run application
uv run python -m {{cookiecutter.project_slug}}

# Fix common issues
uv run ruff format .           # Format code
uv run ruff check --fix .      # Fix lint issues + import order
uv run pyright                 # Type check (fix all errors)

# Manual testing
uv run pytest                  # Run tests directly
```

## Core Design Principles

### YAGNI (You Aren't Gonna Need It)

- Build only what's required for current features
- Avoid premature abstraction
- Start with the simplest solution that works
- Add complexity only when requirements demand it
- **Don't write backwards-compatibility layers unless explicitly requested**
- **Don't support legacy systems unless explicitly requested**

❌ **Don't do this**:
```python
# Over-engineered for a single use case
class AbstractDataProcessorFactory(ABC):
    def create_processor(self, type: ProcessorType) -> DataProcessor:
        ...

# Unnecessary backwards compatibility
def process_data(data, use_legacy=False):
    if use_legacy:
        return legacy_processor(data)  # Don't add unless asked
    return new_processor(data)
```

✅ **Do this**:
```python
# Simple and direct
def process_data(data: dict[str, Any]) -> ProcessedResult:
    # Direct implementation
    return ProcessedResult(...)
```

### DRY (Don't Repeat Yourself)

Always search before implementing:

```bash
# Before creating a validation function
grep -r "def validate" src/
grep -r "ValueError.*positive" src/

# Before creating a service
grep -r "class.*Service" src/
```

## Type Safety Standards

### Static Check Compliance

**CRITICAL: Static check results MUST NOT be ignored unless absolutely necessary.**

**Fix errors immediately when discovered:**
- **Pyright errors** - Fix type issues as soon as they appear
- **Ruff errors** - Address linting issues immediately
- **PLR (refactoring) rules** - Refactor complex code right away
  - PLR0913: Too many arguments → Extract configuration object
  - PLR0915: Too many statements → Break into smaller functions
  - PLR0911: Too many return statements → Simplify logic

```bash
# Check and fix immediately during development
uv run pyright              # Fix any type errors NOW
uv run ruff check .         # Fix any lint errors NOW
uv run ruff check --fix .   # Auto-fix what's possible
```

When you encounter type or lint errors:

1. **Fix the issue immediately** - Don't accumulate technical debt
2. **Refactor if needed** - PLR rules indicate design improvements needed
3. **Document any ignores** - If you must ignore, document it in TODO.md

```markdown
## Deviations

### Static Check Ignore: [file:line]
**Error**: Pyright error about third-party library types
**Reason**: Library lacks type stubs, no alternatives exist  
**Attempted fixes**: Tried Protocol wrapper, investigated stubs
**Approval**: [User approved on date]
```

### Strict Typing Rules

1. **Type everything** - No untyped functions or methods
2. **Avoid `Any`** - Use specific types, unions, or generics
3. **Minimize `None`** - Prefer defaults or exceptions
4. **Use modern typing** - Union, Optional, TypeVar, Protocol

✅ **Good typing**:
```python
from typing import TypeVar, Protocol, Optional

T = TypeVar('T')

class DataStore(Protocol):
    """Protocol for data storage implementations."""
    def get(self, key: str) -> Optional[str]: ...
    def set(self, key: str, value: str) -> None: ...

def get_or_default(store: DataStore, key: str, default: T) -> str | T:
    """Get value from store or return default."""
    value = store.get(key)
    return value if value is not None else default
```

❌ **Bad typing**:
```python
def process_data(data: Any) -> Any:  # Too vague
    return something

def get_value(key):  # No type annotations
    return store[key] if key in store else None
```

### Handling Untyped Libraries

When using libraries without type stubs:

```python
# ✅ Create typed wrappers
from untyped_lib import Client  # type: ignore[import]
from pydantic import BaseModel

class UserData(BaseModel):
    """Type-safe user data model."""
    id: str
    name: str
    email: str

class TypedClient:
    """Type-safe wrapper for untyped client."""
    
    def __init__(self) -> None:
        self._client = Client()
    
    def get_user(self, user_id: str) -> UserData:
        """Get user with type safety."""
        raw_data = self._client.fetch_user(user_id)
        return UserData.model_validate(raw_data)
```

## Code Style Guidelines

### TODO Comments

**CRITICAL: All TODO comments must be resolved before opening a PR.**

```python
# ❌ Don't leave TODOs in PR
def calculate_price(item):
    # TODO: Add tax calculation
    return item.base_price

# ✅ Either implement or remove
def calculate_price(item):
    price = item.base_price
    price += price * TAX_RATE  # Implemented
    return price
```

**Handling TODOs during development:**
1. **Implement it** - Complete the functionality
2. **Remove it** - If no longer needed
3. **Track it** - Create a GitHub issue and remove the TODO
4. **Never** leave TODO comments in code submitted for PR

### Function and Method Design

**Keep functions small and focused**:
- 5-15 lines per function ideal
- Each function does ONE thing
- Extract complex logic into helpers

✅ **Well-structured code**:
```python
def process_order(order_data: OrderData) -> Order:
    """Process a new order through the system."""
    validate_order_data(order_data)
    order = create_order(order_data)
    send_order_confirmation(order)
    return order

def validate_order_data(data: OrderData) -> None:
    """Validate order data meets requirements."""
    if not data.items:
        raise ValueError("Order must contain items")
    if data.total <= 0:
        raise ValueError("Order total must be positive")
```

### Guard Clauses Pattern

Use early returns to reduce nesting:

✅ **Clean with guard clauses**:
```python
def process_payment(payment: Payment) -> PaymentResult:
    """Process payment with validation."""
    if not payment.is_valid():
        return PaymentResult.error("Invalid payment data")
    
    if is_duplicate_payment(payment):
        return PaymentResult.error("Duplicate payment")
    
    if exceeds_daily_limit(payment):
        return PaymentResult.error("Daily limit exceeded")
    
    # Happy path
    return charge_card(payment)
```

## Configuration and Dependency Injection

### Service Pattern with DI

```python
from {{cookiecutter.project_slug}}.core.config import Config
from {{cookiecutter.project_slug}}.core.container import create_container

# Service with explicit dependencies
class DocumentService:
    """Service for document processing."""
    
    def __init__(
        self,
        config: Config,
        vector_store: VectorStoreService,
        chunking_service: ChunkingService,
    ):
        self.config = config
        self.vector_store = vector_store
        self.chunking = chunking_service
    
    async def process_document(self, path: Path) -> Document:
        """Process document through pipeline."""
        chunks = await self.chunking.chunk_file(path)
        embeddings = await self.vector_store.embed_chunks(chunks)
        return Document(chunks=chunks, embeddings=embeddings)

# Usage with container
async with create_container(config) as container:
    doc_service = container.get(DocumentService)
    result = await doc_service.process_document(path)
```

### Configuration Best Practices

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class ServiceConfig:
    """Immutable service configuration."""
    api_key: str = field(repr=False)  # Hide from logs
    timeout: int = 30
    retry_count: int = 3
    
    def with_overrides(self, **kwargs) -> "ServiceConfig":
        """Create new config with overrides."""
        return replace(self, **kwargs)
```

## Testing While Developing

### Main Branch is Always Green

**IMPORTANT: The main branch always has passing tests.** PRs with failing tests cannot be merged.

This means:
- **Test failures during development are always caused by your changes**
- If a test fails, it's your code that needs fixing, not the test
- In the rare case of a flaky test, document it as a deviation

```markdown
## Deviations

### Flaky Test: test_external_service_timeout
**Issue**: Test fails intermittently (~10% of runs)
**Root cause**: External service mock has timing issues
**Temporary fix**: Increased timeout from 1s to 3s
**TODO**: Create issue to properly fix the race condition
```

### Test-Driven Development (TDD)

Write tests as you code:

```python
def test_order_validation_rejects_empty_items():
    """Empty orders should be rejected."""
    # Given: Order with no items
    order_data = OrderData(items=[], total=0)
    
    # When/Then: Validation fails
    with pytest.raises(ValueError, match="must contain items"):
        validate_order_data(order_data)
```

### Testing Patterns

**Use fakes over mocks**:

```python
# ✅ Simple fake
class FakeEmailService:
    """Fake email service for testing."""
    
    def __init__(self):
        self.sent_emails: list[Email] = []
    
    def send(self, email: Email) -> None:
        """Record email instead of sending."""
        self.sent_emails.append(email)

# Usage in tests
def test_order_sends_confirmation():
    """Order processing sends confirmation email."""
    # Given
    fake_email = FakeEmailService()
    service = OrderService(email_service=fake_email)
    
    # When
    order = service.process_order(order_data)
    
    # Then
    assert len(fake_email.sent_emails) == 1
    assert fake_email.sent_emails[0].to == order.customer_email
```

## Documentation Standards

### Google-Style Docstrings

```python
def calculate_discount(
    order: Order,
    customer: Customer,
    promotions: list[Promotion],
) -> Decimal:
    """Calculate total discount for an order.
    
    Applies all applicable promotions and customer-specific
    discounts to determine the final discount amount.
    
    Args:
        order: The order to calculate discount for
        customer: Customer placing the order
        promotions: List of active promotions
        
    Returns:
        Total discount amount in order currency
        
    Raises:
        ValueError: If discount exceeds order total
        
    Example:
        >>> discount = calculate_discount(order, customer, promos)
        >>> final_price = order.total - discount
    """
```

## Logging Standards

Use structured logging with structlog:

```python
import structlog

logger = structlog.get_logger(__name__)

class PaymentService:
    """Service for processing payments."""
    
    async def process_payment(self, payment: Payment) -> PaymentResult:
        """Process a payment transaction."""
        logger.info(
            "Processing payment",
            payment_id=payment.id,
            amount=payment.amount,
            currency=payment.currency,
        )
        
        try:
            result = await self._charge_card(payment)
            logger.info(
                "Payment successful",
                payment_id=payment.id,
                transaction_id=result.transaction_id,
            )
            return result
            
        except PaymentError as e:
            logger.exception(
                "Payment failed",
                payment_id=payment.id,
                error_code=e.code,
            )
            raise
```

### Log Levels

- **DEBUG**: Detailed execution flow, cache operations
- **INFO**: Major operations, state changes
- **WARNING**: Recoverable issues, degraded functionality
- **ERROR**: Unrecoverable errors (with `logger.exception()`)

## Exception Handling

### Creating Custom Exceptions

```python
# Use built-in for simple validation
def validate_age(age: int) -> None:
    """Validate age is positive."""
    if age < 0:
        raise ValueError("Age must be non-negative")

# Custom exceptions for domain logic
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    
    def __init__(self, required: Decimal, available: Decimal):
        self.required = required
        self.available = available
        super().__init__(
            f"Insufficient funds: required {required}, "
            f"available {available}"
        )
```

### Exception Handling Patterns

```python
# ✅ Specific exception handling
try:
    result = await api_client.fetch_data(url)
except HTTPError as e:
    if e.status_code == 429:
        logger.warning("Rate limited", url=url)
        return cached_result
    raise
except ConnectionError:
    logger.error("API unreachable", url=url)
    return fallback_result

# ❌ Avoid broad exception catching
try:
    result = process_data(data)
except Exception:  # Too broad!
    return None
```

## Import Guidelines

### Import Location and Order

**CRITICAL: Imports MUST go at the top of the file** unless absolutely necessary to avoid circular dependencies.

```python
# ✅ Imports at top of file (REQUIRED)
import asyncio
from pathlib import Path
from typing import Optional

from pydantic import BaseModel
import structlog

from {{cookiecutter.project_slug}}.core.exceptions import ValidationError
from {{cookiecutter.project_slug}}.services import DocumentService

# ❌ Only use function-level imports when necessary
def process_data():
    # Only if needed to avoid circular import
    from {{cookiecutter.project_slug}}.core.services import DataService
    return DataService().process()
```

### Import Ordering

Imports must be in the correct order. Use `ruff` to automatically fix:

```bash
# Automatically fix import order
uv run ruff check --fix .
```

**Standard import order**:
1. Standard library imports
2. Third-party imports  
3. Local application imports

Each group separated by a blank line.

### Import Style

```python
# ✅ Use absolute imports
from {{cookiecutter.project_slug}}.core.services import AuthService
from {{cookiecutter.project_slug}}.core.models import User
from {{cookiecutter.project_slug}}.core.config import Config

# ❌ Avoid relative imports in production code
from ..models import User  # Don't do this
```

## Common Patterns

### Async Context Managers

```python
class DatabaseConnection:
    """Async database connection manager."""
    
    async def __aenter__(self) -> "DatabaseConnection":
        """Open connection."""
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Close connection."""
        await self.disconnect()

# Usage
async with DatabaseConnection(config) as db:
    result = await db.query("SELECT * FROM users")
```

### Protocol-Based Interfaces

```python
from typing import Protocol

class MessageSender(Protocol):
    """Protocol for message sending services."""
    
    async def send(self, message: Message) -> None: ...
    def can_send(self, message: Message) -> bool: ...

# Any class with these methods satisfies the protocol
class EmailSender:
    async def send(self, message: Message) -> None:
        # Implementation
    
    def can_send(self, message: Message) -> bool:
        return "@" in message.recipient
```

## Performance Considerations

### Batch Operations

```python
# ✅ Process in batches
async def process_documents(paths: list[Path]) -> list[Document]:
    """Process multiple documents efficiently."""
    BATCH_SIZE = 10
    results = []
    
    for i in range(0, len(paths), BATCH_SIZE):
        batch = paths[i:i + BATCH_SIZE]
        batch_results = await asyncio.gather(
            *[process_document(path) for path in batch]
        )
        results.extend(batch_results)
    
    return results
```

## Next Steps

After coding with these standards:

1. ✅ Run `scripts/check unit` frequently
2. ✅ Keep functions small and focused
3. ✅ Write tests for new functionality
4. ✅ Document public APIs

→ **Continue to [SUBMISSION.md](SUBMISSION.md)** for PR preparation and submission

---

## Quick Style Reference

```python
# Function naming: snake_case, descriptive
def calculate_total_price(items: list[Item]) -> Decimal:

# Class naming: PascalCase
class OrderService:

# Constants: UPPER_SNAKE_CASE
DEFAULT_TIMEOUT = 30

# Type annotations: always required
name: str
items: list[dict[str, Any]]
callback: Callable[[int], None]

# Docstrings: Google style, always for public APIs
"""Brief description.

Longer description if needed.

Args:
    param: Description

Returns:
    Description
"""
```