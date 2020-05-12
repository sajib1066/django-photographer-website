from django.db import models
from django.contrib.auth.models import User

from capture.helper import get_current_user

class Category(models.Model):
    name = models.CharField(max_length=244, unique=True)
    is_delete = models.BooleanField(default=False)
    current_user = get_current_user
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=current_user)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=244)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='gallery/')
    is_delete = models.BooleanField(default=False)
    current_user = get_current_user
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=current_user)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
