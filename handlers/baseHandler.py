#-*- coding: utf-8 -*-

__author__ = 'sean'

import tornado

class BaseHandler(tornado.web.RequestHandler):

    def __init__(self,application, request,**kwargs):
        super(BaseHandler,self).__init__(application,request)

    def get(self):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('errors/404.html',page=None)
        else:
            self.render('errors/unknown.html',page=None)