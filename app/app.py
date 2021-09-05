import cherrypy

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 5000,
        'server.thread_pool': 8,
        'server.max_request_body_size': 0,
        'server.socket_timeout': 60
    }
}

class application:
    @cherrypy.expose
    def index(self):
        return "Hello World!"
        
    @cherrypy.expose
    def info(self):
        return """Method 'add' will take two parameter 'num1', 'num2' and give addition of num1 and num2.<br><br>
        """

    @cherrypy.expose
    def add(self, num1=2,num2=2):
        return "The addition of first number {} and second number {} is equal to {}".format(num1, num2, int(num1)+int(num2))


if __name__ == '__main__':
    cherrypy.quickstart(application(), '', config)
