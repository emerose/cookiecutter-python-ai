Submit the completed work by following the PR submission process.

**Step 1: Verify all checks pass**
```bash
scripts/check
```

## 🛑 CRITICAL: TEST FAILURES BLOCK SUBMISSION

**If ANY checks fail (including tests):**
- **STOP IMMEDIATELY** - Do not continue
- **NO EXCEPTIONS** - There are no "unrelated" test failures
- **REPORT TO USER** - Say: "Cannot proceed - tests are failing: [list failures]"
- **FIX REQUIRED** - Must fix all failures before continuing

**STOP if any checks fail** - fix all issues before proceeding.

**Step 2: Remove TODO.md as final commit**
```bash
git rm TODO.md
git commit -m "docs: remove completed TODO.md"
```

**Step 3: Follow SUBMISSION.md process exactly**

Read and follow ALL steps in `docs/coding-agents/SUBMISSION.md`, including:
- Rebase on latest main
- Run scripts/check again after rebase
- Complete the comprehensive PR checklist
- Verify each checklist item individually
- Create PR with proper description
- Link to relevant issues

**Critical:**
- Never proceed with failing checks
- TODO.md removal must be the LAST commit before submission
- You MUST complete every item in the PR checklist
- Follow the exact process in SUBMISSION.md - no shortcuts

Read `docs/coding-agents/SUBMISSION.md` NOW and follow it exactly.