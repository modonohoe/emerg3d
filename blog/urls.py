from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.PostList.as_view(), name='blogposts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]
