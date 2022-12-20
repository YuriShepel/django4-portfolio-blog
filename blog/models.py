from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    content = RichTextField(blank=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    name = models.CharField('Name', max_length=30)
    email = models.EmailField()
    text = models.TextField('Comment', max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'
