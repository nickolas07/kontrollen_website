from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_kontrollen, name='kontrollen'),
    path('pdf/<str:identifier>/', views.view_pdf, name='view_pdf'),
    path('download/<str:identifier>/', views.download_pdf, name='download_pdf'),
    path('probe/<str:identifier>/', views.kontrolle_erstellen, name='kontrolle_erstellen'),
    path('erstellen/<str:identifier>/', views.kontrolle_erstellen_konfigo, name='kontrolle_erstellen'),
    path('erstellen/<str:identifier>/<str:aufgaben>/', views.kontrolle_erstellen_konfigo, name='kontrolle_erstellen_konfigo'),
]
