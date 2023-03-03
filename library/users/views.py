from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView
from .models import *
from .serializers import UserModelSerializer
from rest_framework.pagination import LimitOffsetPagination


# Create your views here.
class UserOffsetLimitPagination(LimitOffsetPagination):
    default_limit = 100


# Чтение, получение одной записи, обновление
class UserAPIList(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserOffsetLimitPagination
    permisson_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserOffsetLimitPagination
    permisson_classes = [permissions.IsAuthenticatedOrReadOnly]