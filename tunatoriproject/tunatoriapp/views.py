from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import FormView,CreateView,DeleteView,UpdateView
from .forms import PublishCreationForm, ReplyCreationForm
from datetime import datetime
from django.urls import reverse_lazy,reverse
from django.forms.models import model_to_dict
from .models import Publish,Reply,Bookmark
from django.urls import reverse_lazy
from accounts.models import CustomUser
from .models import Publish,Reply
import math
from django.contrib.auth.decorators import login_required

#作品一覧表示ページ
class IndexView(ListView):
    template_name = 'index.html'
    model = Publish
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            publish = Publish.objects.filter(title__icontains=query).order_by("-at_post")
            if not publish.exists():
                return None
        else:
            publish = Publish.objects.order_by("-at_post")
        return publish

def bookmark(request,publish):
    Bookmark.objects.create(
        publish = Publish.objects.get(id=publish),
        user = request.user,
        at_bookmark = datetime.now()
    )
    return HttpResponseRedirect(reverse('tunatoriapp:post',kwargs={'publish':publish}))
def bookmark_del(request,bookmark_id):
    obj = Bookmark.objects.get(id=bookmark_id)
    publish = model_to_dict(obj)['publish']
    obj.delete()
    return HttpResponseRedirect(reverse('tunatoriapp:post',kwargs={'publish':publish}))

# #作品詳細ページ
# class PostView(TemplateView):
#     template_name = 'post.html'

#プロフィールページ
class ProfileView(ListView):
    template_name = 'profile.html'
    model = Publish
    def get_queryset(self, **kwargs):
        # 必要な QuerySet を返す（例: 全件、もしくはフィルタリングしたもの）
        return Publish.objects.filter(user= self.kwargs.get('user'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = CustomUser.objects.get(id=self.kwargs.get('user'))
        return context

    # user= get_object_or_404(, id=user)
    # return render(request, 'profile.html',{'user': user})

#作品投稿ページ
class PublishView(CreateView):
    template_name = 'publish.html'
    form_class = PublishCreationForm
    success_url = reverse_lazy("tunatoriapp:index")
    def form_valid(self, form):
        data = form.save(commit=False)
        data.user = self.request.user
        data.at_post = datetime.now()
        data.save()
        return super().form_valid(form)

#作品詳細・コメント送信ページ
class ReplyView(CreateView):
    template_name = 'Reply.html'
    form_class = ReplyCreationForm
    success_url = reverse_lazy("")
    def get_success_url(self):
        return reverse_lazy("tunatoriapp:post",kwargs={"publish":self.kwargs["publish"]})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publish"] = Publish.objects.get(id=self.kwargs.get('publish'))
        if self.request.user.is_authenticated:
            bookmark = list(Bookmark.objects.filter(publish=self.kwargs.get('publish'),user=self.request.user).values())
            if bookmark:
                context["bookmark"] = bookmark[0]["id"]
        replys = Reply.objects.filter(publish=self.kwargs.get('publish')).order_by("-at_reply")
        context["replys"] = replys

        #評価値の平均計算
        rating = 0
        if replys:
            for reply in replys:
                rating += reply.rating
            rating = math.floor(rating/len(replys)*10)/10.0
        context["rating"] = rating

        return context
    def form_valid(self, form):
        data = form.save(commit=False)
        publish = self.kwargs.get('publish')
        data.publish = Publish.objects.get(id=publish)
        data.user = self.request.user
        data.at_reply = datetime.now()
        data.save()
        return super().form_valid(form)



# from django.db.models import Q # get_queryset()用に追加
# from django.contrib import messages #　検索結果のメッセージのため追加
# class IndexList(ListView):
#    template_name = 'index.html'
#    paginate_by = 2
#    # context_object_name = 'post_list'
#    def get_queryset(self): # 検索機能のために追加
#        queryset = Publish.objects.order_by('-at_post')
#        query = self.request.GET.get('query')
#        if query:
#            queryset = queryset.filter(
#            Q(title__icontains=query) | Q(body__icontains=query)
#            )
#        messages.add_message(self.request, messages.INFO, query) #　検索結果メッセージ
#        return queryset

@login_required
def bookmarked_publishes(request):
    # ログインユーザーがブックマークしている作品を取得
    bookmarked_publishes = Publish.objects.filter(id__in=Bookmark.objects.filter(user=request.user).values_list('publish', flat=True))

    return render(request, 'book_list.html', {'bookmarked_publishes': bookmarked_publishes})

class PublishDeleteView(DeleteView):
    model = Publish
    success_url = reverse_lazy("tunatoriapp:index")

class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ["usericon","username"]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tunatoriapp:index')