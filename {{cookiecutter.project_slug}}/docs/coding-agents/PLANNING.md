# Planning Guide - Before You Code

## 🛑 STOP: DO NOT WRITE CODE YET

**If you're reading this because you were asked to work on a task, STOP and read this entire guide first. Planning is MANDATORY for non-trivial tasks.**

This guide covers everything you need to do **before writing code**: understanding requirements, researching existing solutions, and planning your implementation.

## When Planning is MANDATORY

**You MUST follow this planning process for:**
- ✅ ANY refactoring (like renaming directories across the codebase)
- ✅ New features or functionality
- ✅ Changes affecting multiple files
- ✅ Architecture or API changes
- ✅ Any task estimated > 30 minutes
- ✅ Working on GitHub issues

**Skip planning only for:**
- ❌ Simple typo fixes
- ❌ Single-line bug fixes
- ❌ Documentation updates only

## 📋 Planning Process Overview

**⚠️ MANDATORY STEPS - Follow IN ORDER - DO NOT skip ahead:**

1. **Fetch and understand requirements** - Get latest code, read issue/learn from user
2. **Create meaningful branch** - Branch name based on issue/feature
3. **Research codebase** - Read relevant code and documentation
4. **Ask questions** - Clarify any uncertainties before planning
5. **Develop plan** - Create comprehensive implementation approach
6. **Create TODO.md** - Document the plan formally
7. **Get explicit approval** - MUST have user approval before coding

**🚨 CRITICAL: If you skip planning and jump to implementation, you will be asked to stop and start over with proper planning.**

## ❌ Common Mistake Example

**User**: "Work on issue #441 - refactor directory structure"

**WRONG approach (what NOT to do):**
```bash
# ❌ Immediately starts refactoring
git mv src/{{cookiecutter.project_slug}}/core/old_name src/{{cookiecutter.project_slug}}/core/new_name
git mv src/{{cookiecutter.project_slug}}/modules/old_name src/{{cookiecutter.project_slug}}/modules/new_name
# ... continues making changes without planning
```

**CORRECT approach:**
1. Read this planning guide
2. View the issue: `gh issue view 441`
3. Create a branch: `git checkout -b refactor/issue-441-directory-rename origin/main`
4. Research the codebase
5. Create TODO.md with refactoring plan
6. Get user approval
7. ONLY THEN start implementation

## Quick Reference

| Task | Action |
|------|--------|
| New feature | Create TODO.md → Get approval → Check in → Write tests |
| Add dependency | Research options → Create proposal → Get approval → Test integration |
| Bug fix | Check GitHub issue → Write failing test → Research codebase → Plan fix |
| Refactoring | Document current state → Plan changes → Get approval → Maintain test coverage |

## GitHub Issues Integration

The project uses GitHub issues for task tracking. You can access and manage issues directly from the command line:

```bash
# View issue details
gh issue view 123

# List open issues
gh issue list

# Create a new issue
gh issue create --title "Bug: Description" --body "Details..."

# Comment on an issue
gh issue comment 123 --body "Progress update..."
```

### ⚠️ Shell Escaping Warning

When using CLI tools like `gh`, be careful with shell metacharacters in your input:

```bash
# ❌ Dangerous - unescaped characters can cause problems
gh issue comment 123 --body "Fixed $USER's bug with && operator"

# ✅ Safe - use quotes and escape special characters
gh issue comment 123 --body "Fixed user's bug with '&&' operator"

# ✅ Safe - use here documents for complex content
gh issue comment 123 --body "$(cat <<'EOF'
Fixed the bug with special chars: $, &, |, ;
Test case: foo && bar || baz
EOF
)"
```

Always quote your strings and be mindful of: `$ & | ; > < \` `` * ? [ ] ( ) { }`

## Research Before Implementation

### MANDATORY: Search Existing Code First

**Before implementing ANY new functionality, you MUST:**

1. **Search the entire codebase** for similar functionality:
   ```bash
   # Search for function patterns
   grep -r "def validate" src/
   grep -r "class.*Service" src/
   
   # Search for specific functionality
   grep -r "timeout.*int" src/
   grep -r "ValueError.*positive" src/
   
   # Check common utility locations
   ls src/{{cookiecutter.project_slug}}/config.py
   ls src/{{cookiecutter.project_slug}}/services.py
   ls src/{{cookiecutter.project_slug}}/exceptions.py
   ```

2. **Review test files** to understand existing patterns:
   ```bash
   grep -r "test_.*validate" tests/
   find tests/ -name "*service*" -type f
   ```

3. **Only create new code if nothing similar exists**

4. **Write tests first** for the functionality you're about to implement

### When You Find Existing Code

- **Extend it** with optional parameters if needed
- **Refactor it** to be more general if appropriate
- **Import and reuse it** rather than duplicating
- **Never duplicate** functionality that already exists

## Library Dependency Management

### When to Add a Dependency

Use this decision tree:

