from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import *
from .models import *
# Create your views here.

class ListTransactionView(APIView):
    def get(self,request):
        user = request.user
        data = Transaction.objects.filter(user = user)
        serializer = TransactionSerializer(data, many = True)
        response_data={
                "data": serializer.data
            }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self,request):
        user = request.user
        data = request.data
        serializer = CreateTransactionSerializer(data = data, context= {
                    'request': request
                })
        if serializer.is_valid():
            serializer.save()
            response_data={
                    "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionView(APIView):
        def patch(self, request, pk):
            obj = Transaction.objects.get(id=pk)
            serializer = CreateTransactionSerializer(obj, data=request.data, partial=True) # set partial=True to update a data partially
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def get(self,request,pk):
            data = Transaction.objects.get(id=pk)
            serializer = TransactionSerializer(data)
            response_data={
                    "data": serializer.data
                }
            return Response(response_data, status=status.HTTP_200_OK)

        def delete(self, request, pk):
            data = Transaction.objects.get(id = pk)
            data.delete()
            response_data={
                    "message": "deleted successfully"
            }
            return Response(response_data, status=status.HTTP_200_OK)
