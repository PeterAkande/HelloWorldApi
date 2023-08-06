from django.contrib import admin
from django.urls import path

from hello_world_variety.views import just_helloworld, call_helloworld

urlpatterns = [
    path('', just_helloworld),
    path('shout/', call_helloworld),
]
