# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('ffsjp.config')
db = SQLAlchemy(app)

from ffsjp import views, models

