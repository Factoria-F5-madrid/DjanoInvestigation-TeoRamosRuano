from django import forms
from .models import Book

# BookForm is a ModelForm for the Book model
class BookForm(forms.ModelForm):
    class Meta:
        # This form is used to create or update Book instances
        model = Book
        # Specify the fields to include in the form
        fields = ['title', 'author', 'description', 'publish_date', 'isbn']
