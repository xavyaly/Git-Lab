Javeds-MacBook-Air:2023-Git-Commands javedalam$ pwd
/Users/javedalam/Documents/git/devops/Git-Lab/2023-Git-Commands
Javeds-MacBook-Air:2023-Git-Commands javedalam$ ls
1-Git-Installations	2-Git-Commands.md	testing
Javeds-MacBook-Air:2023-Git-Commands javedalam$ ls -l
total 64
-rw-r--r--  1 javedalam  staff      0 Aug  4 19:35 1-Git-Installations
-rw-r--r--@ 1 javedalam  staff  32294 Aug  5 14:05 2-Git-Commands.md
drwxr-xr-x  7 javedalam  staff    224 Aug  5 09:49 testing
Javeds-MacBook-Air:2023-Git-Commands javedalam$ vim 1-Git-Installations 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   1-Git-Installations

no changes added to commit (use "git add" and/or "git commit -a")
Javeds-MacBook-Air:2023-Git-Commands javedalam$ ls -la
total 72
drwxr-xr-x   5 javedalam  staff    160 Aug  6 11:47 .
drwxr-xr-x  11 javedalam  staff    352 Aug  4 19:34 ..
-rw-r--r--   1 javedalam  staff     76 Aug  6 11:47 1-Git-Installations
-rw-r--r--@  1 javedalam  staff  32294 Aug  5 14:05 2-Git-Commands.md
drwxr-xr-x   7 javedalam  staff    224 Aug  5 09:49 testing
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git add 1-Git-Installations 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git commit -m "added python installation link"
[master 62a1c35] added python installation link
 1 file changed, 3 insertions(+)
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git branch 
* master
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git push 
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 402 bytes | 402.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/xavyaly/Git-Lab.git
   0baf3fb..62a1c35  master -> master
Javeds-MacBook-Air:2023-Git-Commands javedalam$ 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ vim 1-Git-Installations 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   1-Git-Installations

no changes added to commit (use "git add" and/or "git commit -a")
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git add 1-Git-Installations 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git commit -m "added new line"
[master c329e55] added new line
 1 file changed, 1 insertion(+)
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git push 
To https://github.com/xavyaly/Git-Lab.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/xavyaly/Git-Lab.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git pull
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), 800 bytes | 114.00 KiB/s, done.
From https://github.com/xavyaly/Git-Lab
   62a1c35..f42a32a  master     -> origin/master
Auto-merging 2023-Git-Commands/1-Git-Installations
CONFLICT (content): Merge conflict in 2023-Git-Commands/1-Git-Installations
error: could not apply c329e55... added new line
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply c329e55... added new line
Javeds-MacBook-Air:2023-Git-Commands javedalam$ cat 1-Git-Installations 
# Download git on Mac, Windows or Linux/Unix

<<<<<<< HEAD
# ....
=======
>>>>>>> c329e55 (added new line)

https://git-scm.com/downloads
Javeds-MacBook-Air:2023-Git-Commands javedalam$ vim 1-Git-Installations 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git status
interactive rebase in progress; onto f42a32a
Last command done (1 command done):
   pick c329e55 added new line
No commands remaining.
You are currently rebasing branch 'master' on 'f42a32a'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
	both modified:   1-Git-Installations

no changes added to commit (use "git add" and/or "git commit -a")
Javeds-MacBook-Air:2023-Git-Commands javedalam$ 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git log
commit f42a32aa51c677704325c76bc74cc4961af537b8 (HEAD, origin/master, origin/HEAD)
Author: Javed Alam <wellboy.alam13@gmail.com>
Date:   Sun Aug 6 11:55:40 2023 +0530

    added python installation link
    
    Added a link to install python for multiple OS

commit 62a1c354c35197128a84808ae4b4c6b3aaab5375
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sun Aug 6 11:52:12 2023 +0530

    added python installation link

commit 0baf3fbafbb8f654a928531fc3a39a2a23bc49ed
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Sat Aug 5 14:06:31 2023 +0530

    git commands

commit a50dc148a46eba62504dd59c4cde56135713750c
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 21:17:36 2023 +0530

    git commands

commit 5f81b61de21bd807ac22e022e541f44533006aba
Author: Javed Alam <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 21:07:10 2023 +0530

    Update 2-Git-Commands.md

commit f24ab4b5994bb61231cfb4a7bf9cf7e90ebb5750
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Fri Aug 4 21:05:19 2023 +0530

    git commands

commit 614f0104e6c4d1a25deec8edbe1831b327197d42
Author: xavyaly <wellboy.alam13@gmail.com>
Date:   Thu Nov 4 03:42:15 2021 +0000

Javeds-MacBook-Air:2023-Git-Commands javedalam$ git add .
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git commit -m "fix the conflict"
interactive rebase in progress; onto f42a32a
Last command done (1 command done):
   pick c329e55 added new line
No commands remaining.
You are currently rebasing branch 'master' on 'f42a32a'.
  (all conflicts fixed: run "git rebase --continue")

nothing to commit, working tree clean
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git push
fatal: You are not currently on a branch.
To push the history leading to the current (detached HEAD)
state now, use

    git push origin HEAD:<name-of-remote-branch>

Javeds-MacBook-Air:2023-Git-Commands javedalam$ git rebase --continue
Successfully rebased and updated refs/heads/master.
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git push
Everything up-to-date
Javeds-MacBook-Air:2023-Git-Commands javedalam$ vim 1-Git-Installations 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
Javeds-MacBook-Air:2023-Git-Commands javedalam$ vim 1-Git-Installations 
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   1-Git-Installations

no changes added to commit (use "git add" and/or "git commit -a")
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git add 1-Git-Installations ; git commit -m "fix conflicts"
[master 9227dfe] fix conflicts
 1 file changed, 2 deletions(-)
Javeds-MacBook-Air:2023-Git-Commands javedalam$ git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 387 bytes | 387.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/xavyaly/Git-Lab.git
   f42a32a..9227dfe  master -> master
Javeds-MacBook-Air:2023-Git-Commands javedalam$ 
