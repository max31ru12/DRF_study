from rest_framework.serializers import HyperlinkedModelSerializer
from .models import *


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
