from django.conf.urls import url
from django.urls import path
from .views import (AddMessage, ChatRoomDetailAPI, ChatRoomListAPI, UserAPI,
                    UserCreateAPI)

urlpatterns = [
    # chat rooms API
    path('chat_rooms/', ChatRoomListAPI.as_view()),
    url('chat_room/(?P<pk>\d+)$', ChatRoomDetailAPI.as_view()),
    url('user/(?P<pk>\d+)$', UserAPI.as_view()),
    url('user/create', UserCreateAPI.as_view()),
    url('message/add', AddMessage.as_view()),
]
