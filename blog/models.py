from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from sqlalchemy import true

class Category(models.Model): 
    name = models.CharField(max_length=100, primary_key=true)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name



class Todo(models.Model):
    title = models.CharField(max_length=240)
    comment = models.TextField()
    date_posted = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title
