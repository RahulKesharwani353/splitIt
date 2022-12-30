
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('hehe/', ProtectedView.as_view()),
     path('register/', RegisterView.as_view()),
    # path('logout/', reg.LogoutView.as_view(), name='logout'),
]
