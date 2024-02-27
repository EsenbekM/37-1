"""
urls.py - файл маршрутизации проекта
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from post.views import test_view, main_view, post_list_view, \
    post_detail_view, create_post_view, create_comment_view

from user.views import register_view, login_view, profile_view, logout_view, confirm_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', main_view, name='main_view'),
    path('posts/', post_list_view),
    path('posts/<int:post_id>/', post_detail_view),
    path('posts/create/', create_post_view),
    path('posts/<int:post_id>/create_comment/', create_comment_view),

    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('profile/', profile_view, name='profile_view'),
    path('logout/', logout_view, name='logout_view'),
    path('confirm/', confirm_view, name='confirm_view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
