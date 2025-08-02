Explore and plan implementation for: $ARGUMENTS

**Work iteratively with the user to develop a comprehensive plan for this topic.**

First, create a sanitized branch name from `$ARGUMENTS` (e.g. lowercase, spaces to hyphens). Then set up the environment:
```bash
# Example for ARGUMENTS="My New Feature" -> branch "explore/my-new-feature"
git fetch origin
git checkout -b explore/my-new-feature origin/main

**Required process:**
1. Read `docs/coding-agents/PLANNING.md` to understand the planning requirements
2. Ask the user questions about $ARGUMENTS to understand:
   - What problem are we solving?
   - What are the requirements?
   - What constraints exist?
   - How should this integrate with existing code?
3. Research the codebase for related functionality
4. Iteratively develop a plan with the user
5. Create a comprehensive TODO.md
6. Refine based on user feedback
7. Get explicit user approval

**DO NOT:**
- Start any implementation until the user approves the TODO.md
- Make assumptions - ask questions instead
- Skip any planning steps
- Proceed without explicit "approved" or similar confirmation

**Starting point:**
After creating the branch, begin by asking the user to describe what they envision for "$ARGUMENTS". Work together to build a clear plan before any coding begins.

This is an exploratory planning session - no development work should happen until there is an approved TODO.md.