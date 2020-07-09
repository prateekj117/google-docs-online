from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm, UserAuthenticationForm


def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'register.html', context)


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)
