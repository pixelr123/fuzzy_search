from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^search$', views.search_words, name='search_words'),
]