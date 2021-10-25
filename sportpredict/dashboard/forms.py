from django import forms
from django.forms import fields
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name','age','height','sex']