from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = ResBook
        fields = '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'