# Question 6: Git Collaboration

## How I Use Git in Team Projects

### Workflow
1. **Clone** the repository: `git clone <repo-url>`
2. **Create a branch** for each feature: `git checkout -b feature/my-feature`
3. **Make changes** and commit frequently: `git add .` → `git commit -m "message"`
4. **Push** to remote: `git push origin feature/my-feature`
5. **Create Pull Request** on GitHub for code review
6. **Merge** after approval and delete branch

---

## Common Git Command I Use Often
```bash
git status
```

**Why I use it:**
- Check which files are modified/staged
- See which branch I'm on
- Verify everything before committing

**Other frequently used commands:**
- `git pull` – Get latest changes
- `git add .` – Stage all changes
- `git commit -m "message"` – Save changes
- `git push` – Upload to remote
- `git checkout -b branch-name` – Create new branch

---

## Problem I Faced & Solution

### Problem: Merge Conflict

**Situation:** Two developers edited the same file. When I tried to pull changes, Git showed a merge conflict.

**Error:**
```
CONFLICT (content): Merge conflict in app.js
Automatic merge failed; fix conflicts and then commit the result.
```

**How I Solved It:**

1. **Open the conflicting file** (e.g., `app.js`)
2. **Look for conflict markers:**
```javascript
   <<<<<<< HEAD
   // My changes
   =======
   // Their changes
   >>>>>>> branch-name
```
3. **Manually resolve** by keeping correct code
4. **Remove markers** (`<<<<<<<`, `=======`, `>>>>>>>`)
5. **Stage resolved file:** `git add app.js`
6. **Complete merge:** `git commit -m "Resolved merge conflict"`

**Prevention:**
- Pull frequently: `git pull origin main`
- Communicate with team about files being edited
- Use smaller, focused commits

---

## Additional Best Practices
- Write clear commit messages
- Use `.gitignore` for unnecessary files
- Never commit secrets (API keys, passwords)
- Review changes before pushing: `git diff`
- Use branches for all features (never commit directly to `main`)
