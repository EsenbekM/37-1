'''
views.py - файл, содержащий описание представлений приложения

Методы запроса:
GET - получение данных
POST - отправка данных
PUT - обновление данных
DELETE - удаление данных

QuerySet - набор данных, полученных в результате запроса к базе данных

FBV - Function Based View - представление, основанное на функциях
CBV - Class Based View - представление, основанное на классах
'''
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse

from post.models import Post
from post.forms import PostForm, PostForm2, CommentForm


def test_view(request):
    rn = random.randint(1, 1000)
    return HttpResponse(f'Hello, world! {rn}')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def post_list_view(request):
    if request.method == 'GET':
        # 1. Получение всех постов
        posts = Post.objects.all() \
            .prefetch_related('tags') \
                .select_related('category') # QuerySet (SELECT * FROM post_post)

        # 2. Формирование контекста
        context = {'posts': posts}

        # 3. Отображение шаблона
        return render(
            request=request, 
            template_name='post/post_list.html',
            context=context
            )
    

def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return render(
                request=request,
                template_name='errors/404.html'
            )
        form = CommentForm()
        context = {'post': post, 'form': form}

        return render(
            request=request,
            template_name='post/post_detail.html',
            context=context
        )
    

def create_comment_view(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(
                request=request,
                template_name='post/post_detail.html',
                context={'form': form}
            )
        
        # form.save() - попробует сохранить в базу данных 'text'

        comment = form.save(commit=False) # commit=False - не сохранять в базу данных
        # comment.text = "Some text"
        comment.post_id = post_id
        # comment.post_id = 3
        comment.save()

        return redirect(f'/posts/{post_id}/')


def create_post_view(request):
    if request.method == 'GET':
        form = PostForm2()

        return render(
            request=request,
            template_name='post/create_post.html',
            context={"form": form}
        )
    elif request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        # form.add_error(field=None, error='Some error')
        if not form.is_valid():
            return render(
                request=request,
                template_name='post/create_post.html',
                context={"form": form}
            )
        # request.POST 
        # Post.objects.create(**form.cleaned_data)
        form.save()
        return redirect('/posts/')
    
