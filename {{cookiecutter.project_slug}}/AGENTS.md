# AI Agent Quick Reference

This is a quick reference for AI coding agents. For detailed guidance, see the workflow-based documentation in `docs/coding-agents/`.

## 📚 Documentation Structure

Follow these guides in order:

1. **[PLANNING.md](docs/coding-agents/PLANNING.md)** - Before you code
   - GitHub issues, research, TODO.md process, library proposals
   
2. **[DEVELOPMENT.md](docs/coding-agents/DEVELOPMENT.md)** - While you code  
   - Coding standards, patterns, testing, configuration
   
3. **[SUBMISSION.md](docs/coding-agents/SUBMISSION.md)** - Before you submit
   - PR checklist, quality gates, commit standards

## 🚨 Critical Requirements

1. **Complete PR checklist** - MUST complete checklist in [Submission Guide](docs/coding-agents/SUBMISSION.md) before any PR
2. **Run quality checks** - `scripts/check` must pass before submission
3. **Search before implementing** - Always grep for existing functionality
4. **Get dependency approval** - Never add libraries without approval
5. **Follow commit convention** - Use `type(scope): description` format

## 🏃 Quick Commands

```bash
# Setup
uv sync --dev

# Development
scripts/check unit        # Fast feedback
scripts/check            # Standard checks (required)
scripts/check all        # Everything including E2E

# Git workflow  
git checkout -b feature/name origin/main
gh issue view 123
gh pr create --title "feat(scope): description"

# Research
grep -r "pattern" src/
rg "pattern" --type py
```

## 🎯 Workflow Summary

### Planning Phase
1. Check GitHub issue: `gh issue view 123`
2. Create branch: `git checkout -b fix/issue-123-description origin/main`
3. Research codebase: `grep -r "similar_feature" src/`
4. Create TODO.md for significant changes
5. Get user approval before coding

### Development Phase
1. Follow TODO.md implementation steps
2. Write tests first (TDD)
3. Fix type/lint errors immediately
4. Run `scripts/check unit` frequently
5. Document deviations for approval

### Submission Phase
1. Rebase on latest main
2. Run full `scripts/check` (must pass)
3. Complete entire PR checklist
4. Create PR with proper description
5. Respond to all review comments

## 💡 Key Principles

**YAGNI** - Build only what's needed  
**DRY** - Search before implementing  
**Type Safety** - No `Any`, minimal `None`  
**Test First** - Write failing tests before code  
**Fail Early** - Raise errors immediately  

## 🔧 Common Patterns

### Configuration
```python
@dataclass(frozen=True)
class ServiceConfig:
    api_key: str = field(repr=False)
    timeout: int = 30
```

### Testing with Fakes
```python
class FakeEmailService:
    def __init__(self):
        self.sent_emails: list[Email] = []
    
    def send(self, email: Email) -> None:
        self.sent_emails.append(email)
```

### Service with DI
```python
class DocumentService:
    def __init__(self, config: Config, vector_store: VectorStore):
        self.config = config
        self.vector_store = vector_store
```

## ⚠️ Common Mistakes to Avoid

1. **Starting code before planning** - Always plan non-trivial tasks
2. **Ignoring test failures** - No "unrelated" failures exist
3. **Leaving TODOs in code** - Resolve or track as issues
4. **Broad exception catching** - Catch only specific exceptions
5. **Adding dependencies without approval** - Use library proposal process

## 📋 Library Proposal Template

When you need an external library:

1. Check if core business logic (implement yourself)
2. Check if <10 lines of code (implement yourself)
3. Search for existing functionality
4. Create proposal with:
   - Problem description
   - 2-3 library options with pros/cons
   - Recommendation with reasoning
   - Impact analysis

## 🚀 PR Checklist Summary

Before ANY PR submission:

- [ ] All checks pass (`scripts/check`)
- [ ] No TODO comments in code
- [ ] Type annotations everywhere
- [ ] Tests for all new code
- [ ] Google-style docstrings
- [ ] Conventional commits
- [ ] PR description complete
- [ ] Issues linked

**Full checklist: [Submission Guide](docs/coding-agents/SUBMISSION.md)**

---

**Remember**: When in doubt, refer to the detailed guides in `docs/coding-agents/`. They contain comprehensive instructions, examples, and edge cases not covered in this quick reference.