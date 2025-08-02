## 🛑 STOP: DO NOT START CODING

You've been asked to work on GitHub issue #$ARGUMENTS. **DO NOT jump to implementation.**

**MANDATORY PROCESS - NO EXCEPTIONS:**

1. **FIRST**: Read `docs/coding-agents/PLANNING.md` completely
2. **THEN**: Follow ALL 7 planning steps:
   - Fetch and understand requirements (read issue thoroughly)
   - Create meaningful branch (with issue number)
   - Research codebase (search for existing code)
   - Ask questions (clarify all uncertainties)
   - Develop plan (comprehensive approach)
   - Create TODO.md (document everything)
   - Get explicit approval (WAIT for user to approve)
3. **ONLY AFTER APPROVAL**: Start implementation

**⚠️ WARNING**: If you skip planning and start coding immediately (like using `git mv` or editing files), you will be stopped and forced to restart the entire process.

**Quick start for issue #$ARGUMENTS:**
```bash
git fetch origin
gh issue view $ARGUMENTS
gh issue view $ARGUMENTS --comments
```

Then create branch like: `git checkout -b fix/issue-$ARGUMENTS-[description] origin/main`

**DO NOT:**
- Skip any planning steps
- Start coding before TODO.md approval
- Assume anything - ASK QUESTIONS
- Proceed without explicit approval

**REQUIRED READING:**
1. `docs/coding-agents/PLANNING.md` - Complete planning process (READ THIS FIRST!)
2. `docs/coding-agents/DEVELOPMENT.md` - Development standards (after approval)
3. `docs/coding-agents/SUBMISSION.md` - PR submission process

Remember: The planning process is NOT optional. Every step must be completed before writing any code.