#! /usr/bin/env python3

from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo('/Users/temporaryadmin/DHTA_Projects/django-blog')
assert not repo.bare