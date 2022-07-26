from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('isbn', 'author', 'book_title', 'category', 'book_img')
        model = Book
