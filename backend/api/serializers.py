from rest_framework import serializers
from bson import json_util
from base.models import ChatRoom, UserProfile
from utils.mongo import connect_mongo
import json


class ChatRoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"

class ChatRoomDetailSerializer(serializers.ModelSerializer):
    get_chat = serializers.JSONField()

    class Meta:
        model = ChatRoom
        fields = ['id', 'get_chat' ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class MessageSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField(max_length=30)
    chat_id = serializers.IntegerField()
    content = serializers.CharField(max_length=300)
    send_at = serializers.CharField(max_length=30)

    def create(self, validated_data):
        data = {
            "user_id": int(validated_data['user_id']),
            "username": validated_data['username'],
            "chat_id": int(validated_data['chat_id']),
            "content": validated_data['content'],
            "send_at": validated_data['send_at'],
        }
        mongo = connect_mongo()
        mongo["chat"].insert_many([data])
        return validated_data
