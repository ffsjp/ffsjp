# -*- coding: utf-8 -*-
from ffsjp import app

class Base:
    title = ''
    menus = []
    content = ''
    data = []

    def __init__(self, title = ''):
        self.setTitle(title)
        self.menus = []
        for punct in app.config['STRUCTURE']:
            self.menus += [{
                'url': punct['url'],
                'title': punct['title'],
                'active': '',
            }]
    
    def setTitle(self, title):
        self.title = title + ' - ' + app.config['PARAMS']['project_name']
    
    def setActivePunctMenu(self, punct_url):
        i = 0
        for punct in self.menus:
            if punct['url'] == punct_url:
                self.menus[i]['active'] = ' class="active"'
            i += 1
    
    def setPage(self, page):
        self.title = page.title
        self.content = page.content
        self.setActivePunctMenu(page.activeMenu)

    def setData(self, data):
        self.data = data

