$ git
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

$ git init      # initialize an empty git repository

-----------------------------------------------------------------------------------------------------------------

$ ls .git/
HEAD		config		description	hooks		index		info		logs		objects		packed-refs	refs

-----------------------------------------------------------------------------------------------------------------

$ mkdir testing
$ cd testing/
$ ls
$ git init
Initialized empty Git repository in /Users/javedalam/Documents/git/devops/Git-Lab/2023-Git-Commands/testing/.git/
$ ls -la
total 0
drwxr-xr-x  3 javedalam  staff   96 Aug  4 19:40 .
drwxr-xr-x  5 javedalam  staff  160 Aug  4 19:40 ..
drwxr-xr-x  9 javedalam  staff  288 Aug  4 19:40 .git
$ touch testing.txt
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	testing.txt

nothing added to commit but untracked files present (use "git add" to track)

$ git add testing.txt


$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   testing.txt


$ git commit -m "testing file added"
[main (root-commit) 6b1a34e] testing file added
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 testing.txt


$ git status
On branch main
nothing to commit, working tree clean


$ cat >> testing.txt 
hi mam how are you ??
^C


$ cat testing.txt 
hi mam how are you ??


$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   testing.txt

no changes added to commit (use "git add" and/or "git commit -a")


$ git add testing.txt 


$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   testing.txt


$ git restore --staged testing.txt


$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   testing.txt

no changes added to commit (use "git add" and/or "git commit -a")


$ cat testing.txt 
hi mam how are you ??


$ git add testing.txt 


$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   testing.txt


$ git commit -m "testing file modified"
[main cc065e5] testing file modified
 1 file changed, 1 insertion(+)


$ git status
On branch main
nothing to commit, working tree clean

# All commits history stored

$ git log
commit cc065e56c93efc50f219b0bb5c39a3eb988b9792 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 19:57:07 2023 +0530

    testing file modified

commit 6b1a34ea79be72ecc971f404895d9f9d879fb0c5
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 19:50:55 2023 +0530

    testing file added

OR

$ git log --oneline
cc065e5 (HEAD -> main) testing file modified
6b1a34e testing file added

# Play with some more commit 

$ rm testing.txt


$ git status
On branch main
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    testing.txt

no changes added to commit (use "git add" and/or "git commit -a")


$ git add .


$ git commit -m "testing file deleted"
[main e3b3d00] testing file deleted
 1 file changed, 1 deletion(-)
 delete mode 100644 testing.txt


$ git status
On branch main
nothing to commit, working tree clean


$ git log
commit e3b3d007f5861cf6551325ef97e08e7b75cea227 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 20:00:34 2023 +0530

    testing file deleted

commit cc065e56c93efc50f219b0bb5c39a3eb988b9792
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 19:57:07 2023 +0530

    testing file modified

commit 6b1a34ea79be72ecc971f404895d9f9d879fb0c5
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 19:50:55 2023 +0530

    testing file added


# If suppose you wanated to remove the previous commits
# It removes all previous commits 

$ git reset 6b1a34ea79be72ecc971f404895d9f9d879fb0c5
Unstaged changes after reset:
D	testing.txt


$ git log
commit 6b1a34ea79be72ecc971f404895d9f9d879fb0c5 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 19:50:55 2023 +0530

    testing file added


# testing again in untracked file and appearing in red color, not in staging area
$ git status
On branch main
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    testing.txt

no changes added to commit (use "git add" and/or "git commit -a")

# Empty 
$ ls


# testing file starts appearing in green color
$ git add .
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	deleted:    testing.txt


# Add a new file

$ touch testing1.txt

$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	deleted:    testing.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	testing1.txt

$ git add .

$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    testing.txt -> testing1.txt


# Let's add some content and create a new file

$ vim testing1.txt 
$ cat testing1.txt 
hello man, how are you ??

$ touch home.txt
$ ls -la
total 8
drwxr-xr-x   5 javedalam  staff  160 Aug  4 20:34 .
drwxr-xr-x   5 javedalam  staff  160 Aug  4 20:28 ..
drwxr-xr-x  13 javedalam  staff  416 Aug  4 20:33 .git
-rw-r--r--   1 javedalam  staff    0 Aug  4 20:34 home.txt
-rw-r--r--   1 javedalam  staff   26 Aug  4 20:34 testing1.txt

