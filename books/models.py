from django.db import models

class books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField(max_length=2048)
    

    def __str__(self):
        return self.title