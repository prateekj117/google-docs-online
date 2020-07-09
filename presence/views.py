from django.shortcuts import render, redirect


def presence(request):
    if request.user.is_authenticated:
        return render(request, 'presence.html')
    else:
        return redirect("home")
