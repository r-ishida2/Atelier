from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView,CreateView
from .forms import PublishCreationForm, ReplyCreationForm
from datetime import datetime
from django.urls import reverse_lazy

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

class ReplyView(FormView):
    template_name = 'Reply.html'
    form_class = ReplyCreationForm
    success_url = ""



from django.views.generic import ListView
from django.db.models import Q # get_queryset()用に追加
from django.contrib import messages #　検索結果のメッセージのため追加
class IndexList(ListView):
   template_name = 'report/index.html'
   paginate_by = 2
   # context_object_name = 'post_list'
   def get_queryset(self): # 検索機能のために追加
       queryset = Post.objects.order_by('-created_date')
       query = self.request.GET.get('query')
       if query:
           queryset = queryset.filter(
           Q(title__icontains=query) | Q(body__icontains=query)
           )
       messages.add_message(self.request, messages.INFO, query) #　検索結果メッセージ
       return queryset