from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogList, name='blog_list'),
    path('<slug:slug>/', views.blogDetail, name='blog_detail'),
]