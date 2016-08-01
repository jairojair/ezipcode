# -*- coding: utf-8 -*-

import click

from os import environ
from flask import Flask

from application.models import db
from application.zipcode import ZipCodeResource

app = Flask(__name__)
db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')


ZipCodeResource.add_url_rules(app, rule_prefix='/zipcode/')


@app.cli.command()
def initdb():
    """create database tables"""
    db.create_all()


@app.cli.command()
def resetdb():
    """drop database tables"""
    db.drop_all()
