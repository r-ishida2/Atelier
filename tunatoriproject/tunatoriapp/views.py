from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import FormView,CreateView
from .forms import PublishCreationForm, ReplyCreationForm
from datetime import datetime
from django.urls import reverse_lazy
from .models import Publish,Reply

#作品一覧表示ページ
class IndexView(ListView):
    template_name = 'index.html'
    model = Publish
    def get_queryset(self):
        return Publish.objects.order_by("-at_post")

#作品詳細ページ
class PostView(TemplateView):
    template_name = 'post.html'

#プロフィールページ
class ProfileView(TemplateView):
    template_name = 'profile.html'

#作品投稿ページ
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

#コメント送信ページ
class ReplyView(CreateView):
    template_name = 'Reply.html'
    form_class = ReplyCreationForm
    success_url = reverse_lazy("tunatoriapp:index")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publish"] = Publish.objects.get(id=self.kwargs.get('publish_id'))
        context["replys"] = Reply.objects.filter(publish_id=self.kwargs.get('publish_id')).order_by("-at_reply")
        return context
    def form_valid(self, form):
        data = form.save(commit=False)
        publish_id = self.kwargs.get('publish_id')
        data.publish_id = Publish.objects.get(id=publish_id)
        data.user_id = self.request.user
        data.at_reply = datetime.now()
        data.save()
        return super().form_valid(form)



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
