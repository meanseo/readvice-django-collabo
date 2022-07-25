from django.urls import path, include
from books import views

urlpatterns = [
    path(r'search', views.search),
    path(r'add_test', views.add_test),
    path(r'api_book', views.book_api_data),
    path(r'api_book2', views.book_api_data2)
]