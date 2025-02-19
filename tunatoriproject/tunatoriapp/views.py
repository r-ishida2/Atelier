from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView,CreateView
from .forms import PublishCreationForm, ReplyCreationForm
from datetime import datetime
from django.urls import reverse_lazy
from .models import Publish

class IndexView(TemplateView):
    template_name = 'index.html'

class PostView(TemplateView):
    template_name = 'post.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'

class PublishView(CreateView):
    template_name = 'publish.html'
    form_class = PublishCreationForm
    success_url = reverse_lazy("tunatoriapp:index")
    def form_valid(self, form):
        data = form.save(commit=False)
        data.user_id = self.request.user
        data.at_post = datetime.now()
        data.save()
        return super().form_valid(form)

class ReplyView(CreateView):
    template_name = 'Reply.html'
    form_class = ReplyCreationForm
    success_url = reverse_lazy("tunatoriapp:index")
    def form_valid(self, form):
        data = form.save(commit=False)
        publish_id = self.kwargs.get('publish_id')
        data.publish_id = Publish.objects.get(id=publish_id)
        data.user_id = self.request.user
        data.at_reply = datetime.now()
        data.save()
        return super().form_valid(form)