```
1. Is this core business logic for {{cookiecutter.project_slug}}?
   YES → Implement custom code
   NO  → Continue to step 2

2. Can this be implemented in <10 lines of simple code?
   YES → Implement custom code
   NO  → Continue to step 3

3. Does existing functionality in the codebase solve this?
   YES → Use/extend existing code
   NO  → Continue to step 4

4. Research libraries and create proposal
   → Use Library Proposal Template
   → Get approval before proceeding
```

### Library Proposal Template

```markdown
## Library Proposal: [Feature/Functionality]

**GitHub Issue**: #[issue-number]
**Problem**: [What you're trying to solve]

### Options Considered

#### Option 1: [Library Name]
- **PyPI**: https://pypi.org/project/[name]
- **GitHub**: https://github.com/[owner]/[repo]
- **Stars**: [count] | **Last Update**: [date]
- **License**: [license]
- **Size**: [installed size]

**Pros**:
- [Feature 1]
- [Feature 2]

**Cons**:
- [Limitation 1]
- [Limitation 2]

**Example Usage**:
```python
# Show how it would be used in our codebase
from library import Feature
result = Feature().process(data)
```

#### Option 2: [Library Name]
[Same structure as Option 1]

#### Option 3: Custom Implementation
**Estimated LOC**: [number]
**Pros**:
- No external dependencies
- Exact fit for our needs
- Full control

**Cons**:
- Maintenance burden
- Need to handle edge cases
- Testing overhead

### Recommendation

I recommend **[Option N]** because:
1. [Reason 1]
2. [Reason 2]

### Impact Analysis
- **Bundle size increase**: [amount]
- **New dependencies pulled**: [list]
- **Security considerations**: [any concerns]
- **Maintenance burden**: [assessment]
```

## TODO.md Process for Significant Changes

### When to Create TODO.md

Create a TODO.md for:
- ✅ New feature implementation
- ✅ Significant refactoring (>100 lines affected)
- ✅ Architecture changes
- ✅ Breaking API changes
- ✅ Complex multi-step tasks

Skip TODO.md for:
- ❌ Simple bug fixes (but still write a test first!)
- ❌ Documentation updates
- ❌ Minor code cleanup
- ❌ Adding single tests

### TODO.md Template

```markdown
# [Feature/Change Title]

**GitHub Issue**: #[number] - [Issue title]
**Branch**: feature/[descriptive-name]

## Goal

[1-2 sentences describing what this change accomplishes]

## Research Completed

- [x] Searched for existing [functionality]: [what you found]
- [x] Reviewed similar code in: [files/modules]
- [x] Checked test patterns in: [test files]

## High-Level Plan

[Overall approach and architectural decisions]

## Public API Changes

**New APIs**:
- `function_name(params) -> ReturnType` - [purpose]
- `ClassName` - [purpose]

**Modified APIs**:
- `existing_function()` - [what changes]

**Breaking Changes**:
- [List any breaking changes]

## Testing Plan

**Test-First Development**:
- [ ] Write failing tests before implementation
- [ ] Tests should define expected behavior

**Unit Tests**:
- [ ] Test [component] with [scenario]
- [ ] Test error cases for [functionality]
- [ ] Run `scripts/check unit` after each test

**Integration Tests**:
- [ ] Test [workflow] end-to-end
- [ ] Test [integration point]
- [ ] Verify component interactions

**Manual Testing**:
- [ ] Run [command] and verify [outcome]
- [ ] Test with [configuration]
- [ ] Run full `scripts/check` before proceeding

## Implementation Steps

- [ ] Step 1: Write failing tests for [functionality]
- [ ] Step 2: [Implement specific, measurable task]
- [ ] Step 3: Make tests pass
- [ ] Step 4: [Another specific task with tests]
- [ ] Step 5: Update documentation in [file]
- [ ] Step 6: Run scripts/check and fix any issues

## Deviations

[This section is added during implementation if plans change]
```

### TODO.md Workflow

**IMPORTANT: This is not optional for significant changes.**

1. **Complete all planning steps first** (fetch, branch, research, questions)
2. **Create TODO.md** with all sections thoroughly filled
3. **Share complete plan** with user for review
4. **Wait for explicit approval** - User must say "approved" or similar
5. **Only after approval**: Check in TODO.md as first commit
6. **Then and only then**: Begin implementation
7. **Follow plan exactly** - Check off steps as completed
8. **Document any deviations** - Get approval before implementing changes
9. **Request permission** to delete TODO.md only after all work is complete

**Example approval request:**
```
I've completed the planning phase:
- Reviewed issue #123 and understood requirements  
- Created feature/issue-123-oauth-integration branch from origin/main
- Researched existing auth code in src/{{cookiecutter.project_slug}}/core/auth/
- Created comprehensive TODO.md with implementation plan

Please review the TODO.md and approve if the approach looks good.
```

## Detailed Planning Process

