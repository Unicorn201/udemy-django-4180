from django.contrib import admin
from .models import Post, Like, Category

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'thumbnail', 'title', 'category', 'created_at', )
    list_select_related = ('category', )
    list_display_links = ('title', )
    ordering = ('-created_at', )

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','post' )
    list_display_links = ('post', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )



from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import AdminSite
class BlogAdminSite(AdminSite):
    site_header = 'マイページ'
    site_title = 'マイページ'
    index_title = 'ホーム'
    site_url = None
    login_form = AuthenticationForm

    def has_permission(self, request):
        return request.user.is_active

mypage_site = BlogAdminSite(name = "mypage")

mypage_site.register(Post)
mypage_site.register(Like)
mypage_site.register(Category)