from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from datetime import datetime, timedelta

class Question(models.Model):
    questionID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    time = models.DateTimeField(default=datetime.now)
    categories = models.CharField(max_length=500)
    answered = models.IntegerField(default=0)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('question', kwargs={'pk': self.pk})

    def is_recent(self):
        if self.time + timedelta(hours=2) >= timezone.now():
            return True
        return False

    def __str__(self):
        return self.title + ' - ' + str(self.username)

class Answer(models.Model):
    body = models.CharField(max_length=1000)
    time = models.DateTimeField(default=datetime.now)
    plusVotes = models.IntegerField(default=0)
    minusVotes = models.IntegerField(default=0)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)

    def _get_average_votes(self):
        return self.plusVotes - self.minusVotes
    average_votes = property(_get_average_votes)

    def __str__(self):
        return self.body