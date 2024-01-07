from djongo import models

class Todo(models.Model):
    todo = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    