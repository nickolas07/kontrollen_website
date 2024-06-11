from django.urls import path
from . import views

urlpatterns = [
    path('<str:themenbereich>', views.view_aufgaben, name='aufgaben'),
]
