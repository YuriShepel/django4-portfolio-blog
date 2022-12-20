from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.AllPosts.as_view(), name='all_blogs'),
    path('<int:post_id>/', views.Detail.as_view(), name='detail'),
    path('rewiew/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
]
