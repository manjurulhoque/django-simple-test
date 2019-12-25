from django.urls import path

from .views import *

urlpatterns = [
    path('values', all_values),
]
