from django import forms
from .models import Recipe, Flavoring


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'daysToSteep', 'notes')