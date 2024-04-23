from django.contrib import admin
from .models import Product, Profile, ProductImg, Comment

admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(ProductImg)
admin.site.register(Comment)