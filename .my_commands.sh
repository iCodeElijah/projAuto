#!/bin/bash

function create(){

    cd
    python3 create.py $1
    cd /home/elabs/Downloads/myProjects/$1
    git init
    git remote add origin git@github.com:iCodeElijah/$1.git
    touch README.md
    git add .
    git commit -m"First Commit"
    git push -u origin master
    code .

}

# source ~/.my_commands.sh