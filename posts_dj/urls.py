from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.lista_posts, name='lista_posts'),
]