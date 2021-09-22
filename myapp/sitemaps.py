from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url

from myapp.models import Post, Category


class PostSitemap(Sitemap):
    """
    ブログ記事のサイトマップ
    """
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    # モデルに get_absolute_url() が定義されている場合は不要
    def location(self, obj):
        return resolve_url('myapp:post_detail', pk=obj.id)

class StaticSitemap(Sitemap):

    def items(self):
        items = [
            'myapp:index',
            'myapp:contents_policy',
            'myapp:about',
            'myapp:terms',
            'myapp:post_list',
            'myapp:category_list',
        ]
        return items

    def location(self, obj):
        return resolve_url(obj)

    def changefreq(self, obj):
        if obj == 'myapp:index':
            return 'always'
        return 'never'

    def priority(self, obj):
        if obj == 'myapp:index':
            return 0.8
        return 0.1