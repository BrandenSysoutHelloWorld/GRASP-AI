from django.db import models
from django.contrib.auth.models import User

class PDF(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
