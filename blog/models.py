from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    user = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    articles = models.ManyToManyField('Article', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = "Article"

    def __str__(self):
        return self.title
