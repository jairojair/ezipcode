# -*- coding: utf-8 -*-

from invoke import task, run


@task
def clean():
    run("find . -name '*.pyc' -delete")
    run("find . -name '*__pycache__' -delete")
    run("find . -name '.coverage' -delete")


@task
def deps():
    run("pip install -r requirements.txt")


@task(clean)
def tests():
    run("pycodestyle *.py")
    run("python -m unittest tests/*")


@task(clean)
def coverage():
    run("coverage run application/*.py")
    run("coverage report")


@task(deps, clean)
def runserver():
    run("gunicorn --bind 0.0.0.0 --reload --pythonpath application app:app")
