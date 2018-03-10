
from django.db import models


class Version(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    major_version = models.IntegerField(max_length=3)
    minor_version = models.IntegerField(max_length=3)
    hotfix_version = models.IntegerField(max_length=3)
    build_version = models.IntegerField(max_length=3)

    def __str__(self):
        return self.project_name

