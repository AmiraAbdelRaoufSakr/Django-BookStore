from django.contrib import admin

from books.forms import BookForm
from .models import Book, Category, Isbn, Tag


# Register your models here.
class BookPanel(admin.ModelAdmin):
    form = BookForm
    list_display = ("title", "owner", "content")
    list_filter = ("categories",)
    search_fields = ("title",)
    readonly_fields = ("owner",)


class BookInline(admin.StackedInline):
    model = Book
    max_num = 1
    extra = 1


class TagAdmin(admin.ModelAdmin):
    inlines = [BookInline]


admin.site.register(Book, BookPanel)
admin.site.register(Category)
admin.site.register(Isbn, TagAdmin)
admin.site.register(Tag )
