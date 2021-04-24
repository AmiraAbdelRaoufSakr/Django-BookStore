from django.contrib.auth.models import User
from django.db import models
import uuid


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Isbn(models.Model):
    isbn_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=50, null=True, blank=True)
    book_title = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Author:{self.author} | Book:{self.book_title} | Isbn_number: {self.isbn_number}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", null=True, blank=True)
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(Isbn, null=True, blank=True, on_delete=models.CASCADE)
    tage = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="books", null=True, blank=True)

    def __str__(self):
        return self.title
