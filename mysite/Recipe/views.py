from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Flavoring


def recipe_list(request):
    recipes = Recipe.objects.order_by('name')
    return render(request, 'Recipe/recipe_list.html', {'recipes': recipes})