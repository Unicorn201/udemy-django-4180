from django.urls import path, include
from . import views
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from .views import ContactFormView, ContactResultView
from .admin import mypage_site

app_name = 'myapp'

urlpatterns = [
    # ユーザーマイページ
    path('mypage/', mypage_site.urls),

    path('', views.Index.as_view(), name='index'),
    path('ads.txt', TemplateView.as_view(
                                template_name='myapp/ads.txt', content_type='text/plain'
                             )),  # 追加
    # path('', include('mayapp.urls')),
    path('post_create', views.PostCreate.as_view(), name='post_create'),
    # ↓投稿記事の入力内容の確認画面を追加
    # path('post_create_confirm', views.PostCreate.as_view(), name='post_confirm_create'),
    path('post_detail/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('post_update/<int:pk>', views.PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),
    path('post_list', views.PostList.as_view(), name='post_list'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('like/<int:post_id>', views.Like_add, name='like_add'),
    path('category_list', views.CategoryList.as_view(), name='category_list'),
    path('category_detail/<str:name_en>', views.CategoryDetail.as_view(), name='category_detail'),
    path('search', views.Search, name='search'),

    # footer links
    path('about', TemplateView.as_view(template_name='myapp/about.html'), name='about'),
    path('terms', TemplateView.as_view(template_name='myapp/terms.html'), name='terms'),
    path('contents_policy', TemplateView.as_view(template_name='myapp/contents_policy.html'), name='contents_policy'),
    path('contact_me', ContactFormView.as_view(), name='contact_me'),
    path('contact_me/contact_result', ContactResultView.as_view(), name='contact_result'),
    # path('policy/', TemplateView.as_view(template_name='base/policy.html'), name='policy'),


]

# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))