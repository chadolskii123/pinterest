from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='project')

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    # 생성되었을 때 값이 저장됨
    created_at = models.DateTimeField(auto_created=True, null=True)