### Step 1: Fetch and Understand Requirements

**Start in READ-ONLY mode:**

```bash
# FIRST: Always fetch latest changes
git fetch origin

# THEN: Understand what needs to be done
```

**If GitHub issue exists**: 
```bash
gh issue view 123  # Read issue details
gh issue view 123 --comments  # Read all discussion
```

**If no issue**: 
- Ask user for detailed requirements
- Get clear understanding of the task
- Clarify the scope and goals

**Key**: Stay on current branch - just reading, no changes yet!

### Step 2: Create Meaningful Branch

**Now create branch with descriptive name:**

```bash
# Branch name reflects the actual work
git checkout -b fix/issue-123-validation-error origin/main
git checkout -b feature/oauth-integration origin/main
git checkout -b refactor/consolidate-services origin/main

# Include issue number when applicable
git checkout -b fix/issue-234-memory-leak origin/main
```

**Good branch names:**
- `fix/issue-123-user-validation`
- `feature/add-export-functionality`
- `refactor/extract-email-service`
- `docs/update-api-guide`

**Bad branch names:**
- `feature/new-feature`
- `fix/bug`
- `update`

### Step 3: Research Codebase

**Read and understand existing code:**

```bash
# Search for related functionality
grep -r "similar_feature" src/
rg "pattern" --type py

# Read relevant files
cat src/{{cookiecutter.project_slug}}/core/services.py
cat tests/unit/test_services.py
```

### Step 4: Ask Questions

**Clarify before planning:**

- "Should this feature support X?"
- "What should happen when Y occurs?"
- "Are there performance requirements?"
- "Should this integrate with existing Z?"

**Don't assume - ASK!**

### Step 5: Develop Comprehensive Plan

**Consider all aspects:**

- Architecture decisions
- API design
- Testing strategy
- Performance implications
- Security considerations
- Migration needs

### Step 6: Create TODO.md

**Use the template to document everything:**

- Clear goals and approach
- Detailed implementation steps
- Testing plan
- API changes

### Step 7: Get Explicit Approval

**Present TODO.md and wait:**

```
"I've created a TODO.md with the implementation plan for [feature].
Please review and let me know if this approach looks good or if 
any changes are needed."
```

**DO NOT PROCEED WITHOUT APPROVAL**

## Branch Strategy

### Branch Naming

```bash
# Always fetch first and branch from origin/main
git fetch origin

# Features
git checkout -b feature/add-user-auth origin/main
git checkout -b feature/vector-search origin/main

# Bug fixes
git checkout -b fix/memory-leak origin/main
git checkout -b fix/issue-123-validation origin/main

# Refactoring
git checkout -b refactor/service-layer origin/main
git checkout -b refactor/test-structure origin/main

# Documentation
git checkout -b docs/api-guide origin/main
git checkout -b docs/installation origin/main
```

### Branch Workflow

1. **Always fetch and branch from origin/main**:
   ```bash
   git fetch origin
   git checkout -b feature/name origin/main
   ```

2. **For TODO.md-based work**:
   ```bash
   # First commit is always TODO.md
   git add TODO.md
   git commit -m "docs: add implementation plan for [feature]"
   ```

3. **Keep branches focused** - one feature/fix per branch

## Architecture Planning

### Design Patterns to Consider

| Pattern | When to Use | Example |
|---------|-------------|---------|
| **Repository** | Data access abstraction | `UserRepository.find_by_email()` |
| **Service** | Business logic encapsulation | `AuthenticationService.login()` |
| **Factory** | Complex object creation | `DocumentFactory.create_from_json()` |
| **Strategy** | Swappable algorithms | `SearchStrategy`, `RankingStrategy` |
| **Adapter** | Third-party integration | `OpenAIAdapter`, `DatabaseAdapter` |

### System Design Considerations

Before implementing, consider:

1. **Testability**: Can this be easily unit tested? Write the test first!
2. **Scalability**: Will this work with 10x the data?
3. **Maintainability**: Will others understand this in 6 months?
4. **Performance**: Are there any obvious bottlenecks?
5. **Security**: Are we handling sensitive data properly?
6. **Test Coverage**: Are all edge cases testable?

## Next Steps

Once your planning is complete and approved:

1. ✅ TODO.md checked into branch (if applicable)
2. ✅ Dependencies approved (if any)
3. ✅ Research completed and documented
4. ✅ GitHub issue linked and updated

→ **Continue to [DEVELOPMENT.md](DEVELOPMENT.md)** for coding standards and practices

---

## Quick Command Reference

```bash
# GitHub issue management
gh issue list --label bug
gh issue view 123
gh issue create --title "Title" --body "Description"
gh issue comment 123 --body "Update"

# Research commands
grep -r "pattern" src/
find . -name "*.py" -exec grep -l "pattern" {} \;
rg "pattern" --type py  # If ripgrep available

# Branch creation
git fetch origin
git checkout -b feature/name origin/main
```