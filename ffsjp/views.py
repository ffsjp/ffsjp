# -*- coding: utf-8 -*-
from flask import render_template, redirect
from ffsjp import app, db, models
from ffsjp.base import Base

import copy

base = Base()

@app.route('/')
def index():
    base_local = copy.deepcopy(base)
    base_local.setPage(models.Pages.query.filter_by(model='index').first())
    return render_template('index.html', base = base_local)

@app.route('/<page_name>/')
def page(page_name):
    pages_l = ['services', 'games', 'index']
    pages_redirect = ['materials']
    base_local = copy.deepcopy(base)
    if page_name in pages_l:
        base_local.setPage(models.Pages.query.filter_by(model=page_name).first())
        return render_template(page_name + '.html', base = base_local)
    elif page_name in pages_redirect:
        return redirect(app.config['HOME_PATH'] + page_name + '/list/')
    else:
        base_local.setTitle('404 Page not found')
        return render_template('errors/404.html', base = base_local), 404

@app.route('/materials/list/')
@app.route('/materials/list/<cat_name>/')
def materials(cat_name = ''):
    base_local = copy.deepcopy(base)
    base_local.setPage(models.Pages.query.filter_by(model='materials').first())
    category = models.Cat.query.order_by(models.Cat.ord).all()
    this_cat = ''
    if cat_name:
        data = models.Materials.query.filter_by(category = cat_name).order_by(models.Materials.ord).all()
        if data:
            base_local.setData(data)
            this_cat = models.Cat.query.filter_by(name = cat_name).first()
        else:
            return redirect(app.config['HOME_PATH'] + 'materials/list/')
    else:
        base_local.setData(models.Materials.query.order_by(models.Materials.ord).all())
    return render_template('materials.html', base = base_local, category = category, this_cat = this_cat)

@app.errorhandler(404)
def page_not_found(error):
    base_local = copy.deepcopy(base)
    base_local.setTitle('404 Not found')
    return render_template('errors/404.html', base = base_local), 404

