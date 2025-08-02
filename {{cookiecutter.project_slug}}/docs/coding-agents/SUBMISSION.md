# Submission Guide - Before You Submit

This guide covers everything needed to prepare and submit a pull request: quality checks, testing requirements, and the PR process.

## When to Use This Guide

- Preparing code for PR submission
- Running final quality checks
- Writing commit messages
- Completing PR checklist
- Addressing review feedback

## 🚨 CRITICAL: Complete PR Checklist

**You MUST complete every item in this checklist before submitting any PR. This is non-negotiable.**

**IMPORTANT FOR AI AGENTS**: You must explicitly go through each checklist item below and verify compliance. Do not assume or skip items. Check each one individually and confirm it's done.

## ⚠️ AI AGENT CRITICAL RULES

1. **CHECK FAILURES = FULL STOP** - If ANY check fails at ANY point, you MUST:
   - Stop immediately
   - Report to the user: "Cannot proceed - checks are failing"
   - List the exact failures
   - Do NOT rationalize failures as "unrelated" or "pre-existing"
   - Do NOT proceed until all checks pass

2. **NO RATIONALIZATIONS** - Common mistakes to avoid:
   - ❌ "These failures seem unrelated to my changes"
   - ❌ "The tests were probably failing before"
   - ❌ "I'll proceed and mention it in the PR"
   - ✅ "Tests are failing. I must fix them or ask for help."

## Pre-Submission Quality Gates

### 1. Update and Rebase on Main

**CRITICAL: Always rebase on latest main before submitting PR.**

```bash
# Fetch latest changes
git fetch origin

# Rebase your branch on main (NOT merge)
git rebase origin/main

# Resolve any conflicts if they arise
# Then continue rebase
git rebase --continue
```

**Important**: This repository **does not allow merge commits**, only rebase. Never use `git merge`.

### 2. Run Full Quality Check After Rebase

```bash
# MANDATORY after rebase and before every PR
scripts/check

# Must see: "All checks passed! ✅"
```

## 🛑 CRITICAL: TEST FAILURES BLOCK ALL PROGRESS

**If ANY checks fail (including tests):**
- **STOP IMMEDIATELY** - Do not continue with submission
- **NO EXCEPTIONS** - There is no such thing as "unrelated" test failures
- **REPORT TO USER** - State: "Cannot proceed with PR submission - tests/checks are failing"
- **LIST FAILURES** - Show the exact failures to the user
- **FIX REQUIRED** - All failures must be fixed before proceeding

**AI AGENTS: You MUST NOT rationalize or ignore test failures. Every failure matters.**

### 3. Check for Common Issues

```bash
# Look for debug code
grep -r "print(" src/
grep -r "breakpoint()" src/
grep -r "import pdb" src/

# Check for TODO comments
grep -r "TODO" src/
grep -r "FIXME" src/

# Look for test skips
grep -r "@pytest.mark.skip" tests/
grep -r "pytest.skip" tests/
```

## Testing Requirements

### Test Coverage Expectations

All new code must include tests:

- **Business logic**: Full unit test coverage
- **Bug fixes**: Test that reproduces and verifies fix
- **New features**: Unit + integration tests
- **Refactoring**: Maintain or improve existing coverage

### Running Tests

```bash
# Quick feedback during development
scripts/check unit              # <100ms per test

# Before submission
scripts/check                   # Standard suite
scripts/check all              # Include E2E tests

# With specific options
scripts/check all -x           # Stop on first failure
scripts/check unit -k "test_name"  # Run specific test
```

### Test Timeout Adjustments

For slower environments:

```bash
# Use multiplier for slower systems
CI_TIMEOUT_MULTIPLIER=3.0 scripts/check

# CI environment settings
CI_TIMEOUT_MULTIPLIER=10.0 scripts/check all
```

### Network Testing

Most tests block network access. For tests requiring network:

```python
import pytest

@pytest.mark.networking
async def test_external_api():
    """Test requiring real network access."""
    response = await fetch_external_data()
    assert response.status == 200
```

Run networking tests separately:
```bash
pytest -m "networking"          # Only network tests
scripts/check all not networking  # Skip network tests
```

## Commit Standards

### Conventional Commit Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types and Examples

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(auth): add OAuth2 support` |
| `fix` | Bug fix | `fix(api): handle null user ID` |
| `docs` | Documentation | `docs(readme): update install steps` |
| `style` | Formatting | `style: apply ruff formatting` |
| `refactor` | Code restructure | `refactor(services): extract validation` |
| `test` | Test changes | `test(auth): add edge cases` |
| `chore` | Maintenance | `chore(deps): update pytest to 7.4` |

### Commit Message Rules

- **Subject**: ≤50 chars, imperative mood, no period
- **Body**: ≤72 chars per line, explain why not what
- **Reference issues**: Include `#123` in body
- **Breaking changes**: Add `BREAKING CHANGE:` in footer