$ git add .
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    testing.txt -> home.txt
	new file:   testing1.txt


# Now i donot want to commit, only I want you to push back and pull when needed

$ git stash 
Saved working directory and index state WIP on main: 6b1a34e testing file added
$ git status
On branch main
nothing to commit, working tree clean
$ git log
commit 6b1a34ea79be72ecc971f404895d9f9d879fb0c5 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 19:50:55 2023 +0530

    testing file added

$ cat testing.txt 
$ ls -la
total 0
drwxr-xr-x   4 javedalam  staff  128 Aug  4 20:37 .
drwxr-xr-x   5 javedalam  staff  160 Aug  4 20:28 ..
drwxr-xr-x  13 javedalam  staff  416 Aug  4 20:37 .git
-rw-r--r--   1 javedalam  staff    0 Aug  4 20:37 testing.txt


# Now pull back all the changes

$ git stash pop
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   home.txt
	new file:   testing1.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    testing.txt

Dropped refs/stash@{0} (54449ca4ac9141d4b3fc276fc08582643201d34e)

$ ls -la
total 8
drwxr-xr-x   5 javedalam  staff  160 Aug  4 20:39 .
drwxr-xr-x   5 javedalam  staff  160 Aug  4 20:28 ..
drwxr-xr-x  14 javedalam  staff  448 Aug  4 20:39 .git
-rw-r--r--   1 javedalam  staff    0 Aug  4 20:39 home.txt
-rw-r--r--   1 javedalam  staff   26 Aug  4 20:39 testing1.txt


# Execute again stash after add 

$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   home.txt
	new file:   testing1.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    testing.txt

$ git add .
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    testing.txt -> home.txt
	new file:   testing1.txt

$ ls -la
total 8
drwxr-xr-x   5 javedalam  staff  160 Aug  4 20:39 .
drwxr-xr-x   5 javedalam  staff  160 Aug  4 20:28 ..
drwxr-xr-x  14 javedalam  staff  448 Aug  4 20:41 .git
-rw-r--r--   1 javedalam  staff    0 Aug  4 20:39 home.txt
-rw-r--r--   1 javedalam  staff   26 Aug  4 20:39 testing1.txt

$ git stash 
Saved working directory and index state WIP on main: 6b1a34e testing file added

$ ls -la
total 0
drwxr-xr-x   4 javedalam  staff  128 Aug  4 20:42 .
drwxr-xr-x   5 javedalam  staff  160 Aug  4 20:28 ..
drwxr-xr-x  13 javedalam  staff  416 Aug  4 20:42 .git
-rw-r--r--   1 javedalam  staff    0 Aug  4 20:42 testing.txt


# Clean the stash 

$ git stash clear
$ ls -la
total 0
drwxr-xr-x   4 javedalam  staff  128 Aug  4 20:42 .
drwxr-xr-x   5 javedalam  staff  160 Aug  4 20:28 ..
drwxr-xr-x  13 javedalam  staff  416 Aug  4 20:43 .git
-rw-r--r--   1 javedalam  staff    0 Aug  4 20:42 testing.txt
$ git stash pop
No stash entries found.

--------------------------------------------------------------------------------------------------------------

# How to create a new repo and push the changes 

# Go to github.com
# Create a repo with any name
# Execute the below command from CLI
# Done

$ git remote add origin <URL>
OR
$ git remote add origin https://github.com/xavyaly/testing.git
$ git remote -v
origin	https://github.com/xavyaly/testing.git (fetch)
origin	https://github.com/xavyaly/testing.git (push)
$ git branch
* main
$ git push origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 218 bytes | 218.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/xavyaly/testing.git
 * [new branch]      main -> main

--------------------------------------------------------------------------------------------------------------

# Branching ??

# Added multiple commits

