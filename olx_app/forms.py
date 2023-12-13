from django import forms

from .models import *

class product_form(forms.ModelForm):
    class Meta:
        model = product_model
        fields = '__all__'