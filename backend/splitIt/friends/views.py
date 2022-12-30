from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.
class AddFriendsView(APIView):
    def post(self, request):
        serializer = FriendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data={
                "message":"added succesfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListFriendsView(APIView):
    def get(self, request):
        User = request.user
        friends = Friend.objects.filter(user = User)
        serializer = FriendSerializer(friends, many=True)
        response_data={
                "data": serializer.data
            }
        return Response(response_data, status=status.HTTP_200_OK)

class ListAllUsersView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        user = User.objects.all()
        serializer = GetUserSerializer(user, many=True)
        response_data={
                "data": serializer.data
            }
        return Response(response_data, status=status.HTTP_200_OK)