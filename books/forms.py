from django import forms
from django.core.exceptions import ValidationError

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("tage",)

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if len(title) not in range(10, 50):
            raise ValidationError("Title length should be between 10 and 50 characters")

        return title

    def clean(self):
        super(BookForm, self).clean()
        categories = self.cleaned_data.get("categories")

        if len(categories) < 2:
            raise ValidationError("Minimum length of content is 2 characters")
        return self.cleaned_data