✅ **Good commit**:
```
fix(vector-store): prevent duplicate embeddings

The vector store was allowing duplicate documents to be embedded,
causing search quality degradation. This adds a content hash check
before embedding.

Fixes #234
```

❌ **Bad commit**:
```
Fixed bug
```

## Refactoring Completion

### Definition of Complete Refactoring

A refactor is only complete when:

1. ✅ All code uses new APIs/patterns
2. ✅ All tests updated for new implementation
3. ✅ All documentation reflects changes
4. ✅ No legacy code remains (unless approved)

### Legacy Code Removal

**DEFAULT: Remove all legacy code**

Don't leave:
- Old method names for compatibility
- Deprecated parameters
- Wrapper functions calling new implementations
- Any code marked "deprecated"
- Old import paths

### Requesting Legacy Code Exception

If you must keep legacy code, request approval:

```markdown
## Legacy Code Exception Request

**What needs to be kept**: 
`OldClass.old_method()` compatibility wrapper

**Why it's needed**:
- 47 call sites across 12 modules
- 3 in critical production workflows
- Full migration requires coordinated deployment

**Proposed approach**:
- Add deprecation warning
- Create tracking issue #456
- Remove in version 2.0

May I proceed with this approach?
```

## Handling Lint/Type Errors

### Never Suppress Without Approval

**CRITICAL**: Never add these without explicit approval:
- `# type: ignore`
- `# pyright: ignore`
- `# noqa`
- Disabling rules in config

### Requesting Approval

When you encounter an unfixable error:

```markdown
## Type Ignore Request

**Code with error**:
```python
from untyped_lib import Client  # pyright: Unknown import

def process(client: Client) -> Result:
    # Error: Unknown return type
    return client.fetch_data()
```

**Why ignore needed**:
- Third-party library lacks type stubs
- No typed alternatives exist
- Creating stubs would require reverse-engineering

**Alternatives tried**:
- Searched for typed alternatives
- Attempted Protocol wrapper
- Checked for community stubs

May I add `# type: ignore[import]` to line 1?
```

## PR Submission Process

### 1. Final Rebase and Push

```bash
# One final rebase to ensure you're current
git fetch origin
git rebase origin/main

# Force push after rebase (safe for feature branches)
git push --force-with-lease origin feature/your-feature

# Create PR via CLI
gh pr create \
  --title "feat(component): add new feature" \
  --body "$(cat <<'EOF'
## Summary
- Added new feature X
- Improved performance of Y
- Fixed bug with Z

## Testing
- [x] Unit tests added
- [x] Integration tests pass
- [x] Manual testing completed

## Checklist
Completed docs/PR_CHECKLIST.md ✓

Fixes #123
EOF
)"
```

### 2. PR Description Template

```markdown
## Summary
[Brief description of changes - 2-3 sentences]

## Changes
- [Specific change 1]
- [Specific change 2]
- [Specific change 3]

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] Performance impact assessed

## Screenshots
[If applicable]

## Breaking Changes
[List any breaking changes or "None"]

## Checklist
- [x] Completed `docs/PR_CHECKLIST.md`
- [x] All tests passing
- [x] Documentation updated

Fixes #[issue-number]
```

### 3. Link to Issues

Always reference related issues:
- `Fixes #123` - Closes issue when merged
- `Addresses #456` - References without closing
- `Part of #789` - For partial implementations

## Code Review Response

### Addressing Feedback

1. **Respond to all comments** - Even if just "Done"
2. **Push fixes as new commits** - Don't force-push during review
3. **Re-request review** when ready:
   ```bash
   gh pr review --request @reviewer
   ```

