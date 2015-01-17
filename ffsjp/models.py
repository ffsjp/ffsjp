# -*- coding: utf-8 -*-
from ffsjp import db

class Pages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    model = db.Column(db.Text)
    url = db.Column(db.String(20), index = True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    anons = db.Column(db.Text)
    keywords = db.Column(db.Text)
    level = db.Column(db.Integer)
    activeMenu = db.Column(db.Text)

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), index = True, unique = True)
    title = db.Column(db.String(80))
    ord = db.Column(db.Integer)
    mat = db.relationship('Materials', backref = 'cat', lazy = 'dynamic')

class Materials(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    url = db.Column(db.Text)
    category = db.Column(db.String(40), db.ForeignKey('cat.name'))
    anons = db.Column(db.Text)
    ord = db.Column(db.Integer)

