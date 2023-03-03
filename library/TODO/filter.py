from django_filters import rest_framework as filters
from .models import Project, TODO


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr="contains")

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(filters.FilterSet):
    class Meta:
        model = TODO
        fields = ['project']
