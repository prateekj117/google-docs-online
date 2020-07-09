from django.shortcuts import render


def home(request):
    return render(request, 'navigus_assignment/home.html')
