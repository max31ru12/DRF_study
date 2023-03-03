from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from authors.serializers import AuthorModelSerializer
from .models import *
from rest_framework.pagination import LimitOffsetPagination


# Create your views here.
class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
