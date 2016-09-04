# -*- coding: utf-8 -*-
import os

__author__ = 'sean'

from baseHandler import BaseHandler
from lib.utils import *


class Distribution_Handler(BaseHandler):
    def get(self):
        self.distribution()

    def post(self):
        self.distribution()

    def distribution(self):
        distri_app_path = (os.path.join(os.path.dirname(__file__))) + "/../" + DISTRI_APP_PATH
        if self.request.headers['User-Agent'].find("iPhone") >= 0:
            devicetype = 'ios'
        elif self.request.headers['User-Agent'].find("Android") >= 0:
            devicetype = 'android'
        else:
            devicetype = 'desktop'
        if SSL_OPEN:
            server = "https://" + SERVER_IP
        else:
            server = "http://" + SERVER_IP + ":" + SERVER_PORT
        if not self.request.arguments.has_key('app') and not self.request.arguments.has_key('type'):
            items = get_apps(distri_app_path)
            self.render("distr_home_page.html", server=server, items=items, devicetype=devicetype)
        else:
            p_name = self.request.arguments['app'][0]
            p_type = self.request.arguments['type'][0]
            app_path = distri_app_path + '/' + p_type + '/' + p_name
            items = get_packages(app_path, p_name, p_type)[0]
            self.render("distr_detail_page.html", server=server, items=items, devicetype=devicetype)
