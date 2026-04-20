from a2wsgi import WSGIMiddleware
from my_zope_wsgi_app import application as wsgi_app
from starlette.responses import RedirectResponse, PlainTextResponse
from zExceptions import Redirect

class ZopeRedirectCatchMiddleware:
    """
    ASGI middleware to catch Zope Redirect exceptions,
    returning a 302 (or specified) HTTP redirect.

    Because Zope is a special snowflake, we need to catch its Redirect
    exceptions and convert them to proper ASGI responses. This middleware
    does that.

    The Grand Nagus Zek would be proud of this solution, as it allows us
    to integrate Zope's unique behavior and keep the profits flowing.
    """
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        try:
            await self.app(scope, receive, send)
        except Redirect as exc:
            url = exc.args[0] if exc.args else "/"
            status = getattr(exc, "code", 302)
            response = RedirectResponse(url, status_code=status)
            await response(scope, receive, send)
        except Exception as exc:
            # Optional: fallback; you may want logging here
            response = PlainTextResponse("Internal Server Error", status_code=500)
            await response(scope, receive, send)

# Compose your app:
asgi_app = ZopeRedirectCatchMiddleware(WSGIMiddleware(wsgi_app))
