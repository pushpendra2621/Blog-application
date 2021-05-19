from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/<slug:category_slug>', views.category, name="categories"),
    path('tag/<slug:tag_slug>', views.tag, name="tags"),
    path('post/<slug:post_slug>', views.PostDetails, name="postdetails"),
    path('message', views.messages, name='message'),
    path('messagesuccess', views.MessageSuccess, name='messagesuccess'),
]