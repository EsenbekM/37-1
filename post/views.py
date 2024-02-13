'''
views.py - файл, содержащий описание представлений приложения

Методы запроса:
GET - получение данных
POST - отправка данных
PUT - обновление данных
DELETE - удаление данных

QuerySet - набор данных, полученных в результате запроса к базе данных

'''
import random

from django.shortcuts import render
from django.http import HttpResponse

from post.models import Post


def test_view(request):
    rn = random.randint(1, 1000)
    return HttpResponse(f'Hello, world! {rn}')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def post_list_view(request):
    if request.method == 'GET':
        # 1. Получение всех постов
        posts = Post.objects.all() # QuerySet (SELECT * FROM post_post)

        # 2. Формирование контекста
        context = {'posts': posts}

        # 3. Отображение шаблона
        return render(
            request=request, 
            template_name='post/post_list.html',
            context=context
            )