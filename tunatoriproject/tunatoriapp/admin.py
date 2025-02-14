from django.contrib import admin
from .models import Publish,Reply
# Register your models here.

class PublishAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_displaylinks = ('id', 'name')
admin.site.register(Publish,PublishAdmin)

admin.site.register(Reply)