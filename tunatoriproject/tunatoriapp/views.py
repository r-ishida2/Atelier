from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import PublishCreationForm, ReplyCreationForm
from .models import Article


class IndexView(TemplateView):
    template_name = 'index.html'
    context_object_name = 'object_list'

    queryset = Article.objects.all().order_by('-id')

    paginate_by =9


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