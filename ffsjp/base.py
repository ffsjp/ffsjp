from ffsjp.config import params

class Base:
    title = ''

    def __init__(self, title = ''):
        self.setTitle(title)
    
    def setTitle(self, title):
        self.title = title + ' - ' + params['project_name']

