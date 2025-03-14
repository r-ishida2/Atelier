from django.urls import path
from . import views
from .views import bookmarked_publishes

app_name = 'tunatoriapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('post/<int:publish>/', views.ReplyView.as_view(), name='post'),

    path('profile/<int:user>/', views.ProfileView.as_view(), name='profile'),

    path('publish/', views.PublishView.as_view(), name='publish'),

    path('bookmark/<int:publish>/',views.bookmark,name='bookmark'),
    path('bookmark_del/<int:bookmark_id>/',views.bookmark_del,name='bookmark_del'),
    path('bookmarks/', bookmarked_publishes, name='bookmarked_publishes'),

    # path('post/<int:publish>/reply/', views.ReplyView.as_view(), name='reply'),
]