#! /usr/bin/env python3

from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo('/home/tenaciouscri/django-blog/myblog/')
assert not repo.bare