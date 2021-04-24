from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, Isbn


@receiver(post_save, sender=Book)
def after_book_creation(sender, instance, created, *args, **kwargs):
    if created:
        isbn_instance = Isbn.objects.create(author=instance.owner.username, book_title=instance.title)

        instance.isbn = isbn_instance
        instance.save()

    else:
        print("updating")
