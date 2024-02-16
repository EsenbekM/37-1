'''
admin.py - файл, содержащий описание административной панели
'''

from django.contrib import admin

from post.models import Post, Comment, Tag


# admin.site.register(Post)

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'created_at')
    list_display_links = ('title',)
    list_editable = ('rate',)
    list_filter = ('created_at', 'rate')
    search_fields = ('title', 'content')
    readonly_fields = ('id', 'created_at', 'updated_at', 'title')
    fields = ('id', 'title', 'content', 'rate', 'created_at', 'updated_at')
    inlines = [CommentInline]

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return ()
    #     return self.readonly_fields

    # def get_queryset(self, request: HttpRequest) -> QuerySet:
    #     return Post.objects.filter(id=1)

    # def has_add_permission(self, request: HttpRequest) -> bool:
    #     if request.user.is_superuser:
    #         return True
    #     return False
    
    # def has_delete_permission(self, request: HttpRequest, obj: Any = None) -> bool:
    #     return False
    
    # def has_change_permission(self, request: HttpRequest, obj: Any = None) -> bool:
    #     return False



admin.site.register(Comment)
admin.site.register(Tag)
