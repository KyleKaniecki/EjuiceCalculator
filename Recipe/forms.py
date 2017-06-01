from django import forms
from .models import Recipe, Flavoring


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'daysToSteep', 'notes',)


    def __init__(self,*args,**kwargs):
        super(RecipeForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs = {"class":"form-control"}