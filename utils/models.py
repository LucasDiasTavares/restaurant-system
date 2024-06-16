from django.db import models


class Base(models.Model):
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    deleted_by = models.IntegerField()
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
