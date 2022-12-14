import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from chat import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "safe_earth.settings")

application = ProtocolTypeRouter(
    {
        "http":get_asgi_application(),
        "websocket":AuthMiddlewareStack(
            URLRouter(routing.websocket_urlpatterns)
        )
    }
)
