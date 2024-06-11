from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('notFound/', views.not_found, name='nicht_gefunden'),
    path('<str:identifier>/', views.view_kontrolle, name='view_kontrolle'),
    path('delete/<str:name>/', views.delete, name='delete'),
]
