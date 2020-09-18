import git
import os

os.chdir('../mp4concat')


# class SimpleGit(object):
#     def __init__(self, repo):
#         repo = repo
#

def simple_commit(repo, files, commit_message):
    repo.index.add(files)
    for f in files:
        repo.add
    g.


def main():
    # connect to repo
    try:
        repo = git.Repo('.', search_parent_directories=True)
    except:
        print('fatal: not a git repository (or any of the parent directories): .git')
        exit()

