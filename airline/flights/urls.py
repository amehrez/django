from django.contrib import admin
from django.urls import path, include
from flights import views


urlpatterns = [
 path("", views.index, name="index")
]
