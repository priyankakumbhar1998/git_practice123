from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)