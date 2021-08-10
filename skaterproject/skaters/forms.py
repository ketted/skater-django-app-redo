from django import forms
from .models import Skater

class SkaterForm(forms.ModelForm):
    class Meta:
        model = Skater
        fields = ('name', 'image', 'videos', 'pro')