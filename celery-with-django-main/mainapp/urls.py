
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('websocket/', views.WebsocketWay.as_view(), name="wb"),
    path('http/', views.HttpWay.as_view(), name="hp"),
]

