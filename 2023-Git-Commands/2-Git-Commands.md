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











-----------------------------------------------------------------------------------------------------------------

