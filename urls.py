import tornado.web
from handlers.distribution_handler import Distribution_Handler
from handlers.baseHandler import BaseHandler
from settings import settings

application = tornado.web.Application([
    (r"/favicon.ico",
     tornado.web.StaticFileHandler,
     dict(path=settings['static_path'])),
    (r"/ui/(.*)",
     tornado.web.StaticFileHandler,
     dict(path=settings['ui_path'])),
    (r"/distri_apps/(.*)",
     tornado.web.StaticFileHandler,
     dict(path=settings['distri_apps'])),
    (r"/distribution", Distribution_Handler),
    (r".*", BaseHandler),

], **settings)
