# IPAVe (IP Address Visualizer) How Do I Work With You?

# Get setup

1. create a directory named t25 *(this is for everyone's convenience in finding the repo after it's been downloaded)*
1. cd into your t25 directory
1. Log into your github.com account using a web browser
1. navigate to [here](https://github.com/mobycoder001/IPAVe/)
1. clone this repository *(it looks alot like the class repository (go to the next step))*
1. cd to t25/IPAVe/ *(Look for the README.md file (this is the project summary file))*
1. checkout the branch dev
1. from dev, create a branch with "your_name" (this has all the thing we are working on, make your changes here)
> git checkout -b "your_name_here"
1. do a git branch -a -v (you'll see you have the same hash number for your branch and the currentproject branch)
> git branch -a -v
1. checkout your branch: git checkout "your_name_here"
> git checkout "your_name_here"
1. make changes, commit, change, push, pull, whatever 'till your heart is content
1. git pull (get any upstream changes)
1. git push (send your changes to your branch on github)
1. Let someone in the project slack channel know you've got some code to be reviewed ( @channel "hey I pushed code" // there's a slack plugin for that right?)
1. git checkout dev
1. git merge dev (fix any merge conflicts)
1. git push when merge conflicts are resolved
1. git checkout "your_name", continue to work and make changes in your project
> git checkout "your_name_here"
1. commit your changes to the branch
1. git push


### how to submit code to this repo (members)?  
Create a pull request from your currentproject branch **note I think once I add you to this project you won't have to fork it, so get me your "git name"!

#### alternate workflow
- **insert after step 8** *(skip this section if it sounds complex, just make changes in the branch **currentproject** )*

### how to submit code to this repo (other contributers)?  
1. Create a fork of this repository
1. Create a branch with "your_name_here" or "feature_name_here"
1. Make changes
1. add, commit, pull, push changes from your repository
1. Request a pull request via github

### How to we submit code to the class repo?
1. The build master will merge the *dev* branch into the master branch, at regular intervals the a request will be submitted via the slack channel for Instructor1 and Instructor2 will be asked to take a look at the master branch (we all have copies of this code on our machines)
1. Instructor1 and Instructor2 can also see all of our code on a direct link to this repo or via a cloning of the repository to thier local machines

*notes:
* we all haove both repos, we will see our published changes in the class repo and our working changes in the currentproject in this repo
* This seems complex?  Why do it this way?
  - By doing this in a separate fork/repository, we can commit and share code as often as we like without waiting for a pull request to see each others commits (if we use the class repo, we're going to be waiting on a pull request, we use our own repos, it's going to be extremely difficult to review each others changes)


# I'm excited to get going and conribute code! What's next?
- send me an @username slack message with your git ID and asking to be added to the mobycoder001 group
> "Hi my name is "your_name_here" and my git ID is "git_id", I' like to join and contribute to your project, please add me to your org


# environment setup
- see environment setup in this repo / 00_env_setup/README.md

Am I working on environment setup or just munging data files?
- That's up to you where you contribue, some people will pull data, some will munge data, some will present data, we can do it!
