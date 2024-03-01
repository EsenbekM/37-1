from .models import Post


def create_100_posts():
    posts = []
    for i in range(100):
        post = Post(
            title=f'Title {i}',
            content=f'Content {i}',
            rate=i
        )
        posts.append(post)

    Post.objects.bulk_create(posts)


    