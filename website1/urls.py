from website1 import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index")
]
