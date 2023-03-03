from django.contrib import admin
from .models import *


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "repo_link", )
    search_fields = ('name', )


class TODOAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'node_text', 'date_created', 'date_updated', 'creator', 'is_active')
    search_fields = ('id', 'is_active', 'creator', 'project')


admin.site.register(Project, ProjectAdmin)
admin.site.register(TODO, TODOAdmin)