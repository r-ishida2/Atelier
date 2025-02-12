from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import PublishCreationForm, ReplyCreationForm

class IndexView(TemplateView):
    template_name = 'index.html'

class PostView(TemplateView):
    template_name = 'post.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'

class PublishView(FormView):
    template_name = 'publish.html'
    form_class = PublishCreationForm
    success_url = ""

class ReplyView(FormView):
    template_name = 'Reply.html'
    form_class = ReplyCreationForm
    success_url = ""