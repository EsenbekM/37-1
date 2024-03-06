'''
models.py - файл, содержащий описание моделей приложения (базы данных)
'''

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model): 
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='posts',
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    image = models.ImageField(upload_to='post_images/%Y/%m/%d', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(
        Tag, 
        related_name='posts'
    )

    def __str__(self):
        return f'{self.title} - {self.rate}'


# class PostInfo(models.Model):
#     post = models.OneToOneField(
#         Post,
#         on_delete=models.CASCADE,
#         related_name='info'
#     )
#     likes = models.IntegerField(default=0)
#     dislikes = models.IntegerField(default=0)
#     views = models.IntegerField(default=0)

#     def __str__(self):
#         return f'Info for {self.post.title}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE, # SET_NULL, SET_DEFAULT, DO_NOTHING, PROTECT
        related_name='comments' # default: comment_set
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Comment for {self.post.title}'
