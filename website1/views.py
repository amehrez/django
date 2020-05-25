from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
        return render(request, "website1/index.html",{
            "newyear": datetime.month == 1 and datetime.day == 1
        })
