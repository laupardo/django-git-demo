from django import forms
from .models import Dogs


class DogModelForm(forms.ModelForm):
    class Meta:
        model = Dogs
        fields=[
            'name',
            'breed',
            'age',
            'color'
        ]
