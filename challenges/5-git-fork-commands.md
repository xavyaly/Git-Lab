# FORK, CLONE, CHECKOUT, UPSTREAM, LOCAL/REMOTE BRANCH DELETE


ahfkjfhshfdjk

total 16
drwxr-xr-x@  4 javedalam  staff  128 Aug  6 15:09 Architectures
drwxr-xr-x@  6 javedalam  staff  192 Aug  6 19:29 Lambda-Lab
-rw-r--r--@  1 javedalam  staff   63 Aug  9 15:48 README.md
drwxr-xr-x  11 javedalam  staff  352 Aug  5 13:52 advanced-terraform-3099246
drwxr-xr-x@  5 javedalam  staff  160 Aug  8 22:57 aws-boto3
drwxr-xr-x@  4 javedalam  staff  128 Aug  9 16:25 aws-cli
drwxr-xr-x@  5 javedalam  staff  160 Aug  9 15:52 aws-core
drwxr-xr-x@ 11 javedalam  staff  352 Aug  7 15:20 bash-lab
drwxr-xr-x@ 11 javedalam  staff  352 Aug  9 13:12 git-lab
drwxr-xr-x   5 javedalam  staff  160 Aug  8 20:42 projects
drwxr-xr-x@  7 javedalam  staff  224 Aug  9 11:55 python-lab
-rwxr-xr-x@  1 javedalam  staff  207 Aug  7 12:40 repo.sh
drwxr-xr-x@  5 javedalam  staff  160 Aug  7 20:22 terraform-lab
Javeds-MacBook-Air:devops javedalam$ git clone https://github.com/xavyaly/game-of-life.git
Cloning into 'game-of-life'...
remote: Enumerating objects: 9222, done.
remote: Total 9222 (delta 0), reused 0 (delta 0), pack-reused 9222
Receiving objects: 100% (9222/9222), 17.57 MiB | 5.92 MiB/s, done.
Resolving deltas: 100% (5619/5619), done.
Javeds-MacBook-Air:devops javedalam$ 
Javeds-MacBook-Air:devops javedalam$ cd game-of-life/
$ ls -l
total 64
-rw-r--r--@  1 javedalam  staff   3093 Aug 10 12:07 README.markdown
drwxr-xr-x@  5 javedalam  staff    160 Aug 10 12:07 gameoflife-acceptance-tests
drwxr-xr-x@  4 javedalam  staff    128 Aug 10 12:07 gameoflife-build
drwxr-xr-x@  9 javedalam  staff    288 Aug 10 12:07 gameoflife-core
drwxr-xr-x@  3 javedalam  staff     96 Aug 10 12:07 gameoflife-deploy
drwxr-xr-x@ 10 javedalam  staff    320 Aug 10 12:07 gameoflife-web
-rw-r--r--@  1 javedalam  staff     50 Aug 10 12:07 infinitest.filters
-rw-r--r--@  1 javedalam  staff  22300 Aug 10 12:07 pom.xml
$ 
$ git branch
* master
$ 
$ git branch testing 
$ git branch 
* master
  testing
$ git checkout testing 
Switched to branch 'testing'
$ git branch 
  master
* testing
$ 
$ ls -l 
total 64
-rw-r--r--@  1 javedalam  staff   3093 Aug 10 12:07 README.markdown
drwxr-xr-x@  5 javedalam  staff    160 Aug 10 12:07 gameoflife-acceptance-tests
drwxr-xr-x@  4 javedalam  staff    128 Aug 10 12:07 gameoflife-build
drwxr-xr-x@  9 javedalam  staff    288 Aug 10 12:07 gameoflife-core
drwxr-xr-x@  3 javedalam  staff     96 Aug 10 12:07 gameoflife-deploy
drwxr-xr-x@ 10 javedalam  staff    320 Aug 10 12:07 gameoflife-web
-rw-r--r--@  1 javedalam  staff     50 Aug 10 12:07 infinitest.filters
-rw-r--r--@  1 javedalam  staff  22300 Aug 10 12:07 pom.xml
$ 
$ vi README.markdown 
$ git status
On branch testing
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.markdown

no changes added to commit (use "git add" and/or "git commit -a")
$ git add .
$ git commit "blank line added "
error: pathspec 'blank line added ' did not match any file(s) known to git
$ git commit -m "blank line added"
[testing 3ec60c0] blank line added
 1 file changed, 1 insertion(+)
$ 
$ git push 
fatal: The current branch testing has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin testing

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

$ 
$ git push --set-upstream origin testing 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 291 bytes | 291.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'testing' on GitHub by visiting:
remote:      https://github.com/xavyaly/game-of-life/pull/new/testing
remote: 
To https://github.com/xavyaly/game-of-life.git
 * [new branch]      testing -> testing
