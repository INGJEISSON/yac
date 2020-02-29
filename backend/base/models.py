from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.mongo import connect_mongo
import pandas as pd
import json
class UserProfile(AbstractUser):
    class Meta:
        db_table = "user_profile"

    def __str__(self):
        return str(self.username)


class ChatRoom(models.Model):
    name = models.CharField(max_length=30, blank=False,
                            null=False, unique=True)
    description = models.TextField(
        blank=False, null=False, default="")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def get_users_online(self):
        return UsersChatRoom.objects.filter(active=True, chat_room=self).count()

    def get_chat(self):
        from django.core import serializers
        

        mongo = connect_mongo()
        chat = pd.DataFrame(list(mongo["chat"].find({"chat_id":int(self.id)})))
        chat['index'] = chat.index
        chat = pd.DataFrame(chat, columns= ['id_chat', 'id_user', 'username', 'content', 'send_at', 'index'])
        chat = chat.to_json(orient='records')
        return chat

    class Meta:
        db_table = "chat_room"

    def __str__(self):
        return str(self.name)


class UsersChatRoom(models.Model):
    user = models.ForeignKey(
        UserProfile,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='user_chat_room'
    )
    chat_room = models.ForeignKey(
        ChatRoom,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='room_chat_room'
    )
    active = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        unique_together = (('user', 'chat_room'),)
        db_table = "user_chat_room"

    def __str__(self):
        return str(self.user + " - " + self.chat_room)
