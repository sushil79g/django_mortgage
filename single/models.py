from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    content = models.TextField(default='',blank=True, null=False)
    datetime = models.DateField(auto_now=True)
    url = models.TextField(default='', blank=True, null=False)

    def __str__(self):
        return str(self.title)
