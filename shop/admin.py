from django.contrib import admin
from .models import *

# Register your models here.

class CaegoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')

admin.site.register(Category, CaegoryAdmin)
admin.site.register(Products)
