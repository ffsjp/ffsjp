# -*- coding: utf-8 -*-

PARAMS = {
    'project_name': 'ffsjp'
}

STRUCTURE = [
    {
        'url': 'index',
        'title': u'Главная'
    },
    {
        'url': 'materials/list',
        'title': u'Материалы'
    },
    {
        'url': 'services',
        'title': u'Сервисы'
    },
    {
        'url': 'games',
        'title': u'Игры'
    }
]

HOME_PATH = '/'

DATABASE = 'ffsjp/data.db'
SECRET_KEY = 'secret key'
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/ffsjp'

