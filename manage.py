import os
import cherrypy
from flask_script import Manager
from flaskapp import flasktemplate, Base, engine


manager = Manager(flasktemplate)


@manager.command
def db():
    Base.metadata.create_all(bind=engine)


@manager.command
def quick(port=8080):
    # Mount the application
    cherrypy.tree.graft(flasktemplate, "/")

    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    # Instantiate a new server object
    server = cherrypy._cpserver.Server()

    # Configure the server object
    server.socket_host = "0.0.0.0"
    server.socket_port = int(port)
    server.thread_pool = 30

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

    # Subscribe this server
    server.subscribe()

    # Example for a 2nd server (same steps as above):
    # Remember to use a different port

    # server2             = cherrypy._cpserver.Server()

    # server2.socket_host = "0.0.0.0"
    # server2.socket_port = 8081
    # server2.thread_pool = 30
    # server2.subscribe()

    # Start the server engine (Option 1 *and* 2)

    try:
        cherrypy.engine.start()
        cherrypy.engine.block()
    except KeyboardInterrupt:
        cherrypy.engine.stop()


@manager.command
def go():
    flasktemplate.run(debug=True, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    manager.run()
