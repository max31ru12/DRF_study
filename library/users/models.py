from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=64, verbose_name='Имя')
    lastname = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(max_length=128, unique=True, verbose_name='Электронная почта')
    user_name = models.CharField(max_length=64, verbose_name='Имя пользователя')

    class Meta:
        ordering = ['id', ]


