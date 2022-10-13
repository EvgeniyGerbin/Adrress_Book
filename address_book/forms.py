from django import forms
from django.forms import ModelForm

from address_book.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

