from django import forms
from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team 
        exclude = ('videos',)
        fields = ('brand', 'est', 'olympics', 'skaters')