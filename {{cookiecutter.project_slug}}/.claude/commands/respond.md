# /respond - Respond to PR Review Comments

Systematically address all review comments on the current PR by checking CI status, fixing issues, and responding to reviewers.

## Process

1. **Check CI Status**
   - Use `gh pr checks <pr-number>` to check current CI status
   - If CI is running, wait for it to complete before proceeding
   - If no PR number provided, determine it from current branch with `gh pr list --head <current-branch>`

2. **Handle CI Failures**
   - If CI failed, use `gh run view <run-id> --log-failed` to get failure details
   - Identify specific failing tests or issues
   - Fix the issues (update code, fix tests, etc.)
   - Commit and push fixes
   - Wait for CI to pass before proceeding to review comments

3. **Gather Review Comments**
   - Use `gh api repos/{owner}/{repo}/pulls/{pr}/reviews` to get all reviews
   - Use `gh api repos/{owner}/{repo}/pulls/{pr}/comments` to get line-by-line comments
   - Use `gh api repos/{owner}/{repo}/issues/{pr}/comments` to get general PR comments
   - Filter to comments created after the last response (if this isn't the first time responding)
   - Show the user the full CLI commands used and the actual comment text retrieved

4. **Categorize Comments**
   - **Real Issues**: Comments pointing to actual bugs, security issues, or code problems
   - **Suggestions**: Improvement suggestions or style preferences
   - **Future Work**: Features or changes that should be handled in separate PRs/issues
   - **Incorrect/Disputed**: Comments that are factually wrong or based on misunderstanding

5. **Address Each Comment**

   For **Real Issues**:
   - Fix the issue in code
   - Test the fix locally
   - Commit with descriptive message
   - Push changes
   - Reply to comment: "✅ Fixed in commit [hash]. [Brief description of fix]. @[reviewer-username]"

   For **Future Work**:
   - Ask user: "This comment suggests [description]. Should I create a follow-up issue for this?"
   - If user agrees, create GitHub issue with `gh issue create`
   - Reply to comment: "✅ Created follow-up issue #[number] to track this enhancement. @[reviewer-username]"

   For **Incorrect/Disputed**:
   - Reply with explanation: "This is actually [correct behavior/already implemented] because [detailed explanation]. @[reviewer-username]"

   For **Suggestions**:
   - Implement if reasonable and within PR scope
   - If out of scope, treat as Future Work
   - Reply appropriately based on action taken

6. **Post Comprehensive Summary**
   - Create a summary comment listing all changes made
   - Reference specific commits for each fix
   - Thank reviewers explicitly
   - Use format: "Thank you @[reviewer] for the thorough review! I've addressed all your feedback in commits [list]:"

## Requirements

- Always address reviewers by @username so they get notifications
- Show full CLI commands used to gather review data
- Provide commit hashes for all fixes
- Never leave a review comment without a response
- If uncertain about whether something is an issue, ask the user first
- Wait for CI to pass before responding to comments (fixes might affect other issues)

## Example Response Format

```
Thank you @reviewer-name for the detailed feedback! I've addressed all your comments:

**High Priority - Resource Leak:**
✅ Fixed in commit abc1234. Added proper socket cleanup in cancellation handler to prevent orphaned threads.

**Medium Priority - Exception Handling:**  
✅ Fixed in commit def5678. Replaced broad Exception with specific OSError and EOFError catching.

**Future Enhancement - Test Automation:**
✅ Created follow-up issue #123 to track CLI integration test automation as suggested.

All fixes have been tested and CI is passing. The implementation is now ready for final review!
```

## Notes

- This command should only be used on open PRs with review comments
- Always verify CI passes before and after making changes
- If multiple rounds of review, only address new comments since last response
- Create follow-up issues liberally to keep PR scope focused