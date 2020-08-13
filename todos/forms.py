from django import forms
from django.forms import ModelForm

from .models import *

class ItemsForm(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new item...'}))
    cost= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new item...'}))
    quantity= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new item...'}))
    description= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new item...'}))
    class Meta:
        model = Items
        fields = '__all__'