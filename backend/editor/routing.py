from django.urls import re_path
from editor.consumers import CodeEditorConsumer

websocket_urlpatterns = [
    re_path(r"ws/editor/(?P<room_name>\w+)/$", CodeEditorConsumer.as_asgi()),
]
