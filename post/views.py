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
from django.db.models.query import QuerySet

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# from django.urls import reverse

from post.models import Post, Tag
from post.forms import PostForm, PostForm2, CommentForm


def test_view(request):
    rn = random.randint(1, 1000)
    return HttpResponse(f'Hello, world! {rn}')


class TestView(View):
    def get(self, request):
        rn = random.randint(1, 1000)
        return HttpResponse(f'Hello, world! {rn}')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


class PostListView(ListView):
    model = Post
    context_object_name = 'posts' # default: 'object_list'
    template_name = 'post/list.html' # default: '<app>/<model>_list.html'
    # context = {'object_list': Post.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')    

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(content__icontains=search)
            )
        return queryset


def post_list_view(request):
    if request.method == 'GET':
        # 1. Получение всех постов
        search = request.GET.get('search')
        tag_id = request.GET.get('tag')
        sort = request.GET.get('sort')
        page = request.GET.get('page', 1)

        tags = Tag.objects.all()
        posts = Post.objects.all() \
            .prefetch_related('tags') \
                .select_related('category') # QuerySet (SELECT * FROM post_post)

        if search:
            # posts = posts.filter(title__icontains=search) | posts.filter(content__icontains=search)
            posts = posts.filter(
                Q(title__icontains=search) | 
                Q(content__icontains=search)
                # Q(tags__name__icontains=search)
            )
        if tag_id:
            posts = posts.filter(tags=tag_id)

        if sort == 'rate':
            order = request.GET.get('order')
            if order == 'asc':
                posts = posts.order_by('rate')
            else:
                posts = posts.order_by('-rate')
        elif sort == 'created_at':
            order = request.GET.get('order')
            if order == 'asc':
                posts = posts.order_by('created_at')
            else:
                posts = posts.order_by('-created_at')

        # icontains - case insensitive contains
        # contains - case sensitive contains
        # iexact - case insensitive exact
        # exact - case sensitive exact
        # startswith - начинается с
        # endswith - заканчивается на
        # in - входит в список
        # gt - больше чем
        # gte - больше или равно
        # lt - меньше чем
        # lte - меньше или равно
        # range - входит в диапазон
        # isnull - равно null
        # regex - регулярное выражение
        # Docs: https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups


        'posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10]'
        'limit = 3, page = 1'
        'max_pages = 10 / 3 = 3.3333 => 4'

        'formula:'
        'start = (page - 1) * limit'
        'end = start + limit'

        'example:'
        'page = 1, limit = 3'
        'start = (1 - 1) * 3 = 0'
        'end = 0 + 3 = 3'

        'page = 2, limit = 3'
        'start = (2 - 1) * 3 = 3'
        'end = 3 + 3 = 6'

        'page = 4, limit = 3'
        'start = (4 - 1) * 3 = 9'
        'end = 9 + 3 = 12'

        limit = 20
        max_pages = posts.count() / limit
        if max_pages % 1 != 0:
            max_pages = int(max_pages) + 1
            
        pages = [i for i in range(1, max_pages + 1)]
    
        # if len(pages) > 10:
        #     pages = pages[:10] + [max_pages + 1]

        start = (int(page) - 1) * limit
        end = start + limit

        posts = posts[start:end]

        # 2. Формирование контекста
        context = {
            'posts': posts, 'tags': tags,
            "pages": pages
            }

        # 3. Отображение шаблона
        return render(
            request=request, 
            template_name='post/list.html',
            context=context
            )
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/post_detail.html'
    pk_url_kwarg = 'post_id'



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


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm2
    template_name = 'post/create_post.html'
    success_url = '/posts/'


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
    

@login_required(login_url='/login/')
def update_post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(
            request=request,
            template_name='errors/404.html'
        )
    if request.method == 'GET':
        form = PostForm2(instance=post)
        return render(
            request=request,
            template_name='post/update_post.html',
            context={"form": form}
        )
    elif request.method == 'POST':
        form = PostForm2(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(
                request=request,
                template_name='post/update_post.html',
                context={"form": form}
            )
        form.save()
        return redirect(f'/posts/{post_id}/')