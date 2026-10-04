from django.contrib import admin

admin.site.site_header = "Админ панель"
admin.site.site_title = "Админ панель"
admin.site.index_title = "Добро пожаловать в админ панель"
from .models import Category, SubCategory, Product, Cart, Order, OrderItem

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
