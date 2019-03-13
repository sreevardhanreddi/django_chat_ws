from django.urls import path, include
from chat.views import *


urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
