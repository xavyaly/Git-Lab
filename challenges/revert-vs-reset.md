# Revert Vs Reset In Git

 Git Revert vs Git Reset

Both `git revert` and `git reset` are used to undo changes in Git, but they operate differently and are suited to different scenarios. Here's a detailed explanation of each, including when to use them and examples.

---

 1. Git Revert
- Definition: `git revert` undoes a specific commit by creating a new commit that reverses the changes introduced by the original commit. The original commit remains in the history.
- Purpose: Keeps the Git history intact, which is ideal for collaborative workflows.
- Use Case: When you need to undo changes safely without altering the commit history, especially when working with a team.

# Example of `git revert`
You have a commit history like this:

A -> B -> C

Now you want to undo commit `C`.

1. Run the revert command:
   
   git revert <commit-hash-of-C>
   

2. A new commit is created that reverses the changes made in commit `C`. Your new history looks like this:
   
   A -> B -> C -> D (revert commit of C)
   

Pros of `git revert`:
- Keeps a clear record of what was changed and undone.
- Safe for shared branches (like `main` or `master`).

Cons:
- Can be tedious if you need to revert multiple commits.

---

 2. Git Reset
- Definition: `git reset` removes commits from the history (if you're resetting the HEAD) or stages/unstages files in the working directory.
- Purpose: Alters Git history by removing or undoing commits entirely, making it look like certain changes never happened.
- Use Case: Used when you want to rewrite commit history, typically for local changes that have not been shared with others.

# Types of Git Reset
There are three types of `git reset` depending on how far you want to roll back:
1. `--soft`: Moves the HEAD pointer to a previous commit, but leaves the changes in the staging area.
2. `--mixed` (default): Moves the HEAD pointer to a previous commit and unstages the changes (keeps them in the working directory).
3. `--hard`: Moves the HEAD pointer and completely deletes all changes in the working directory.

---

# Example of `git reset`
You have a commit history like this:

A -> B -> C

Now you want to remove commit `C`.

1. Check out your branch:
   
   git checkout main
   

2. Run the reset command:
   
   git reset --hard <commit-hash-of-B>
   
   - After this, your commit history becomes:
     
     A -> B
     
   - All changes introduced in `C` are deleted from the working directory.

Pros of `git reset`:
- Powerful for undoing local changes before pushing to a remote.
- Useful for cleaning up commits during a rebase.

Cons:
- Dangerous if used incorrectly, especially with `--hard`, as it can permanently delete changes.
- Not safe for shared branches (rewrites history).

---

 Key Differences

| Feature               | `git revert`                              | `git reset`                             |
|-----------------------|--------------------------------------------|-----------------------------------------|
| History Impact    | Does not modify commit history.            | Rewrites commit history (if resetting HEAD). |
| New Commit        | Creates a new commit to undo changes.      | No new commit is created.               |
| Safety            | Safe for shared repositories.              | Unsafe for shared branches (rewrites history). |
| Undo Scope        | Undoes specific commits.                   | Removes commits entirely or un-stages changes. |
| Working Directory | Does not affect the working directory.     | May affect the working directory (depending on type). |

---

 When to Use Which

1. Use `git revert` when:
   - You're working in a shared repository and need to undo changes without altering commit history.
   - You want to keep track of what was undone for transparency.

2. Use `git reset` when:
   - You're working in a private branch and want to clean up or remove commits.
   - You accidentally made commits that you don't want to keep.
   - You're preparing commits before sharing them (e.g., during an interactive rebase).

---

 Combined Example

Suppose you pushed some commits (`A -> B -> C`) to a shared branch but later realized `C` introduced a bug.

# Safe Approach with `git revert`:
1. Revert commit `C`:
   
   git revert <commit-hash-of-C>
   
   This creates a new commit `D` that undoes the changes from `C`:
   
   A -> B -> C -> D
   

# Local Cleanup with `git reset`:
1. If `C` has not been pushed yet, reset the branch:
   
   git reset --hard <commit-hash-of-B>
   
   Your history becomes:
   
   A -> B
   

---

 Conclusion

- Use `git revert` for undoing changes in a safe and collaborative environment where preserving history is critical.
- Use `git reset` for local cleanups or rewrites where you need to remove or modify commits before sharing them with others.