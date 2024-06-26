from django.db import models
from django.contrib.auth.models import User
# from django.core.files.storage import default_storage
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=50)
    name_en = models.CharField('カテゴリ名英語', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def post_count(self):
        n = Post.objects.filter(category = self).count()
        return n

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    title = models.CharField('タイトル', max_length=100)
    content = models.TextField('内容', max_length=10000)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    thumbnail = models.ImageField(upload_to='images/', blank=True)
    thumbnail_preview = ImageSpecField(source='thumbnail',
                                      processors=[ResizeToFill(200, 100)],
                                      format='PNG',
                                      options={'quality': 60}
                                      )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def like_count(self):
        n = Like.objects.filter(post = self).count()
        return n

    def __str__(self):
        return self.title
    """
    def save(self):
        upload_file = self.files['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)
    """
    @property
    def thumbnail_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url
        return '#'


class Like(models.Model):
    post = models.ForeignKey(Post, verbose_name="投稿", on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name="Likeしたユーザー", on_delete=models.PROTECT)
