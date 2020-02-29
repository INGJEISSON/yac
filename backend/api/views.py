import pandas as pd
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import ChatRoom, UserProfile
from utils.mongo import connect_mongo

from .serializers import (ChatRoomDetailSerializer, ChatRoomListSerializer,
                          MessageSerializer, UserSerializer)


class ChatRoomListAPI(generics.ListCreateAPIView):
    """
    Api for **ChatRoom**
    [GET] Returns a list of all **ChatRoom** or create.
    [POST] Create a **ChatRoom**:
       - params:  
            --"name": "string",
            --"description": "string"

    """
    permission_classes = (permissions.AllowAny,)

    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomListSerializer


class ChatRoomDetailAPI(generics.RetrieveAPIView):
    """
    Api for **ChatRoom** Detail
    [GET] Returns a list of all **ChatRoom** or create.
    """
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'pk'

    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomDetailSerializer


class UserAPI(generics.RetrieveAPIView):
    """
    Retrieve a **User** by (pk)
    - params:  
        --"pk": "string",

    """
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'pk'

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserCreateAPI(generics.CreateAPIView):
    """
    Create a **User**
    - params:  
        --"username": "string",
        --"password": "string",

    """
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'pk'

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    """
    Api for ObtainAuthToken
       - params:  
            --"username": "string",
            --"password": "string"

    """

    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class AddMessage(APIView):
    """
    Api Add Message
       - params:  
            --"ususer_idername": "string"
            --"username": "string"
            --"chat_id": "string"
            --"content": "string"
            --"send_at": "string"

    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
