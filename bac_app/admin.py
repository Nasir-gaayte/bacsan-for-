from ast import Store
from django.contrib import admin
from .models import FromFactry, Sales, StoreIn

# Register your models here.

admin.site.register(FromFactry)
admin.site.register(Sales)
admin.site.register(StoreIn)