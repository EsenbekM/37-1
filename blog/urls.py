"""
urls.py - файл маршрутизации проекта
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from post.views import test_view, main_view, post_list_view, \
    post_detail_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', main_view),
    path('posts/', post_list_view),
    path('posts/<int:post_id>/', post_detail_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
