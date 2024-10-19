from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='catalog/photo/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publication_status = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = [
            ("can_unpublish_product", "can unpublish product"),
        ]
