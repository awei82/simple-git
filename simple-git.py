import git
import os
import sys


# class SimpleGit(object):
#     def __init__(self, repo):
#         repo = repo
#

g = git.Git()

def simple_commit(repo, files, commit_message):
    repo.index.add(files)
    for f in files:
        repo.add(f)


def check_status():
    """Runs 'git status' to check if we're in a git repo. Exit if not."""
    try:
        g.status()
    except:
        print('fatal: Not a git repository (or any of the parent directories): .git', file=sys.stderr)
        exit(-1)


def main():
    # check that we're in a git repo - check_status() exits if not.
    check_status()


    print(g.status())


if __name__ == "__main__":
    main()

