from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todoitem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Author: {self.author}, Title: {self.title}, Description: {self.description}, created_at: {self.created_at}, updated_at: {self.created_at}"
