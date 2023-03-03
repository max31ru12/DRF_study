from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'user_name', )
    search_fileds = ('id', 'lastname', 'user_name')


admin.site.register(User, UserAdmin)
