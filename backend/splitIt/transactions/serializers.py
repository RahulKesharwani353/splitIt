from rest_framework import serializers
from .models import Category, Transaction
from friends.serializers import GetUserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    friends = GetUserSerializer(many = True)
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'friends', 'category', 'description', 'amount']

class CreateTransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Transaction
        fields = '__all__'