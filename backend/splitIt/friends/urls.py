
from django.urls import path
from .views import *

urlpatterns = [
    path('', ListAllUsersView.as_view()),
    path('add-friends/', AddFriendsView.as_view(), name='add-friends'),
    path('my-friends/', ListFriendsView.as_view()),
]