from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class morning_entry(models.Model):
    date = models.DateField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()


class evening_entry(models.Model):
    date = models.DateField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()


class anchor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()
