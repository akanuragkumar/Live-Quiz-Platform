from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

import random
import json
import string

class Quiz(models.Model):
    _owner = models.ForeignKey(User, on_delete=models.CASCADE)
    _quizName = models.CharField(max_length=60)
    _quizDescription = models.TextField(null=True, default=None)
    _dateCreated = models.DateTimeField(auto_now_add=True)


class Session(models.Model):
    _quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    _owner = models.IntegerField(default = -1)
    _sessionID = models.CharField(max_length=6, default='') 
    _hostChannelName = models.CharField(max_length=255)
    _questionCounter = models.IntegerField(default = -1)
    _currentVotes = models.IntegerField(default = 0)


class AnonymousUser(models.Model):
    _session = models.ForeignKey(Session, on_delete=models.CASCADE)
    _userID = models.TextField(max_length = 15, default = '')
    _points = models.IntegerField(default = 0)
    _previousPoints = models.IntegerField(default = 0)
    _previousCorrect = models.BooleanField(default = False)
    _userChannelName = models.CharField(max_length=255)
    

class Question(models.Model):

    _quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    _questionText = models.CharField(max_length=200)
    

class Answer(models.Model):
    _question = models.ForeignKey(Question, on_delete=models.CASCADE)
    _text = models.CharField(max_length=50)
    _correct = models.BooleanField()
    _pointValue = models.IntegerField(default=0)
    _votes = models.IntegerField(default=0)
    _voters = models.ManyToManyField(AnonymousUser)