$ touch file-1.txt
$ git add .
$ git commit -m "adding a file"
[main 389168c] adding a file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 file-1.txt
$ touch file-2.txt
$ git add .
$ git commit -m "adding a file"
[main 101bcbb] adding a file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 file-2.txt
$ touch file-3.txt
$ git add .
$ git commit -m "adding a file"
[main 39c65b5] adding a file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 file-3.txt
$ git log
commit 39c65b504eb940300b66bc89ca9a9901851e5c12 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 09:49:12 2023 +0530

    adding a file

commit 101bcbb88d15e3a637e4c077d7d91978124a5bf5
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 09:49:04 2023 +0530

    adding a file

commit 389168c807f3069bbbd9992c0b3d40411edbf9c8
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 09:48:54 2023 +0530

    adding a file

commit 6b1a34ea79be72ecc971f404895d9f9d879fb0c5 (origin/main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 19:50:55 2023 +0530

    testing file added


--------------------------------------------------------------------------------------------------------------

# Play with it: https://learngitbranching.js.org/

# Never ever push any changes to master or main branch

# Always create a new branch in case to add a new feature 

# how to restrict a user to push any changes to master/main branch ?

# Play with it: https://learngitbranching.js.org/
$ git commit 
$ git commit 
$ git commit 
$ git log 

# What is HEAD ? commit stored in HEAD

# Lets create a new feature branch 
$ git branch feature        # created a new feature branch 
$ git checkout feature      # switched to feature branch 
$ git commit                # feature branch will move, main branch will stopped and commit stored in head instead of master
$ git commit                # feature branch will move, main branch will stopped and commit stored in head instead of master
$ git checkout main         # swithed to main branch, now the HEAD is main branch 
$ git commmit             
$ git branch                # main branch
$ git merge feature         # merge to main branch 
$ git checkout C5
$ git checkout C8
$ git checkout main 

--------------------------------------------------------------------------------------------------------------

# Play locally

$ git log 
commit 39c65b504eb940300b66bc89ca9a9901851e5c12 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 09:49:12 2023 +0530

    adding a file

commit 101bcbb88d15e3a637e4c077d7d91978124a5bf5
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 09:49:04 2023 +0530

    adding a file

commit 389168c807f3069bbbd9992c0b3d40411edbf9c8
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 09:48:54 2023 +0530

    adding a file

commit 6b1a34ea79be72ecc971f404895d9f9d879fb0c5 (origin/main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 19:50:55 2023 +0530

    testing file added
$ 
$ git remote -v
origin	https://github.com/xavyaly/testing.git (fetch)
origin	https://github.com/xavyaly/testing.git (push)

$ ls -la
total 0
drwxr-xr-x   7 javedalam  staff  224 Aug  5 09:49 .
drwxr-xr-x   5 javedalam  staff  160 Aug  4 21:19 ..
drwxr-xr-x  13 javedalam  staff  416 Aug  5 10:19 .git
-rw-r--r--   1 javedalam  staff    0 Aug  5 09:48 file-1.txt
-rw-r--r--   1 javedalam  staff    0 Aug  5 09:48 file-2.txt
-rw-r--r--   1 javedalam  staff    0 Aug  5 09:49 file-3.txt
-rw-r--r--   1 javedalam  staff    0 Aug  4 20:42 testing.txt

$ git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 600 bytes | 600.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/xavyaly/testing.git
   6b1a34e..39c65b5  main -> main


# Cross check in main branch -> all files suppose to push on remote

# HEAD has been changed
$ git log
commit 39c65b504eb940300b66bc89ca9a9901851e5c12 (HEAD -> main, origin/main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 09:49:12 2023 +0530

    adding a file

commit 101bcbb88d15e3a637e4c077d7d91978124a5bf5
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 09:49:04 2023 +0530

    adding a file

commit 389168c807f3069bbbd9992c0b3d40411edbf9c8
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 09:48:54 2023 +0530

    adding a file

commit 6b1a34ea79be72ecc971f404895d9f9d879fb0c5
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 19:50:55 2023 +0530

    testing file added

--------------------------------------------------------------------------------------------------------------

# FORK, CLONE, UPSTREAM

# fork this: https://github.com/xavyaly/advanced-terraform-3099246

$ git clone https://github.com/xavyaly/advanced-terraform-3099246.git

# UPSTREAM -> forked from different peoples clone URL 

$ cd advanced-terraform-3099246/
$ ls
CONTRIBUTING.md	LICENSE		NOTICE		README.md	gcp_commands.md	main.tf
$ git remote add upstream https://github.com/xavyaly/advanced-terraform-3099246.git

$ git remote -v
origin	https://github.com/xavyaly/advanced-terraform-3099246.git (fetch)
origin	https://github.com/xavyaly/advanced-terraform-3099246.git (push)
upstream	https://github.com/xavyaly/advanced-terraform-3099246.git (fetch)
upstream	https://github.com/xavyaly/advanced-terraform-3099246.git (push)

--------------------------------------------------------------------------------------------------------------

# NEW BRANCH, COMMIT, CHECKOUT, HEAD POINTS TO FEATURE BRANCH 

$ git branch 
* main
$ git branch feature        # CREATED A NEW BRANCH 
$ git branch                # LIST THE LOCAL BRANCHES
  feature
* main
$ git checkout feature      # SWITCH TO FEATURE BRANCH, HEAD POINTS TO FEATURE NOW 
Switched to branch 'feature'
$ ls -la
total 96
drwxr-xr-x  11 javedalam  staff    352 Aug  5 10:33 .
drwxr-xr-x@  7 javedalam  staff    224 Aug  5 10:33 ..
drwxr-xr-x  12 javedalam  staff    384 Aug  5 12:58 .git
drwxr-xr-x   6 javedalam  staff    192 Aug  5 10:33 .github
-rw-r--r--   1 javedalam  staff    158 Aug  5 10:33 .gitignore
-rw-r--r--   1 javedalam  staff    635 Aug  5 10:33 CONTRIBUTING.md
-rw-r--r--   1 javedalam  staff   6648 Aug  5 10:33 LICENSE
-rw-r--r--   1 javedalam  staff  16760 Aug  5 10:33 NOTICE
-rw-r--r--   1 javedalam  staff   2753 Aug  5 10:33 README.md
-rw-r--r--   1 javedalam  staff    720 Aug  5 10:33 gcp_commands.md
-rw-r--r--   1 javedalam  staff   2710 Aug  5 10:33 main.tf
$ vim README.md               # ADDED A NEW LINE
$ git status
On branch feature
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
$ git add .
$ git commit -m "added new line"              # COMMIT ID GENERATED
[feature b14afe1] added new line
 1 file changed, 1 insertion(+)
$ git log
commit b14afe17db8cb2bbb612092878ac261302bfd9be (HEAD -> feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 12:58:51 2023 +0530

    added new line

commit 93825cfe6c5ccd69e4cb95fd0fed9110c5e46d1e (origin/main, origin/HEAD, main)
Author: Steven Moser <mellotronplayer@gmail.com>
Date:   Thu Jan 19 14:44:29 2023 -0800

    Update NOTICE

commit d668802c9b482cabf8e372fade8c17c01c242658
Author: Steven Moser <mellotronplayer@gmail.com>
Date:   Thu Jan 19 14:42:11 2023 -0800

    Update README.md

............
............
............

--------------------------------------------------------------------------------------------------------------

# PUSH, BRANCH, RAISE PR: PULL REQUEST, ADD REVIEWEE, REVIEW, SUGGEST COMMENT, MERGE THE CHANGES TO MAIN BRNACH 

$ git status
On branch feature
nothing to commit, working tree clean
$ git branch 
* feature
  main
$ git push origin feature 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 287 bytes | 287.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'feature' on GitHub by visiting:
remote:      https://github.com/xavyaly/advanced-terraform-3099246/pull/new/feature
remote: 
To https://github.com/xavyaly/advanced-terraform-3099246.git
 * [new branch]      feature -> feature

# VISIT github.com
# A POP WILL APPEAR -> COMPARE & PULL REQUEST
# CROSS CKECK THE BASE AND HEAD REPOS BEFORE RAISING THE PR 
# ADD THE REVIEWER
# CLICK ON "CREATE PULL REQUESTS"

# MAIL TRIGGERED TO REVIEWERS AND YOU
# REVIEWER REVIEWS THE CODE
# CROSS CHECK THE "FILE CHANGED" -> COMPARE THE FILES
# ADD THR COMMENTS IF REQUIRED
# MAIL TRIGGERED TO YOU
# IF REQUIRED, END USER RE-RAISE THE PR IF REQUIRED FOR CODE CHANGES
# MAIL TRIGGERED

# REVIEWER RE-REVIEW THE CODE
# CLOSE THE PR WITH PROPER COMMENTS IF SATISFIED
# MERGE THE CHANGES TO MAIN 
# MAIL TRIGGERED

# IF CONFLICTS, WE HAVE ANOTHER STORY 


# LETS ADD ANOTHER FILE AND TRY TO RAISE A NEW PR

$ ls -la
total 96
drwxr-xr-x  11 javedalam  staff    352 Aug  5 12:58 .
drwxr-xr-x@  7 javedalam  staff    224 Aug  5 10:33 ..
drwxr-xr-x  13 javedalam  staff    416 Aug  5 13:07 .git
drwxr-xr-x   6 javedalam  staff    192 Aug  5 10:33 .github
-rw-r--r--   1 javedalam  staff    158 Aug  5 10:33 .gitignore
-rw-r--r--   1 javedalam  staff    635 Aug  5 10:33 CONTRIBUTING.md
-rw-r--r--   1 javedalam  staff   6648 Aug  5 10:33 LICENSE
-rw-r--r--   1 javedalam  staff  16760 Aug  5 10:33 NOTICE
-rw-r--r--   1 javedalam  staff   2754 Aug  5 12:58 README.md
-rw-r--r--   1 javedalam  staff    720 Aug  5 10:33 gcp_commands.md
-rw-r--r--   1 javedalam  staff   2710 Aug  5 10:33 main.tf
$ touch xyz.txt
$ git status
On branch feature
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	xyz.txt

nothing added to commit but untracked files present (use "git add" to track)
$ git add .
$ git commit -m "test"
[feature f2ed3d0] test
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 xyz.txt
$ git log
commit f2ed3d045cc1e0427a6e6e83cfa449c5645808b7 (HEAD -> feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 13:22:06 2023 +0530

    test

commit b14afe17db8cb2bbb612092878ac261302bfd9be (origin/feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 12:58:51 2023 +0530

    added new line

commit 93825cfe6c5ccd69e4cb95fd0fed9110c5e46d1e (origin/main, origin/HEAD, main)
Author: Steven Moser <mellotronplayer@gmail.com>
Date:   Thu Jan 19 14:44:29 2023 -0800

    Update NOTICE

..............
..............
..............

$ git push 
fatal: The current branch feature has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin feature

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

$ git push --set-upstream origin feature
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 265 bytes | 265.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/xavyaly/advanced-terraform-3099246.git
   b14afe1..f2ed3d0  feature -> feature
branch 'feature' set up to track 'origin/feature'.


# NOTE:
# IF END USER PUSH A CHANGES IN SAME PR, THEN COMMITS COUNT INCREASES NOT PR COUNT
# TEAM LEAD NEED TO GO THROUGH EACH COMMIT INDIVIDUALLY, REVIEW THE CODE AND MERGE THE CHANGES 


# FOR REFERENCE: 
https://github.com/facebook/react-native/pulls
# 305 OPEN AND 13,180 CLOSED 


--------------------------------------------------------------------------------------------------------------

# UNSTAGED, RESET

# LET'S REMOVE THE LATEST COMMIT ID, COPY ONE LEVEL BELOW COMMIT ID
$ git status
On branch feature
Your branch is up to date with 'origin/feature'.

nothing to commit, working tree clean

$ git log
commit f2ed3d045cc1e0427a6e6e83cfa449c5645808b7 (HEAD -> feature, origin/feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 13:22:06 2023 +0530

    test

.............

$ git reset b14afe17db8cb2bbb612092878ac261302bfd9be
$ git log
commit b14afe17db8cb2bbb612092878ac261302bfd9be (HEAD -> feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 12:58:51 2023 +0530

    added new line

commit 93825cfe6c5ccd69e4cb95fd0fed9110c5e46d1e (origin/main, origin/HEAD, main)
Author: Steven Moser <mellotronplayer@gmail.com>
Date:   Thu Jan 19 14:44:29 2023 -0800

    Update NOTICE

commit d668802c9b482cabf8e372fade8c17c01c242658
Author: Steven Moser <mellotronplayer@gmail.com>
Date:   Thu Jan 19 14:42:11 2023 -0800

    Update README.md

..........
..........

$ git status
On branch feature
Your branch is behind 'origin/feature' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	xyz.txt

nothing added to commit but untracked files present (use "git add" to track)

$ git add .
$ git stash
Saved working directory and index state WIP on feature: b14afe1 added new line
$ git status
On branch feature
Your branch is behind 'origin/feature' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean

$ git push 
To https://github.com/xavyaly/advanced-terraform-3099246.git
 ! [rejected]        feature -> feature (non-fast-forward)
error: failed to push some refs to 'https://github.com/xavyaly/advanced-terraform-3099246.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

$ git status
On branch feature
Your branch is behind 'origin/feature' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean

$ git log 
commit b14afe17db8cb2bbb612092878ac261302bfd9be (HEAD -> feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 12:58:51 2023 +0530

    added new line

commit 93825cfe6c5ccd69e4cb95fd0fed9110c5e46d1e (origin/main, origin/HEAD, main)
Author: Steven Moser <mellotronplayer@gmail.com>
Date:   Thu Jan 19 14:44:29 2023 -0800

    Update NOTICE

commit d668802c9b482cabf8e372fade8c17c01c242658
Author: Steven Moser <mellotronplayer@gmail.com>
Date:   Thu Jan 19 14:42:11 2023 -0800

    Update README.md

............
............

# FORCE PUSH COZ ONLINE REPO CONTAIN A COMMIT WHERE AS MY LOCAL DOESN'T 

$ git push origin feature -f
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/xavyaly/advanced-terraform-3099246.git
 + f2ed3d0...b14afe1 feature -> feature (forced update)

# REFRESH https://github.com/LinkedInLearning/advanced-terraform-3099246/pull/6/commits
# COMMIT IS GONE NOW

# CHANGES REVIEWED
# MERGE THIS PR 
# CHANGES MERGED

--------------------------------------------------------------------------------------------------------------

# SYNC WITH FORK REPOS, FETCH, PRUNE 

# ONLINE HAS 16 COMMITS WHERE AS IN LOCAL
# https://github.com/xavyaly/advanced-terraform-3099246/commits/main -> 16 COMMITS 
# LOCAL HAS ALSO 16 COMMITS BUT IN SOME CASE IF LOCAL HAS LESS COMMITS AS COMPARED TO ONLINE COMMITS, FOLLOW BELOW COMMANDS

# 2 WAYS 

# FIRST WAY MANUALLY AND SECOND WAY THORUGH UI

# FIRST WAY
$ git branch 
* feature
  main
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'. 
$ git log
commit 93825cfe6c5ccd69e4cb95fd0fed9110c5e46d1e (HEAD -> main, upstream/main, origin/main, origin/HEAD)
Author: Steven Moser <mellotronplayer@gmail.com>
Date:   Thu Jan 19 14:44:29 2023 -0800

    Update NOTICE

commit d668802c9b482cabf8e372fade8c17c01c242658
Author: Steven Moser <mellotronplayer@gmail.com>
Date:   Thu Jan 19 14:42:11 2023 -0800

    Update README.md

commit 2e426b80a76c2055de99b3bd93a43198fc1429ab
Merge: d12522c b723854
Author: Dave Swersky <dswersky@gmail.com>
Date:   Thu Nov 17 15:35:35 2022 -0600

    Merge pull request #1 from dswersky/main
    
    Merge main branch pls

commit b7238545e8c325345b7eea3a3206f343466566f0
Author: dswersky <dswersky@gmail.com>
Date:   Tue Nov 15 10:22:55 2022 -0600

    added web tag to NGINX proxy

commit bd2f30d4fdb7a217a1313ec2164af9a2b72e3cfa
Author: dswersky <dswersky@gmail.com>
Date:   Tue Nov 8 09:56:09 2022 -0600

    added service enable commands to gcp_commands

commit da3c9ad30862cd95bd0acfbcc4e9de1c97c894c5
Author: dswersky <dswersky@gmail.com>
Date:   Tue Oct 11 13:37:34 2022 -0500

    added comment to replace project-id

commit 9c7ccf3a56e72eb061081eb50a1c6b63e6120c37
Author: dswersky <dswersky@gmail.com>
Date:   Fri Sep 30 11:30:06 2022 -0500

    added access_config to nginx

commit cfd504a713ae5727aab67ecfbed3c16a946cb427
Author: dswersky <dswersky@gmail.com>
Date:   Fri Sep 30 11:28:14 2022 -0500

    removed access_config

commit b6184b053a6412a7471747c04bab3efca792bf21
Author: dswersky <dswersky@gmail.com>
Date:   Wed Sep 14 13:43:12 2022 -0500

    removed unnecessary comments

commit a8b4756705684240adc76f6431f7ddd55e978ed0
Author: dswersky <dswersky@gmail.com>
Date:   Wed Sep 14 13:41:18 2022 -0500

    removed project attribute from VPC data resource

commit 34da7777d951a8b24e6487ffaaf0b8882f5bfe82
Author: dswersky <dswersky@gmail.com>
Date:   Wed Sep 14 11:45:37 2022 -0500

    First config deploy successful

commit 83219c5410c23df41d4fc3bc2df349bbafe8e1a6
Author: dswersky <dswersky@gmail.com>
Date:   Wed Sep 7 14:14:16 2022 -0500

    Added database VM and default VPC data source

commit 6163836297cadba119feda1c18db367e4bf9a683
Author: dswersky <dswersky@gmail.com>
Date:   Thu Sep 1 14:43:53 2022 -0500

    First commit of main.tf

commit 8304a62842919192dd6687baf711eee83dc25ffe
Author: dswersky <dswersky@gmail.com>
Date:   Thu Sep 1 10:23:37 2022 -0500

    test commit

commit d12522c801931fb5c54d353ce3b6a265f6963e95
Author: cmosier-LiL <88352515+cmosier-LiL@users.noreply.github.com>
Date:   Mon Aug 29 10:01:26 2022 -0700

    Update README.md

commit 56a21a49c43f25470c18a561121165c0cd4f5623
Author: cmosier-LiL <88352515+cmosier-LiL@users.noreply.github.com>
Date:   Mon Aug 29 10:01:00 2022 -0700

    Initial commit

$ ls -la
total 96
drwxr-xr-x  11 javedalam  staff    352 Aug  5 13:52 .
drwxr-xr-x@  7 javedalam  staff    224 Aug  5 10:33 ..
drwxr-xr-x  14 javedalam  staff    448 Aug  5 13:52 .git
drwxr-xr-x   6 javedalam  staff    192 Aug  5 10:33 .github
-rw-r--r--   1 javedalam  staff    158 Aug  5 10:33 .gitignore
-rw-r--r--   1 javedalam  staff    635 Aug  5 10:33 CONTRIBUTING.md
-rw-r--r--   1 javedalam  staff   6648 Aug  5 10:33 LICENSE
-rw-r--r--   1 javedalam  staff  16760 Aug  5 10:33 NOTICE
-rw-r--r--   1 javedalam  staff   2753 Aug  5 13:52 README.md
-rw-r--r--   1 javedalam  staff    720 Aug  5 10:33 gcp_commands.md
-rw-r--r--   1 javedalam  staff   2710 Aug  5 10:33 main.tf

$ git fetch --all --prune 
Fetching origin
Fetching upstream
From https://github.com/xavyaly/advanced-terraform-3099246
 * [new branch]      feature    -> upstream/feature
 * [new branch]      main       -> upstream/main

$ ls -la | wc
      12     101     675

$ git reset --hard upstream/main
HEAD is now at 93825cf Update NOTICE

# EXECUTE 
$ git log             # SHOULD LIST ALL THE COMMITS SAME LIKE REMOTE, IN MY CASE IT IS DIFFERENT

-----------------------------------------------------------------------------------------------------------------

# MERGE CONFLICT, SQUASHING YOUR COMMIT

