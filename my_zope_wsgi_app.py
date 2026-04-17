# file: my_zope_wsgi_app.py
from Zope2.Startup.run import make_wsgi_app

application = make_wsgi_app(
    global_config={},
    zope_conf='zope/etc/zope.conf',
)