from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# models
from msgboard.models import Topic, Message

# restricted
def restricted(request):
	template = loader.get_template("msgboard/restricted.html")
	return HttpResponse(template.render(RequestContext(request, {})))

# login action
def loginform(request):
	if request.user.is_authenticated():
		return index(request)
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return index(request)
		else:
			logout(request) # just in case
			return index(request, "Invalid login info.") # request holds knowledge that user is unauthenticated
			
# user registration
def register(request, errorMsg=""):
	template = loader.get_template("msgboard/register.html")
	return HttpResponse(template.render(RequestContext(request, {"errorMsg" : errorMsg})))
	
def registerform(request):
	# check if password and confirmed password match
	if request.POST['password'] != request.POST['re_password']:
		return index(request, "Passwords do not match.")
	# check if name or email is taken
	elif User.objects.filter(username=request.POST['username']).count() + User.objects.filter(email=request.POST['email']).count() > 0:
		return index(request, "The user by that name or email already exists.")
	else:
		user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password']) # auto saves to database
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		login(request, user) # logs in user automatically
		return index(request)

# message board home
def index(request, errorMsg=""):
	template = loader.get_template("msgboard/index.html")
	
	topicList = Topic.objects.order_by('-updated') # get topics from newest updated to oldest
	
	# package in an array of json objects in which each topic is associated with a number of posts
	for x in topicList:
		x.msgCount = Message.objects.filter(topic=x.id).count() # get number of posts for this topic
	
	if request.user.is_authenticated():
		currentUser = request.user
	else:
		currentUser = None
	
	print "currentUser: ", currentUser
	
	context = RequestContext(request, {"topicList" : topicList, "currentUser" : currentUser, "errorMsg" : errorMsg})
	return HttpResponse(template.render(context))

# page for a particular topic
def topic(request, topic_id):
	template = loader.get_template("msgboard/topic.html")
	
	messageList = Message.objects.filter(topic=topic_id).order_by('datetime') # get messages for this topic, from oldest to newest
	
	print messageList
	
	context = RequestContext(request, {"messageList" : messageList, "topicId" : topic_id})
	return HttpResponse(template.render(context))

@login_required
# creating a new topic
def newtopic(request):
	template = loader.get_template("msgboard/newtopic.html")
	return HttpResponse(template.render(RequestContext(request, {})))
	
def newtopicform(request):
	topic = Topic(title=request.POST['title'], author=request.user)
	topic.save()
	message = Message(msgbody=request.POST['msgbody'], author=request.user, topic=topic)
	message.save()
	
	return index(request)

@login_required
# creating a new message for a particular topic
def newmsg(request, topic_id):
	title = Topic.objects.get(id=topic_id).title # get title of the topic
	
	template = loader.get_template("msgboard/newmessage.html")
	context = RequestContext(request, {"topicId" : topic_id, "topicTitle" : title})
	return HttpResponse(template.render(context))
def newmsgform(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	
	message = Message(msgbody=request.POST['msgbody'], author=request.user, topic=topic)
	message.save()
	
	return index(request)
	
