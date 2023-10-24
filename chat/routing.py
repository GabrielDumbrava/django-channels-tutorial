from django.urls import re_path
# use re_path due to some limitations of URLRouter
# https://channels.readthedocs.io/en/stable/topics/routing.html#urlrouter

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
