# -*- coding: utf-8 -*-
from ffsjp.config import *

class Base:
    title = ''
    menus = []

    def __init__(self, title = ''):
        self.setTitle(title)
        self.menus = []
        for punct in STRUCTURE:
            self.menus += [{
                'url': punct['url'],
                'title': punct['title'],
                'active': '',
            }]
    
    def setTitle(self, title):
        self.title = title + ' - ' + PARAMS['project_name']
    
    def setActivePunctMenu(self, punct_url):
        i = 0
        for punct in self.menus:
            if punct['url'] == punct_url:
                self.menus[i]['active'] = ' class="active"'
            i += 1