branch 'testing' set up to track 'origin/testing'.
$ 
$ git branch 
  master
* testing
$ 
$ git branch -v
  master  c24bb1a Merge pull request #198 from GeraldScott/master
* testing 3ec60c0 blank line added
$ 
$ git branch --delete testing 
error: Cannot delete branch 'testing' checked out at '/Users/javedalam/Documents/git/devops/game-of-life'
$ 
$ git checkout master 
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
$ git branch 
* master
  testing
$ git branch --delete testing 
warning: deleting branch 'testing' that has been merged to
         'refs/remotes/origin/testing', but not yet merged to HEAD.
Deleted branch testing (was 3ec60c0).
$ 
$ git branch 
* master
$ git branch -v
* master c24bb1a Merge pull request #198 from GeraldScott/master
$ git branch -r
  origin/HEAD -> origin/master
  origin/continuous-delivery
  origin/continuous-delivery-demo
  origin/feature-history
  origin/feature-new-look-and-feel
  origin/game-history-feature
  origin/gameoflife-release-.1
  origin/gameoflife-release-1.0.1
  origin/gameoflife-release-1.0.10
  origin/gameoflife-release-1.0.11
  origin/gameoflife-release-1.0.12
  origin/gameoflife-release-1.0.13
  origin/gameoflife-release-1.0.14
  origin/gameoflife-release-1.0.15
  origin/gameoflife-release-1.0.16
  origin/gameoflife-release-1.0.19
  origin/gameoflife-release-1.0.2
  origin/gameoflife-release-1.0.20
  origin/gameoflife-release-1.0.22
  origin/gameoflife-release-1.0.23
  origin/gameoflife-release-1.0.24
  origin/gameoflife-release-1.0.25
  origin/gameoflife-release-1.0.26
  origin/gameoflife-release-1.0.27
  origin/gameoflife-release-1.0.28
  origin/gameoflife-release-1.0.29
  origin/gameoflife-release-1.0.3
  origin/gameoflife-release-1.0.30
  origin/gameoflife-release-1.0.31
  origin/gameoflife-release-1.0.32
  origin/gameoflife-release-1.0.33
  origin/gameoflife-release-1.0.34
  origin/gameoflife-release-1.0.35
  origin/gameoflife-release-1.0.36
  origin/gameoflife-release-1.0.37
  origin/gameoflife-release-1.0.4
  origin/gameoflife-release-1.0.8
  origin/gameoflife-release-1.0.9
  origin/integration-branch
  origin/master
  origin/releases
  origin/tdd-labs
  origin/tdd-training
  origin/testing
$ 
$ git push origin --delete testing 
To https://github.com/xavyaly/game-of-life.git
 - [deleted]         testing
$ 
$ git branch -r
  origin/HEAD -> origin/master
  origin/continuous-delivery
  origin/continuous-delivery-demo
  origin/feature-history
  origin/feature-new-look-and-feel
  origin/game-history-feature
  origin/gameoflife-release-.1
  origin/gameoflife-release-1.0.1
  origin/gameoflife-release-1.0.10
  origin/gameoflife-release-1.0.11
  origin/gameoflife-release-1.0.12
  origin/gameoflife-release-1.0.13
  origin/gameoflife-release-1.0.14
  origin/gameoflife-release-1.0.15
  origin/gameoflife-release-1.0.16
  origin/gameoflife-release-1.0.19
  origin/gameoflife-release-1.0.2
  origin/gameoflife-release-1.0.20
  origin/gameoflife-release-1.0.22
  origin/gameoflife-release-1.0.23
  origin/gameoflife-release-1.0.24
  origin/gameoflife-release-1.0.25
  origin/gameoflife-release-1.0.26
  origin/gameoflife-release-1.0.27
  origin/gameoflife-release-1.0.28
  origin/gameoflife-release-1.0.29
  origin/gameoflife-release-1.0.3
  origin/gameoflife-release-1.0.30
  origin/gameoflife-release-1.0.31
  origin/gameoflife-release-1.0.32
  origin/gameoflife-release-1.0.33
  origin/gameoflife-release-1.0.34
  origin/gameoflife-release-1.0.35
  origin/gameoflife-release-1.0.36
  origin/gameoflife-release-1.0.37
  origin/gameoflife-release-1.0.4
  origin/gameoflife-release-1.0.8
  origin/gameoflife-release-1.0.9
  origin/integration-branch
  origin/master
  origin/releases
  origin/tdd-labs
  origin/tdd-training
$ 
