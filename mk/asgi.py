"""
ASGI config for mk project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mk.settings')

djang_asgi_app = get_asgi_application()

from chatApp import routing

application = ProtocolTypeRouter(
  {
    "http": djang_asgi_app,
    "websocket": AllowedHostsOriginValidator(
      AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
    )
  }
)