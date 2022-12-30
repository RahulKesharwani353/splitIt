from django.db import models
from django.conf import settings


# Create your models here.
User = settings.AUTH_USER_MODEL
class Friend(models.Model):
    user = models.ForeignKey(User,  related_name='user',on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend', on_delete=models.CASCADE)