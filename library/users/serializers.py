from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import *


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
