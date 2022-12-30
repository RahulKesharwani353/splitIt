import uuid

from django.db import models
from django.contrib.auth.models import User

# class Token(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     token = models.UUIDField(default=uuid.uuid4, primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True)

# def create_token(user):
#     token = Token.objects.create(user=user)
#     return token.token

# def delete_token(token):
#     Token.objects.filter(token=token).delete()

# def is_valid(token):
#     return Token.objects.filter(token=token).exists()
