from django.urls import path
from . import views

app_name = 'tunatoriapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('post/<int:publish_id>/', views.ReplyView.as_view(), name='post'),

    path('profile/<int:user_id>/', views.ProfileView.as_view(), name='profile'),

    path('publish/', views.PublishView.as_view(), name='publish'),

    path('bookmark/<int:publish_id>/',views.bookmark,name='bookmark'),
    path('bookmark_del/<int:bookmark_id>/',views.bookmark_del,name='bookmark_del'),

    # path('post/<int:publish_id>/reply/', views.ReplyView.as_view(), name='reply'),
]