**Note on rebasing during review**:
- During review: Push new commits (don't rebase)
- After approval: Rebase to clean up history if requested
- Final merge: Will be rebased automatically (no merge commits)

### Common Review Fixes

```bash
# Format code
uv run ruff format .

# Fix lint issues
uv run ruff check . --fix

# Update types
uv run pyright

# Run tests
scripts/check
```

## Comprehensive PR Checklist

### Code Quality

#### ✅ Design Principles
- [ ] **YAGNI**: Only implemented what's required for current features
- [ ] **DRY**: Searched codebase thoroughly for existing similar functionality  
- [ ] **Library Research**: For significant non-business logic, researched third-party libraries and got approval for any new dependencies
- [ ] **No backwards compatibility**: No legacy support unless explicitly requested

#### ✅ Type Safety
- [ ] **Strict typing**: All functions, methods, and variables have type annotations
- [ ] **No `Any` types**: Used specific types, generics, or unions instead of `Any`
- [ ] **Minimal `None` returns**: Used Optional, defaults, or exceptions instead of returning `None` where practical
- [ ] **Pyright passes**: No type checking errors in strict mode
- [ ] **All errors fixed immediately**: Fixed pyright and ruff errors as discovered

#### ✅ Exception Handling
- [ ] **Domain-specific exceptions**: Used custom exceptions when they add semantic value
- [ ] **Built-in exceptions**: Used `ValueError`, etc. for simple validation where appropriate
- [ ] **Error context**: Included error codes and context in custom exceptions
- [ ] **Narrow exception catching**: Only caught specific exceptions that are expected and can be recovered from
- [ ] **Let bugs propagate**: Avoided broad `except Exception:` or bare `except:` that hide unexpected errors

#### ✅ Configuration & Dependencies
- [ ] **Dependency injection**: Used `Config` and container pattern instead of parameter proliferation
- [ ] **Immutable config**: Configuration objects are frozen/immutable
- [ ] **No new dependencies**: No external dependencies added without approval process

#### ✅ Logging Standards
- [ ] **Structlog usage**: Used `structlog.get_logger(__name__)` for all logging
- [ ] **Structured context**: Used keyword arguments for all log context (no string formatting)
- [ ] **Exception handling**: Used `logger.exception()` for unexpected errors to capture stack traces
- [ ] **Appropriate levels**: INFO for user-facing events, DEBUG for internal operations
- [ ] **No sensitive data**: No passwords, API keys, or personal data logged at INFO level

### Documentation

#### ✅ Code Documentation
- [ ] **Google-style docstrings**: All public functions, methods, and classes documented
- [ ] **Type annotations**: Comprehensive typing throughout
- [ ] **Usage examples**: Complex functions include docstring examples
- [ ] **Updated documentation**: Documentation files updated if guidelines changed

### Testing

#### ✅ Test Coverage
- [ ] **Tests written**: All new functionality has corresponding tests
- [ ] **Test intention comments**: Every test includes clear English description of what it tests
- [ ] **Three-tier architecture**: Tests placed in correct directory (unit/integration/e2e)
- [ ] **Performance requirements**: Unit tests <100ms, integration tests <500ms, e2e tests <30s
- [ ] **Test-first development**: Tests written before implementation

#### ✅ Test Quality
- [ ] **Business logic focus**: Only tested business logic, not implementation details or framework code
- [ ] **Leverage strict typing**: Didn't test what pyright already validates (types, parameter validation)
- [ ] **No third-party testing**: Didn't test library code, only our business logic interactions
- [ ] **Quality over quantity**: Wrote fewer, meaningful tests rather than duplicative ones
- [ ] **Fakes over mocks**: Used lightweight fake implementations instead of `@patch` decorators
- [ ] **Test behavior, not implementation**: Avoided assertions on method calls, focused on outcomes
- [ ] **Test isolation**: Unit tests have no external dependencies (filesystem, network, APIs)

### Code Standards

#### ✅ Quality Checks
- [ ] **`scripts/check` passes**: All static analysis, linting, and tests pass
- [ ] **Ruff formatting**: Code properly formatted
- [ ] **Ruff linting**: No linting errors
- [ ] **Pyright strict**: No type checking errors
- [ ] **Test coverage**: All new code covered by tests
- [ ] **No TODO comments**: All TODOs resolved or tracked as issues
- [ ] **Imports at top**: All imports at file top unless avoiding circular dependencies
- [ ] **Import order correct**: Used `ruff check --fix` to ensure proper order

#### ✅ Git Standards
- [ ] **Conventional commits**: All commits follow `<type>(<scope>): <subject>` format
- [ ] **Atomic commits**: Each commit represents one logical change
- [ ] **Commit messages**: Clear, imperative mood, under 50 characters for subject
- [ ] **Branch naming**: Follows convention (`feature/`, `fix/`, `refactor/`, `docs/`, `test/`)

### Pull Request

#### ✅ PR Description
- [ ] **Clear description**: Explains what changes were made and why
- [ ] **Linked issues**: References relevant GitHub issues with "Fixes #123"
- [ ] **Breaking changes**: Any breaking changes clearly documented
- [ ] **Testing notes**: Explains how to test the changes

#### ✅ CI/CD
- [ ] **GitHub Actions pass**: All CI checks are green
- [ ] **No conflicts**: Branch is up-to-date with main and has no merge conflicts
- [ ] **Reviewable size**: PR is focused and not too large to review effectively

### Final Verification

#### ✅ Manual Testing
- [ ] **Local testing**: Changes tested locally in realistic scenarios
- [ ] **Edge cases**: Considered and tested error conditions and edge cases
- [ ] **Integration**: Verified changes work with existing functionality

#### ✅ Documentation Sync
- [ ] **Comments accurate**: Code comments reflect actual behavior
- [ ] **Examples work**: All code examples in documentation are functional

#### ✅ Significant Changes (if applicable)
- [ ] **TODO.md process followed**: For complex changes, created TODO.md with user approval
- [ ] **All deviations documented**: Any changes from original plan documented and approved
- [ ] **Implementation plan completed**: All steps checked off in TODO.md
- [ ] **Original design verified**: Code matches planned design plus approved deviations

#### ✅ Review Process
- [ ] **Self-review**: Reviewed own changes line by line before requesting review
- [ ] **Ready for review**: All checklist items completed
- [ ] **Responsive to feedback**: Will address review comments promptly
- [ ] **Task completion**: Consider task complete only when PR is approved and merged

### Quick Verification Commands

```bash
# All must pass before submitting PR
scripts/check                    # Full quality check
grep -r "TODO\|FIXME" src/       # Should be empty
grep -r "print(" src/            # Should be empty
git log --oneline origin/main..HEAD  # Check commit messages
```

## 🤖 AI Agent Final Verification

**STOP! Before creating the PR, you MUST:**

1. **Verify all checks are passing** - Run `scripts/check` one final time
2. **If ANY check fails** - STOP and report: "Cannot create PR - checks are failing"
3. **Read through the ENTIRE checklist above** - Every single item
4. **Manually verify each checkbox** - Don't assume, actually check
5. **Run all verification commands** - Confirm they pass
6. **Self-review the changes** - Read every line of your diff
7. **Confirm compliance** - State explicitly that all items are checked

**Example verification statement before creating PR:**
```
I have completed the PR checklist verification:
- ✅ All checks passing - scripts/check shows "All checks passed! ✅"
- ✅ All design principles followed (YAGNI, DRY, no backwards compatibility)
- ✅ Full type safety with no Any types or unapproved ignores  
- ✅ Documentation updated with Google-style docstrings
- ✅ No TODO comments remaining in code
- ✅ Rebased on latest main and all checks pass
- ✅ All 40+ checklist items verified

Ready to create PR.
```

**If you cannot make this statement because tests are failing:**
```
❌ CANNOT CREATE PR - Tests are failing:
- test_example_one: AssertionError: Expected X but got Y
- test_example_two: ValueError: Invalid configuration

These failures must be fixed before submission can proceed.
```

### After PR Creation

1. **Monitor CI** - Ensure all checks pass
2. **Link issues** - Add references if missed
3. **Notify reviewers** - If urgent
4. **Stay responsive** - Address feedback promptly

## Special Scenarios

### Breaking Changes

For breaking changes:

1. **Discuss first** - Get approval before implementing
2. **Document clearly** - In PR description
3. **Migration guide** - Provide upgrade instructions
4. **Version appropriately** - Major version bump

### Large PRs

If PR is large (>500 lines):

1. **Consider splitting** - Multiple smaller PRs
2. **Provide context** - Detailed description
3. **Guide reviewers** - Suggest review order
4. **Be patient** - Large PRs take time

### Hotfixes

For urgent fixes:

1. **Branch from main** - `git checkout -b hotfix/issue main`
2. **Minimal changes** - Fix only the critical issue
3. **Fast track** - Note urgency in PR
4. **Backport** - If needed for release branches

## Common Rejection Reasons

Avoid these to prevent PR rejection:

1. ❌ **Incomplete PR checklist**
2. ❌ **Failing tests or quality checks**
3. ❌ **No tests for new code**
4. ❌ **Unapproved type ignores**
5. ❌ **Poor commit messages**
6. ❌ **Unrelated changes** ("while I was there...")
7. ❌ **Legacy code left behind**
8. ❌ **Missing documentation**

## Success Criteria

Your PR is ready when:

✅ All checks pass (`scripts/check`)  
✅ PR checklist completed  
✅ Tests cover new functionality  
✅ Documentation updated  
✅ Commits follow convention  
✅ Issue linked appropriately  
✅ No unapproved suppressions  
✅ Clean focused changes  

---

## Quick Reference

```bash
# Final checks
scripts/check                    # Must pass
grep -r "TODO\|FIXME\|print(" src/  # Should be empty

# Create PR
gh pr create --title "type(scope): description"

# Review commands  
gh pr review --comment -b "Feedback"
gh pr review --approve
gh pr review --request @reviewer

# Common fixes
uv run ruff format .            # Format
uv run ruff check . --fix       # Lint
scripts/check unit -x           # Test
```

## After PR Approval

Once approved and all checks pass:

1. **Squash and merge** (preferred) or merge
2. **Delete branch** after merge
3. **Close related issues** if not auto-closed
4. **Update project board** if applicable

🎉 **Congratulations on your contribution!**