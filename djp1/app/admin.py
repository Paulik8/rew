from django.contrib import admin
from .models import *
# Register your models here.

def counter(obj):
    return len(Books.objects.get(name=obj.name).name)

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', counter)
    list_filter = ('name', )
    search_fields = ('name',)


admin.site.register(Books, BooksAdmin)


