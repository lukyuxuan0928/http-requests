from handler import *
import wsgiref.simple_server
import tornado.web
import tornado.wsgi

# r"/" == root website address
application = tornado.web.Application([
	(r"/api/do", DoHandler),
])

# Start the server at port n
if __name__ == "__main__":
    try:
        app = tornado.wsgi.WSGIAdapter(application)
        server = wsgiref.simple_server.make_server('', 5124, app)
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    print "Server closed..."