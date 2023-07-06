from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('games', views.games, name='games'),
    path('space', views.space, name='space'),
]
