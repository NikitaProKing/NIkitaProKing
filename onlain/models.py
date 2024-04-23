from django.db import models
from django.contrib.auth.models import User

class ProductImg(models.Model):
    img = models.ImageField('фотография продукта', blank=True)

class Product(models.Model):
    name = models.CharField('название', max_length=40)
    short_description = models.CharField('краткое описание', max_length=35)
    full_description = models.TextField('полное описание')
    price = models.IntegerField('цена')
    quantity = models.IntegerField('количество на складе')
    product_images = models.ForeignKey(ProductImg, on_delete=models.CASCADE, related_name='products')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=20)
    age = models.IntegerField(blank=True)
    surname = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=20, default='user')

class Comment(models.Model):
    link_to_the_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user_link = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text_of_the_comment = models.CharField('текст комментария', max_length=200)
    date_of_creation = models.DateField('дата создания', auto_created=True)

class Rating(models.Model):
    link_to_the_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user_link = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    grade = models.IntegerField(blank=True)
