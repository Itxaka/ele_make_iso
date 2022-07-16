from django.db import models

# Create your models here.

status = (
    ("started", "started"),
    ("stuck", "stuck"),
    ("failed", "failed"),
    ("finished", "finished")
)


class Jobs(models.Model):
    uuid = models.UUIDField(unique=True, auto_created=True)
    status = models.CharField(choices=status, max_length=128, null=True)
    failReason = models.TextField(max_length=10000,null=True)
    yaml = models.TextField(max_length=50000)
    name = models.CharField(max_length=200, unique=True)
