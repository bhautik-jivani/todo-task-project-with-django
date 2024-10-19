from django.db import models

# Create your models here.
class TodoTask(models.Model):
    name = models.CharField(max_length=250, blank=True, default="")
    description = models.TextField(blank=True, default="")
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)