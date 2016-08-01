# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class ZipCodeModel(db.Model):

    __tablename__ = 'zipcodes'

    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.String, unique=True)
    address = db.Column(db.String)
    neighborhood = db.Column(db.String)
    state = db.Column(db.String(2))
    city = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
