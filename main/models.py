from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    def __str__(self):
        return f'{self.name}({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    image = models.ImageField(upload_to='main/', blank=True, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        return f'{self.category} {self.name}({self.description}) {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="имя")
    phone = models.CharField(max_length=20, verbose_name="телефон")
    email = models.EmailField(max_length=200, verbose_name="почта")
    address = models.TextField(blank=True, verbose_name="адрес")

    def __str__(self):
        return f'{self.name} {self.phone} {self.email} {self.address}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(max_length=200, verbose_name='адрес')
    content = models.TextField(blank=True, verbose_name='текст')
    preview = models.ImageField(upload_to='main/', blank=True, verbose_name='превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} {self.created_at} {self.views_count}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name='продукт')
    version_number = models.CharField(max_length=20, verbose_name='номер версии', blank=True)
    version_name = models.CharField(max_length=200, verbose_name='название версии', blank=True)
    is_current = models.BooleanField(default=False, verbose_name='текущая версия')

    def __str__(self):
        return f'{self.version_name} ({self.version_number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

