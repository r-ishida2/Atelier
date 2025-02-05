from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class PostView(TemplateView):
    template_name = 'post.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'