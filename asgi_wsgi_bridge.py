# file: asgi_wsgi_bridge.py
from a2wsgi import ASGIMiddleware
from my_fastapi_app import asgi_app

# asgi_wsgi_mount.py
def make_fastapi_app(global_conf, **local_conf):
    return ASGIMiddleware(asgi_app)
