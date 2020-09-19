import git
import os
import sys


# class SimpleGit(object):
#     def __init__(self, repo):
#         repo = repo
#

g = git.Git()

def simple_commit(files, commit_message):
    """ Add files, create a commit, and push changes to origin"""
    for f in files:
        g.add(f)

    try:
        print(g.commit(message=commit_message))
    except:
        print('commit error', file=sys.stderr)
        exit(-1)


    # push
    # if branch exists at origin, just push
    # otherwise, run 'push -u origin new_branch
    try:
        print(g.push())
    except:
        print('push error', file=sys.stderr)
        exit(-1)

    print(f'simple_commit succeeded commit to branch {repo.active_branch.name}')




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

    # connect to repo
    try:
        global repo
        repo = git.Repo('.', search_parent_directories=True)
    except:
        print('fatal: not a git repository (or any of the parent directories): .git')
        exit()

    print('test')


if __name__ == "__main__":
    main()

