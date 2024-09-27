from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField()
    image = models.ImageField(upload_to='blog/photo')
    created_at = models.DateTimeField(auto_now_add=True)
    publication_sign = models.BooleanField(default=True)
    count_of_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['title']
