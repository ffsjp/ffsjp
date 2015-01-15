# -*- coding: utf-8 -*-
from flask import render_template
from ffsjp import app
from ffsjp.base import Base

import copy

base = Base()

@app.route('/')
def index():
    base_local = copy.deepcopy(base)
    base_local.setTitle(u'Главная')
    base_local.setActivePunctMenu('index')
    return render_template('index.html', base = base_local)

@app.route('/services')
def services():
    base_local = copy.deepcopy(base)
    base_local.setTitle(u'Сервисы')
    base_local.setActivePunctMenu('services')
    return render_template('services.html', base = base_local)

@app.route('/games')
def games():
    base_local = copy.deepcopy(base)
    base_local.setTitle(u'Игры')
    base_local.setActivePunctMenu('games')
    return render_template('games.html', base = base_local)

@app.errorhandler(404)
def page_not_found(error):
    base_local = base
    base_local.setTitle('404 Not found')
    return render_template('errors/404.html', base = base), 404

