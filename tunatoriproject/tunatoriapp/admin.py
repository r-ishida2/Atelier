from django.contrib import admin
from .models import Publish,Reply,Bookmark
# Register your models here.

class PublishAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_displaylinks = ('id', 'title')
admin.site.register(Publish,PublishAdmin)

admin.site.register(Reply)
admin.site.register(Bookmark)