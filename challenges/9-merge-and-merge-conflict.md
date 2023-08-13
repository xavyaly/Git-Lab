[merge link](https://www.javatpoint.com/git-merge-and-merge-conflict)


# MERGE CONFLICT RESOLVE BETWEEN 2 BRANCHES

$ ls -la
total 144
drwxr-xr-x@ 12 javedalam  staff    384 Aug 13 12:47 .
drwxr-xr-x@ 11 javedalam  staff    352 Aug  9 13:12 ..
-rw-r--r--@  1 javedalam  staff   2148 Aug  9 13:12 0-create-repository.md
-rw-r--r--@  1 javedalam  staff     76 Aug  9 13:12 1-Git-Installations.md
-rw-r--r--@  1 javedalam  staff   7107 Aug  9 13:12 2-Conflict-Pull-LifeCycle.md
drwxr-xr-x@  5 javedalam  staff    160 Aug  9 13:12 3-Git-Documents
-rw-r--r--@  1 javedalam  staff  32294 Aug  9 13:12 4-Git-Commands.md
-rw-r--r--@  1 javedalam  staff   7837 Aug 13 12:13 5-git-fork-commands.md
-rw-r--r--@  1 javedalam  staff   3416 Aug 10 12:46 6-pull-requests
-rw-r--r--@  1 javedalam  staff     68 Aug 10 12:50 7-git-branching.md
-rw-r--r--@  1 javedalam  staff   6102 Aug 13 12:33 8-git-cherry-pick.md
-rw-r--r--@  1 javedalam  staff      0 Aug 13 12:47 9-merge-
Javeds-MacBook-Air:challenges javedalam$ 
Javeds-MacBook-Air:challenges javedalam$ touch 9-merge-and-merge-conflict.md
Javeds-MacBook-Air:challenges javedalam$ 
Javeds-MacBook-Air:challenges javedalam$ ls -l
total 144
-rw-r--r--@ 1 javedalam  staff   2148 Aug  9 13:12 0-create-repository.md
-rw-r--r--@ 1 javedalam  staff     76 Aug  9 13:12 1-Git-Installations.md
Javeds-MacBook-Air:challenges javedalam$ mkdir test
Javeds-MacBook-Air:challenges javedalam$ cd test/
$ git init
Initialized empty Git repository in /Users/javedalam/Documents/git/devops/git-lab/challenges/test/.git/
$ 
$ vim file1.txt
$ 
$ git add file1.txt 
$ git commit -m 'new file added'
[main (root-commit) 6ecc54a] new file added
 1 file changed, 1 insertion(+)
 create mode 100644 file1.txt
$ 
$ git branch 
* main
$ git branch feature1
$ git branch feature2
$ git branch 
  feature1
  feature2
* main
$ 
$ git checkout feature1
Switched to branch 'feature1'
$ ls -la
total 8
drwxr-xr-x@  4 javedalam  staff  128 Aug 13 12:49 .
drwxr-xr-x@ 13 javedalam  staff  416 Aug 13 12:48 ..
drwxr-xr-x@ 12 javedalam  staff  384 Aug 13 12:49 .git
-rw-r--r--@  1 javedalam  staff   50 Aug 13 12:49 file1.txt
$ 
$ vim file1.txt 
$ git add file1.txt 
$ git commit -m 'code fix'
[feature1 aede194] code fix
 1 file changed, 3 insertions(+), 1 deletion(-)
$ 
$ git log
commit aede19439d54b88c48cddcb7d074c61d5af677d7 (HEAD -> feature1)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:50:37 2023 +0530

    code fix

commit 6ecc54a80ac5dc75894055e89bcadced597c4ec5 (main, feature2)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:49:17 2023 +0530

    new file added
$ 
$ git branch 
* feature1
  feature2
  main
$ 
$ git feature2
git: 'feature2' is not a git command. See 'git --help'.
$ git checkout feature2
Switched to branch 'feature2'
$ 
$ ls -l
total 8
-rw-r--r--@ 1 javedalam  staff  50 Aug 13 12:51 file1.txt
$ 
$ vim file1.txt 
$ 
$ git add file1.txt 
$ git commit -m 'another line added'
[feature2 1651e75] another line added
 1 file changed, 3 insertions(+), 1 deletion(-)
$ git log
commit 1651e7518e69ae9e34a7dafb94c1391913324e7d (HEAD -> feature2)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:52:50 2023 +0530

    another line added

commit 6ecc54a80ac5dc75894055e89bcadced597c4ec5 (main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:49:17 2023 +0530

    new file added
$ 
$ git branch 
  feature1
* feature2
  main
$ 
$ cat file1.txt 
trying to merge from feature2 to fearure1 branch

added another line  
$ git checkout feature1
Switched to branch 'feature1'
$ cat file1.txt 
trying to merge from feature2 to fearure1 branch

added a new code to fix the issue 
$ 
$ git merge 1651e7518e69ae9e34a7dafb94c1391913324e7d
Auto-merging file1.txt
CONFLICT (content): Merge conflict in file1.txt
Automatic merge failed; fix conflicts and then commit the result.
$ 
$ git checkout feature1
file1.txt: needs merge
error: you need to resolve your current index first
$ 
$ git branch 
* feature1
  feature2
  main
$ git checkout feature2
file1.txt: needs merge
error: you need to resolve your current index first
$ 
$ vim file1.txt 
$ cat file1.txt 
trying to merge from feature2 to fearure1 branch

<<<<<<< HEAD
added a new code to fix the issue 
=======
added another line  
>>>>>>> 1651e7518e69ae9e34a7dafb94c1391913324e7d
$ 
$ vim file1.txt 
$ 
$ vim file1.txt 
$ 
$ git merge 1651e7518e69ae9e34a7dafb94c1391913324e7d
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
$ 
$ vim file1.txt 
$ git add .
$ git commit -m 'merge resolved'
[feature1 9feb5e7] merge resolved
$ 
$ vim file1.txt 
$ 
$ git merge 1651e7518e69ae9e34a7dafb94c1391913324e7d
Already up to date.
$ 
$ vim file1.txt 
$ 
$ git merge 1651e7518e69ae9e34a7dafb94c1391913324e7d
Already up to date.
$ 
$ git status
On branch feature1
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file1.txt

no changes added to commit (use "git add" and/or "git commit -a")
$ git add .
$ git commit -m 'merge resolved'
[feature1 ec71f17] merge resolved
 1 file changed, 1 deletion(-)
$ 
$ git merge 1651e7518e69ae9e34a7dafb94c1391913324e7d
Already up to date.
$ git log
commit ec71f1714ea9989bc76125c35a6ad18d231557b5 (HEAD -> feature1)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 13:01:16 2023 +0530

    merge resolved

commit 9feb5e717af6f574d4268fa24ea69e0f2d420494
Merge: aede194 1651e75
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:59:24 2023 +0530

    merge resolved

commit 1651e7518e69ae9e34a7dafb94c1391913324e7d (feature2)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:52:50 2023 +0530

    another line added

commit aede19439d54b88c48cddcb7d074c61d5af677d7
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:50:37 2023 +0530

    code fix

commit 6ecc54a80ac5dc75894055e89bcadced597c4ec5 (main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:49:17 2023 +0530

    new file added
$ 


# MERGE CONFLICT RESOLVE BETWEEN BRANCH AND MASTER

    $ git merge <branch-name>


# 

