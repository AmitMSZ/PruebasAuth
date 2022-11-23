from django.contrib import admin
from .models import Warehouse, Type, Product
# Register your models here.
admin.site.register(Warehouse)
admin.site.register(Type)
admin.site.register(Product)
