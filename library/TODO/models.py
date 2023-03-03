from datetime import datetime
import uuid


from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название проекта')
    repo_link = models.URLField(blank=True, default=uuid.uuid4, verbose_name='Ссылка на репозиторий')
    user_list = models.ManyToManyField('users.User', verbose_name='ID пользователя')

    def __str__(self):
        return self.name


class TODO(models.Model):
    project = models.ForeignKey(Project,
                                verbose_name='Проект, к которому относится заметка',
                                on_delete=models.SET_NULL,
                                null=True)
    node_text = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('users.User', verbose_name='Создатель', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.project

