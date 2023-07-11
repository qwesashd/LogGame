from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('games', views.games, name='games'),
    path('space', views.space, name='space'),
    path('login', views.login, name='login'),
    path('reg', views.reg, name='reg'),
    path('error', views.error, name='error'),
    path('support', views.support, name='support'),
    path('send', views.send, name='send'),

]
