from rest_framework import serializers
from .models import *
from django.conf import settings
from django.contrib.auth.models import User


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email')

class AddFriendSerializer(serializers.ModelSerializer):
    class Meta:
         model = Friend
         fields = ('user','friend')

class FriendSerializer(serializers.ModelSerializer):
    friend = GetUserSerializer(many = False)
    class Meta:
        model = Friend
        fields = ('friend')

