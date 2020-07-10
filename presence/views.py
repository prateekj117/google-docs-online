import hashlib

from django.shortcuts import render, redirect

from channels.generic.websocket import WebsocketConsumer
from channels_presence.models import Room, Presence


def presence(request):
    if request.user.is_authenticated:
        avatar_url = gravatar(request.user)
        return render(request, 'presence.html', {'avatar_url': avatar_url,
                                                 'username': request.user.username,
                                                 'email': request.user.email,
                                                 'name': request.user.first_name + ' ' + request.user.last_name
                                                 })
    else:
        return redirect("home")


def gravatar(user, size=50, default='identicon', rating='g'):
    url = 'http://www.gravatar.com/avatar'
    hash = hashlib.md5(user.email.encode('utf-8')).hexdigest()
    return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(url=url, hash=hash, size=size, default=default, rating=rating)


class CheckPresence(WebsocketConsumer):

    def connect(self):
        super().connect()
        Room.objects.add("viewing_docs", self.channel_name, self.scope["user"])
        print(Room.objects.all())

    def disconnect(self, close_code):
        Room.objects.remove("viewing_docs", self.channel_name)
        print(Room.objects.all())

    def receive(self, text_data=None, bytes_data=None):
        Presence.objects.touch(self.channel_name)
        print(Room.objects.all())
