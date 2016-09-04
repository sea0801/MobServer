from urls import application
from config.config import *


def https_server_main():
    http_server = tornado.httpserver.HTTPServer(application,
                                                ssl_options={
                                                    "certfile": './cert/server.crt',
                                                    "keyfile": './cert/server.key',
                                                })

    http_server.listen(443)
    tornado.ioloop.IOLoop.instance().start()


def http_server_main():
    tornado.options.parse_command_line()
    sockets = bind_sockets(SERVER_PORT, family=socket.AF_INET)
    server = HTTPServer(application, xheaders=True, no_keep_alive=True, idle_connection_timeout=120)
    server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    from tornado.httpserver import HTTPServer
    from tornado.netutil import bind_sockets
    from tornado.options import define, options
    import tornado.ioloop
    import socket

    if SSL_OPEN:
        https_server_main()
    else:
        http_server_main()
