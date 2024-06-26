"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.sitemaps.views import sitemap
from myapp.sitemaps import PostSitemap, StaticSitemap

sitemaps = {
    'post': PostSitemap,
    #'category':BlogCategorySitemap,
    'static': StaticSitemap,    
}


from django.contrib import admin
from django.urls import path, include

admin.site.site_title = 'ぎょうざブログ 内部管理サイト'
admin.site.site_header = 'ぎょうざブログ 内部管理サイト'
admin.site.index_title = 'メニュー'

admin.site.disable_action('delete_selected')



urlpatterns = [
    path('staff-admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)