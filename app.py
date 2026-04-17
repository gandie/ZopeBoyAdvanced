# file: app.py
from a2wsgi import WSGIMiddleware
from my_zope_wsgi_app import application as wsgi_app

asgi_app = WSGIMiddleware(wsgi_app)
