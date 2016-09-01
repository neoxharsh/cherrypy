import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return  "Hello World"

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 80})
    cherrypy.quickstart(HelloWorld())
