"""
urls.py - файл маршрутизации проекта
"""
from django.contrib import admin
from django.urls import path

from post.views import test_view, main_view, post_list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', main_view),
    path('posts/', post_list_view),
]
