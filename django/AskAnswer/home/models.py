from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class Question(models.Model):
    questionID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    plusVotes = models.IntegerField(default=0)
    minusVotes = models.IntegerField(default=0)
    time = models.DateTimeField(default=datetime.now)
    categories = models.CharField(max_length=500)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Answer(models.Model):
    body = models.CharField(max_length=1000)
    time = models.DateTimeField(default=datetime.now)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)