from django.urls import path, include
from comments import views

urlpatterns = [
    path(r'', views.comments),
    path(r'query/test', views.query_test)
]