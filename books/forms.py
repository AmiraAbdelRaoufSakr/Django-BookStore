from django import forms
from .models import books

class booksForm(forms.ModelForm):
    class Meta:
        model = books
        fields = "__all__"