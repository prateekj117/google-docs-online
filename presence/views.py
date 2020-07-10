import hashlib
import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels.generic.websocket import WebsocketConsumer
from channels_presence.models import Room, Presence
from channels_presence.signals import presence_changed
from django.dispatch import receiver
from django.shortcuts import render, redirect

from authentication.models import User


channel_layer = get_channel_layer()


def presence(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        data = []
        for user in users:
            user_last_seen = {
                user.email: user.last_login
            }
            data.append(user_last_seen)
        return render(request, 'presence.html', {'users_last_seen': data})
    else:
        return redirect("home")


def gravatar(user, size=50, default='identicon', rating='g'):
    url = 'https://www.gravatar.com/avatar'
    hash = hashlib.md5(user.email.encode('utf-8')).hexdigest()
    return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(url=url, hash=hash, size=size, default=default, rating=rating)


class CheckPresence(WebsocketConsumer):

    def connect(self):
        print('connect')
        super().connect()
        Room.objects.add("viewing_docs", self.channel_name, self.scope["user"])
        print(Room.objects.all())

    def disconnect(self, close_code):
        print('Disconnect')
        Room.objects.remove("viewing_docs", self.channel_name)
        print(Room.objects.all())

    def receive(self, text_data=None, bytes_data=None):
        if text_data == '"heartbeat"':
            print(text_data)
            Presence.objects.touch(self.channel_name)
        print(Room.objects.all())

    def forward_message(self, event):
        """
        Utility handler for messages to be broadcasted to groups.  Will be
        called from channel layer messages with `"type": "forward.message"`.
        """
        self.send(event["message"])


@receiver(presence_changed)
def broadcast_presence(sender, room, **kwargs):

    users_info = []

    for user in room.get_users():

        user_info = {
            'avatar_url': gravatar(user), 'name': user.first_name + ' ' + user.last_name,
            'username': user.username, 'email': user.email
        }
        users_info.append(user_info)

    channel_layer_message = {
       "type": "forward.message",
       "message": json.dumps(users_info)
    }

    async_to_sync(channel_layer.group_send)(room.channel_name, channel_layer_message)
