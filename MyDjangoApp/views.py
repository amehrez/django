from django.http import HttpResponse
from django.shortcuts import render
from numpy.core.defchararray import capitalize


# Create your views here.
def index(request):
    return render(request, "MyDjangoApp/index.html")

def greet(request, name):
    return render(request, "MyDjangoApp/greet.html", {
        "name": name.capitalize()
    })
