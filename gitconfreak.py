#!/usr/bin/python3
from datetime import datetime
import subprocess as cmd

no_of_commits = 3
commit_message = "random message " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def create_file(commit_number):
    """
    create a file in the root repo,
    probably overwrite when you're creating a new one
    :param commit_number:
    :return:
    """
    f = open("gitconfreak.txt", "w+")
    f.write(f"Commit {commit_number} occurred at "
            + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    f.close()


def commit_changes(commit_msg,cmd):
    """
    commit changes made to file
    :param commit_msg:
    :return:
    """
    cmd.run("git add .", check=True, shell=True)
    cmd.run(f"git commit -m \"{commit_msg}\"", check=True, shell=True)

def push_changes():
    """
    push changes to the repo
    :return:
    """
    cmd.run("git push -u origin master -f", check=True, shell=True)


for i in range(no_of_commits):
    create_file(commit_number=i)
    commit_changes(commit_msg= commit_message, cmd=cmd)

push_changes()