from django.conf.urls import url
from chat.consumers import ChatConsumer, roomlistConsumer


websocket_urls = [
    url(r'^ws/roomlist/$', roomlistConsumer.as_asgi()),
    url(r'^ws/chat/(?P<group_id>\d+)/$', ChatConsumer.as_asgi()),
    #url(r'^ws/middleware/$', MyMiddlewareConsumer),
]