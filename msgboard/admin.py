from django.contrib import admin
from msgboard.models import Topic, Message

# Register your models here.

class TopicAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "datetime")
	
class MessageAdmin(admin.ModelAdmin):
	list_display = ("__unicode__", "author", "topic", "datetime", "likes")

admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)
