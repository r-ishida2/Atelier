from django.urls import path
from . import views

app_name = 'tunatoriapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('post/', views.PostView.as_view(), name='post'),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('publish/', views.PublishView.as_view(), name='publish'),

    path('<int:publish_id>/reply/', views.ReplyView.as_view(), name='reply'),
]