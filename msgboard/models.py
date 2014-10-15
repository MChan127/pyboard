from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

def getNow():
	return datetime.now

class Topic(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User)
	datetime = models.DateTimeField(editable=False, default=getNow())
	updated = models.DateTimeField(editable=False, default=getNow())
	def __unicode__(self):
		return self.title
	
class Message(models.Model):
	msgbody = models.CharField(max_length=1000)
	author = models.ForeignKey(User)
	topic = models.ForeignKey(Topic)
	datetime = models.DateTimeField(editable=False, default=datetime.now)
	likes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.msgbody[:50] + '...'
