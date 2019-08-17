# users/serializers.py
from rest_framework import serializers
from .models import User
from django.http import JsonResponse


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:

        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        if not User.objects.filter(email=validated_data['email']).first():
            user = super(UserSerializer, self).create(validated_data)
            user.set_password(validated_data['password'])
            user.username=validated_data['email']
            user.email = validated_data['email']
            user.save()
            return user
        return JsonResponse({'test':'test'})