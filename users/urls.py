from django.urls import path, include
from users import views

urlpatterns = [
    path('join', views.users),
    path('login', views.login),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]
