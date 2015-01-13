from flask import render_template
from ffsjp import app
from ffsjp.base import Base

@app.route('/')
def index():
    base = Base(title = 'Home')
    return render_template('index.html', base = base)

@app.errorhandler(404)
def page_not_found(error):
    base = Base(title = '404')
    return render_template('errors/404.html', base = base), 404

