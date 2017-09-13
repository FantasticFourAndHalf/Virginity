from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


def phone_request(request):
    if request.method == 'POST':
        return HttpResponse("Okay.")
    else:
        return render(request, 'phone.html')
