from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, Flavoring
from .forms import RecipeForm


def recipe_list(request):
    recipes = Recipe.objects.order_by('name')
    flavoring = Flavoring.objects.order_by('name')
    return render(request, 'Recipe/recipe_list.html', {'recipes': recipes, 'flavoring': flavoring})


def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
        return render(request, 'Recipe/recipe_new.html', {'form': form})


def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.name = request.name
            recipe.daysToSteep = request.daysToSteep
            recipe.save()
            return redirect('recipe_edit', pk=recipe.pk)
    else:
        recipe = RecipeForm(instance=recipe)
    return render(request, 'Recipe/recipe_edit.html', {'recipe': recipe})