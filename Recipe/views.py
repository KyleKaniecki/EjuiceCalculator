from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Recipe, Flavoring
from .forms import RecipeForm
from django.forms import inlineformset_factory


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
            recipe = form.save()
            messages.add_message(request,messages.SUCCESS,"Updated recipe successfully!")
            return redirect('recipe_edit', pk=recipe.pk)
    else:
        recipeform = RecipeForm(instance=recipe)
        recipe = Recipe.objects.get(id=pk)

    return render(request, 'Recipe/recipe_edit.html', {'recipeform': recipeform,
                                                       'recipe':recipe})


def flavorings_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    FlavoringInlineFormSet = inlineformset_factory(Recipe, Flavoring, fields=('name',))
    if request.method == "POST":
        formset = FlavoringInlineFormSet(request.POST, request.FILES, instance=recipe)
        if formset.is_valid():
            formset.save()
            return redirect('recipe_list')
    else:
        formset = FlavoringInlineFormSet(instance=recipe)
    return render(request, 'Recipe/recipe_edit.html', {'formset': formset})