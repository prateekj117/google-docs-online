from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from .views import CheckPresence

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)

    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^connect/$", CheckPresence)
        ])
    ),
})
