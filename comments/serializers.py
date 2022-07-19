from rest_framework import serializers

from books.serializers import BookSerializer
from users.serializers import UserSerializer
from .models import Book as book
from .models import User as user
from .models import Comment as comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'

class MypageSerializer(serializers.Serializer):
    comment_id = serializers.CharField()
    comment = serializers.CharField()
    auto_recode = serializers.CharField()
    reg_date = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()
    birth = serializers.CharField()
    gender = serializers.CharField()
    isbn = serializers.CharField()
    author = serializers.CharField()
    book_title = serializers.CharField()
    book_info = serializers.CharField()
    library_name = serializers.CharField()
    price = serializers.CharField()
    category = serializers.CharField()
    book_img = serializers.CharField()

