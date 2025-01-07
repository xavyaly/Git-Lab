# git cherry-pick 

 Git `cherry-pick` Practical Example

The `git cherry-pick` command allows you to apply a specific commit from one branch to another. Here’s a practical example to demonstrate how to use it.

---

# Scenario
1. You are working on a feature branch (`feature-branch`).
2. A critical bug fix was made in the `main` branch and committed with hash `abc123`.
3. You need to apply this fix to your `feature-branch` without merging the entire `main` branch into your branch.

---

# Step-by-Step Workflow

## 1. Identify the Commit to Cherry-Pick
- First, find the commit hash of the change you want to cherry-pick. 
- Run this in the `main` branch:
  
  git log --oneline
  
  Example output:
  
  abc123 Fix critical bug
  def456 Update documentation
  
  The commit `abc123` is the one you want to apply.

## 2. Switch to the Target Branch
- Switch to the branch where you want to apply the commit (`feature-branch`):
  
  git checkout feature-branch
  

## 3. Cherry-Pick the Commit
- Apply the commit to the current branch:
  
  git cherry-pick abc123
  

- If the cherry-pick is successful, Git will add the changes to your branch and create a new commit.

## 4. Resolve Conflicts (If Any)
- If there are conflicts, Git will pause the cherry-pick process and show conflict markers in the affected files.
- Resolve conflicts manually, then mark them as resolved:
  
  git add <file-with-conflict>
  
- Continue the cherry-pick process:
  
  git cherry-pick --continue
  

## 5. Verify the Changes
- Check the commit history to confirm the cherry-picked commit was applied:
  
  git log --oneline
  
  You should see the new commit added to your `feature-branch`.

---

# Practical Use Case
Imagine you're a DevOps engineer working on an infrastructure repository:
- You’re on a branch `terraform-updates`.
- A critical fix was pushed to the `main` branch that resolves an AWS resource issue.

Apply it to your branch using:

git cherry-pick abc123


This avoids merging all unrelated changes from `main` into your branch while incorporating the necessary fix.

---

# Additional Options
- Cherry-pick multiple commits:
  
  git cherry-pick <commit1> <commit2> <commit3>
  
- Cherry-pick a range of commits:
  
  git cherry-pick <start-commit>^..<end-commit>
  

This is useful for applying multiple related fixes to a branch.

----------------------------------------------------------------------------------------------------------

Live Example:

$ ls -l
total 128
-rw-r--r--@ 1 javedalam  staff   2148 Aug  9 13:12 0-create-repository.md
-rw-r--r--@ 1 javedalam  staff     76 Aug  9 13:12 1-Git-Installations.md
-rw-r--r--@ 1 javedalam  staff   7107 Aug  9 13:12 2-Conflict-Pull-LifeCycle.md
drwxr-xr-x@ 5 javedalam  staff    160 Aug  9 13:12 3-Git-Documents
-rw-r--r--@ 1 javedalam  staff  32294 Aug  9 13:12 4-Git-Commands.md
-rw-r--r--@ 1 javedalam  staff   7838 Aug 13 11:56 5-git-fork-commands.md
-rw-r--r--@ 1 javedalam  staff   3416 Aug 10 12:46 6-pull-requests
-rw-r--r--@ 1 javedalam  staff     68 Aug 10 12:50 7-git-branching.md
drwxr-xr-x@ 4 javedalam  staff    128 Aug 13 11:51 test
 
$ git branch 
* feature
  master
 
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
 
$ git branch 
  feature
* master
 
$ git branch -r
  origin/DevOps

$ ls -la
total 0
drwxr-xr-x@  2 javedalam  staff   64 Aug 13 12:18 .
drwxr-xr-x@ 11 javedalam  staff  352 Aug 13 12:18 ..

$ git init
Initialized empty Git repository in /Users/javedalam/Documents/git/devops/git-lab/challenges/test/.git/
 
$ git branch

$ pwd
/Users/javedalam/Documents/git/devops/git-lab/challenges/test
 
$ cat >> screw.txt
#!/usr/bin/python

print ()^[[D
^C
$ vim screw.txt 
 
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        screw.txt

nothing added to commit but untracked files present (use "git add" to track)
$ cat screw.txt 
#!/usr/bin/python

print ("cherry-pick")
$ git add .
$ git commit -m 'added a file'
[main (root-commit) 7960915] added a file
 1 file changed, 3 insertions(+)
 create mode 100644 screw.txt
$ git log
commit 7960915d1bd7a51586443d67c310263074234440 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file

$ git branch 
* main
 
$ git branch feature
$ git branch 
  feature
* main

$ git checkout feature 
Switched to branch 'feature'
 
$ git branch 
* feature
  main
 
$ ls -l 
total 8
-rw-r--r--@ 1 javedalam  staff  41 Aug 13 12:20 screw.txt
 
$ vim screw.txt 
 
$ git add .
$ git commit -m 'added a new line'
[feature cc210de] added a new line
 1 file changed, 2 insertions(+)
 
$ git branch 
* feature
  main
 
$ git log
commit cc210debe28a056786f9e4702ada7b41d2e6e38b (HEAD -> feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:25:28 2023 +0530

    added a new line

commit 7960915d1bd7a51586443d67c310263074234440 (main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file
 
$ git branch 
* feature
  main
 
$ git checkout main
Switched to branch 'main'
 
$ ls -la
total 8
drwxr-xr-x@  4 javedalam  staff  128 Aug 13 12:26 .
drwxr-xr-x@ 11 javedalam  staff  352 Aug 13 12:18 ..
drwxr-xr-x@ 12 javedalam  staff  384 Aug 13 12:26 .git
-rw-r--r--@  1 javedalam  staff   41 Aug 13 12:26 screw.txt
 
$ cat screw.txt 
#!/usr/bin/python

print ("cherry-pick")
 
$ git log
commit 7960915d1bd7a51586443d67c310263074234440 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file
 
$ git cherry-pick cc210debe28a056786f9e4702ada7b41d2e6e38b
[main ae6f11e] added a new line
 Date: Sun Aug 13 12:25:28 2023 +0530
 1 file changed, 2 insertions(+)
 
$ git log
commit ae6f11e73c13a0410a459cf39315e471d227bddc (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:25:28 2023 +0530

    added a new line

commit 7960915d1bd7a51586443d67c310263074234440
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file
 
$ cat screw.txt 
#!/usr/bin/python

print ("cherry-pick")

print ("added a new line")
 
$ git checkout feature 
Switched to branch 'feature'
 
$ cat screw.txt 
#!/usr/bin/python

print ("cherry-pick")

print ("added a new line")
 
$ git log
commit cc210debe28a056786f9e4702ada7b41d2e6e38b (HEAD -> feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:25:28 2023 +0530

    added a new line

commit 7960915d1bd7a51586443d67c310263074234440
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file