from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('teste', teste, name="teste"),
    path('forms', forms, name="forms"),
]


