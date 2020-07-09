import hashlib

from django.shortcuts import render, redirect


def presence(request):
    if request.user.is_authenticated:
        avatar_url = gravatar(request.user)
        return render(request, 'presence.html', {'avatar_url': avatar_url})
    else:
        return redirect("home")


def gravatar(user, size=50, default='identicon', rating='g'):
    url = 'http://www.gravatar.com/avatar'
    hash = hashlib.md5(user.email.encode('utf-8')).hexdigest()
    return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(url=url, hash=hash, size=size, default=default, rating=rating)
