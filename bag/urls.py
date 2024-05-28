# Description: This file contains the URL patterns for the bag app.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
         
]