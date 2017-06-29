from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MessageManager(models.Manager):
	def add_message(self,sender, thread, content):
		return self.create(sender = sender, thread = thread, content = content)

class MessageThread(models.Model):
    subject = models.CharField(max_length = 255, blank = True)
    participants = models.ManyToManyField(User, related_name = 'message_threads')
    when = models.DateTimeField(auto_now_add = True)


class Message(models.Model):
	sender = models.ForeignKey(User, related_name = 'sender')
	thread = models.ForeignKey(MessageThread, related_name = 'thread')
	content = models.TextField()
	when = models.DateTimeField(auto_now_add =True)

	objects = MessageManager()

	def __str__(self):
		return ('sender: {}  thread: {}  content: {}  date: {} \n '.format(self.sender, self.thread, self.content, self.when))

class Profile(models.Model):
	owner = models.OneToOneField(User, related_name = 'owner')
	# message = models.ForeignKey(Message, related_name = '_message')
	thread = models.ForeignKey(MessageThread, related_name = '_thread')
	is_removed = models.BooleanField()

	def __str__(self):
		return ('owner: {}  thread: {} is_removed: {} \n'.format(self.owner, self.thread,self.is_removed))