from django.contrib import admin
from django.urls import path
from .views import  index,nepal

urlpatterns = [
    path('' , index ),
    path('nepal/', nepal, name="nepal")
]
