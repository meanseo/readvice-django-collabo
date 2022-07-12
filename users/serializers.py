from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'birth', 'gender')

    def validate(self, data):
        email = data.get('email', None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('user already exists')
        return data

    def create(self, validated_data):
        instance = User.objects.create(**validated_data)
        instance.email = validated_data.pop('email')
        instance.password = validated_data.pop('password')
        instance.username = validated_data.pop('username')
        instance.birth = validated_data.pop('birth')
        instance.gender = validated_data.pop('gender')
        return instance