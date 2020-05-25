
from django.urls import path
# TM Import
from . import views #imports views from same dir

app_name = 'blog'
#specifying the app name will mean the detail page is connected to blog

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

# /blog goes to urls.py in proj folder and gets forwarded to urls.py in blog
# it then goes