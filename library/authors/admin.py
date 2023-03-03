from django.contrib import admin
from .models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birthday_year')
    search_fields = ('first_name', 'last_name')


admin.site.register(Author, AuthorAdmin)
