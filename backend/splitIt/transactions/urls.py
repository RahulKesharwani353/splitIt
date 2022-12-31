from django.urls import path
from .views import *

urlpatterns = [
    path('', ListTransactionView.as_view()),
    path('category/', ListCategoryView.as_view()),
    path('<pk>/', TransactionView.as_view()),
]