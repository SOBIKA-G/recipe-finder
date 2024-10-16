from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Recipe
from django.template import loader
# Create your views here.
def index(request):
    res = Recipe.objects.all()
    sample_recipes = Recipe.objects.all()[:5]
    return render(request, 'home.html', {
        'res': res,
        'sample_recipes': sample_recipes})
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_details.html', {'recipe': recipe})

def search_recipes(request):
    query = request.GET.get('search')
    recipes = Recipe.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'recipes': recipes, 'query': query})