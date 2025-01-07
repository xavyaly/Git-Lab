# git 50 complex commands 

Below is a list of 50 critical and complex Git commands designed for advanced workflows, each with a description and example usage:

---

 1. git init --bare
Creates a bare repository for remote collaboration (no working directory).

git init --bare /path/to/repo.git


---

 2. git clone --mirror
Clones a repository with all references, suitable for backup.

git clone --mirror https://github.com/user/repo.git


---

 3. git remote add
Adds a new remote repository.

git remote add upstream https://github.com/another/repo.git


---

 4. git remote set-url
Changes the URL of an existing remote.

git remote set-url origin https://new-url.git


---

 5. git config --global alias
Creates a Git alias for a command.

git config --global alias.st status


---

 6. git diff --name-only
Shows only file names that differ between two commits.

git diff --name-only HEAD HEAD~1


---

 7. git diff --cached
Shows changes staged for the next commit.

git diff --cached


---

 8. git log --oneline --graph
Displays a simplified commit history with a graph.

git log --oneline --graph --all


---

 9. git rebase -i
Interactive rebase to edit, squash, or reorder commits.

git rebase -i HEAD~3


---

 10. git cherry-pick
Applies a specific commit from another branch to the current branch.

git cherry-pick <commit-hash>


---

 11. git stash push -m
Saves uncommitted changes with a custom message.

git stash push -m "WIP: Fixing bugs"


---

 12. git stash pop
Applies the latest stash and removes it from the stash list.

git stash pop


---

 13. git stash branch
Creates a new branch from stashed changes.

git stash branch new-feature


---

 14. git reflog
Tracks the history of HEAD movements for recovery.

git reflog


---

 15. git checkout -b
Creates and switches to a new branch.

git checkout -b feature-branch


---

 16. git branch -d
Deletes a branch locally.

git branch -d feature-branch


---

 17. git branch -r
Lists all remote branches.

git branch -r


---

 18. git clean -fd
Removes untracked files and directories.

git clean -fd


---

 19. git reset --soft
Moves HEAD without affecting the working directory or staging area.

git reset --soft HEAD~1


---

 20. git reset --mixed
Resets HEAD and staging area but leaves the working directory unchanged.

git reset --mixed HEAD~1


---

 21. git reset --hard
Completely resets the HEAD, staging, and working directory to a specific commit.

git reset --hard HEAD~1


---

 22. git rm --cached
Unstages a file but leaves it in the working directory.

git rm --cached file.txt


---

 23. git mv
Renames or moves a file in the repository.

git mv oldfile.txt newfile.txt


---

 24. git blame
Shows who made changes to a specific line in a file.

git blame -L 10,20 file.txt


---

 25. git bisect
Finds the commit that introduced a bug using binary search.

git bisect start
git bisect bad
git bisect good <commit>


---

 26. git tag
Creates a lightweight or annotated tag.

git tag -a v1.0 -m "Release version 1.0"


---

 27. git tag -d
Deletes a local tag.

git tag -d v1.0


---

 28. git push --tags
Pushes all tags to a remote repository.

git push --tags


---

 29. git fetch --prune
Removes deleted branches from the remote.

git fetch --prune


---

 30. git merge --no-ff
Merges branches and forces a merge commit.

git merge --no-ff feature-branch


---

 31. git merge --squash
Combines changes without committing, creating a single commit later.

git merge --squash feature-branch


---

 32. git push --force-with-lease
Forces a push but only if the remote branch hasn’t changed.

git push --force-with-lease


---

 33. git pull --rebase
Pulls changes and rebases instead of merging.

git pull --rebase origin main


---

 34. git shortlog
Summarizes commits by author.

git shortlog -s -n


---

 35. git show
Displays details about a specific commit.

git show <commit-hash>


---

 36. git apply
Applies a patch file without committing it.

git apply changes.patch


---

 37. git format-patch
Generates patch files from commits.

git format-patch HEAD~3


---

 38. git archive
Creates an archive of the repository or a subset of files.

git archive --format=zip HEAD > archive.zip


---

 39. git rev-parse
Gets the commit hash of a branch or reference.

git rev-parse HEAD


---

 40. git log -S
Searches for commits that add or remove a specific string.

git log -S "search-term"


---

 41. git diff --word-diff
Shows word-level differences between commits.

git diff --word-diff HEAD~1 HEAD


---

 42. git sparse-checkout
Checks out only specific directories or files.

git sparse-checkout init
git sparse-checkout set dir/


---

 43. git submodule add
Adds a submodule to your repository.

git submodule add https://github.com/example/repo.git


---

 44. git submodule update
Updates all submodules to their latest commit.

git submodule update --remote


---

 45. git worktree
Creates a new working tree for a branch.

git worktree add ../path-to-dir new-branch


---

 46. git log --since
Shows commits after a specific date.

git log --since="2 weeks ago"


---

 47. git log --grep
Searches commit messages for a specific term.

git log --grep="bugfix"


---

 48. git credential-cache
Caches Git credentials temporarily.

git config --global credential.helper cache


---

 49. git verify-commit
Validates signed commits.

git verify-commit <commit-hash>


---

 50. git config --global init.defaultBranch
Sets the default branch name for new repositories.

git config --global init.defaultBranch main


---

These commands demonstrate advanced techniques and are essential for mastering Git in complex scenarios. Let me know if you'd like detailed explanations or further examples for specific commands!