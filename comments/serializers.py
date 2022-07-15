from rest_framework import serializers
from .models import Comment as comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    book = serializers.CharField(read_only=True)
    class Meta:
        model = comment
        fields = '__all__'