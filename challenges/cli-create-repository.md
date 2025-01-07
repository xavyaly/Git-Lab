# Create a new repository through UI: https://docs.github.com/en/get-started/quickstart/create-a-repo
<!-- 
In the upper-right corner of any page, use the drop-down menu, and select New repository.
Type a short, memorable name for your repository. ...
Optionally, add a description of your repository. ...
Choose a repository visibility. ...
Select Initialize this repository with a README.
Click Create repository.
 -->

---------------------------------------------------------------------------------------------

# Create a new repository through CLI

Steps:

In the upper-right corner of any page, use the drop-down menu, and select New repository.
Type a short, memorable name for your repository. ...
Click on "create repository"

$ echo "<repo-name>" >> README.md

$ git init
Initialized empty Git repository in /Users/javedalam/Documents/git/devops/.git/

$ git add README.md 

$ git commit -m "first commit"
[main (root-commit) 421c233] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

$ git branch -M main

$ git remote add origin https://github.com/xavyaly/<repo-name>.git

$ git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 221 bytes | 221.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/xavyaly/repo-name.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

$ git clone https://github.com/xavyaly/repo-name.git
Cloning into 'aws-sdk'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

# Remove the repo if not needed
# Go to setting and remove 
# Your repository "xavyaly/<repo-name>" was successfully deleted.

---------------------------------------------------------------------------------------------

# Shell Script -> repo.sh

echo "<repo-name>" >> README.md
git init
git add README.md 
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/xavyaly/<repo-name>.git
git push -u origin main