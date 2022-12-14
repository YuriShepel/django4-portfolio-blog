from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    content = RichTextField(blank=True)

    def __str__(self):
        return self.title
