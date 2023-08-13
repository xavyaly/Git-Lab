# git cherry-pick 

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
$ 
$ git branch 
* feature
  master
$ 
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
$ 
$ git branch 
  feature
* master
$ 
$ git branch -r
  origin/DevOps
Javeds-MacBook-Air:test javedalam$ ls -la
total 0
drwxr-xr-x@  2 javedalam  staff   64 Aug 13 12:18 .
drwxr-xr-x@ 11 javedalam  staff  352 Aug 13 12:18 ..
Javeds-MacBook-Air:test javedalam$ git init
Initialized empty Git repository in /Users/javedalam/Documents/git/devops/git-lab/challenges/test/.git/
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git branch
Javeds-MacBook-Air:test javedalam$ pwd
/Users/javedalam/Documents/git/devops/git-lab/challenges/test
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ cat >> screw.txt
#!/usr/bin/python

print ()^[[D
^C
Javeds-MacBook-Air:test javedalam$ vim screw.txt 
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        screw.txt

nothing added to commit but untracked files present (use "git add" to track)
Javeds-MacBook-Air:test javedalam$ cat screw.txt 
#!/usr/bin/python

print ("cherry-pick")
Javeds-MacBook-Air:test javedalam$ git add .
Javeds-MacBook-Air:test javedalam$ git commit -m 'added a file'
[main (root-commit) 7960915] added a file
 1 file changed, 3 insertions(+)
 create mode 100644 screw.txt
Javeds-MacBook-Air:test javedalam$ git log
commit 7960915d1bd7a51586443d67c310263074234440 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git branch 
* main
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git branch feature
Javeds-MacBook-Air:test javedalam$ git branch 
  feature
* main
Javeds-MacBook-Air:test javedalam$ git checkout feature 
Switched to branch 'feature'
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git branch 
* feature
  main
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ ls -l 
total 8
-rw-r--r--@ 1 javedalam  staff  41 Aug 13 12:20 screw.txt
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ vim screw.txt 
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git add .
Javeds-MacBook-Air:test javedalam$ git commit -m 'added a new line'
[feature cc210de] added a new line
 1 file changed, 2 insertions(+)
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git branch 
* feature
  main
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git log
commit cc210debe28a056786f9e4702ada7b41d2e6e38b (HEAD -> feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:25:28 2023 +0530

    added a new line

commit 7960915d1bd7a51586443d67c310263074234440 (main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git branch 
* feature
  main
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git checkout main
Switched to branch 'main'
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ ls -la
total 8
drwxr-xr-x@  4 javedalam  staff  128 Aug 13 12:26 .
drwxr-xr-x@ 11 javedalam  staff  352 Aug 13 12:18 ..
drwxr-xr-x@ 12 javedalam  staff  384 Aug 13 12:26 .git
-rw-r--r--@  1 javedalam  staff   41 Aug 13 12:26 screw.txt
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ cat screw.txt 
#!/usr/bin/python

print ("cherry-pick")
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git log
commit 7960915d1bd7a51586443d67c310263074234440 (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git cherry-pick cc210debe28a056786f9e4702ada7b41d2e6e38b
[main ae6f11e] added a new line
 Date: Sun Aug 13 12:25:28 2023 +0530
 1 file changed, 2 insertions(+)
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git log
commit ae6f11e73c13a0410a459cf39315e471d227bddc (HEAD -> main)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:25:28 2023 +0530

    added a new line

commit 7960915d1bd7a51586443d67c310263074234440
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ cat screw.txt 
#!/usr/bin/python

print ("cherry-pick")

print ("added a new line")
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git checkout feature 
Switched to branch 'feature'
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ cat screw.txt 
#!/usr/bin/python

print ("cherry-pick")

print ("added a new line")
Javeds-MacBook-Air:test javedalam$ 
Javeds-MacBook-Air:test javedalam$ git log
commit cc210debe28a056786f9e4702ada7b41d2e6e38b (HEAD -> feature)
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:25:28 2023 +0530

    added a new line

commit 7960915d1bd7a51586443d67c310263074234440
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 13 12:21:21 2023 +0530

    added a file
Javeds-MacBook-Air:test javedalam$ 