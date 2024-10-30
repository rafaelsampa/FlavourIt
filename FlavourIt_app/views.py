from django.shortcuts import render
from .forms import *
from .models import receita, valores_nutricionais,utensilio
from .utils import insert_recipe

def menu(request):
    return render(request, 'flavourit/menu.html')

def tool_filter(request):
    return render(request, 'flavourit/tool_filter.html')

def time_filter(request):
    return render(request, 'flavourit/time_filter.html')

def recipe_results(request):
    return render(request, 'flavourit/recipe_results.html')

def recipe_card(request):
    return render(request, 'flavourit/recipe_card.html')

def receitas(request):
    query = "SELECT nome FROM receita"
    form = receita.objects.raw(query)
    
    return render(request, 'templates/flavourit/name_search.html', {'Receitas':form})

### FUNCIONOOOUUUUOOOOOUUOUOUUOOUUOUOUOUO
def ingredient_filter(request):
    ingredients = valores_nutricionais.objects.all()
    return render(request, 'flavourit/ingredient_filter.html', {'ingredients': ingredients})

def search_by_ingredients(request):
    selected_ingredients = request.GET.getlist('ingredients')

    if selected_ingredients:
        # Filter recipes based on selected ingredient IDs
        recipes = receita.objects.filter(
            ingredient__id_val_Nutri__id__in=selected_ingredients
        ).distinct()
    else:
        recipes = receita.objects.all()  # Show all recipes if no ingredients selected

    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes})

###

### NAME search okay bro!!!!!!!
def name_search(request):
    return render(request, 'flavourit/name_search.html')

def search_by_name(request):
    query = request.GET.get('name', '')  # Get the search query from the GET request

    if query:
        # Filter recipes based on the name containing the query string (case-insensitive)
        recipes = receita.objects.filter(nome__icontains=query)
    else:
        recipes = receita.objects.all()  # If no query, show all recipes

    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes, 'query': query})

###

###

def tool_filter(request):
    utensilios = utensilio.objects.all()
    return render(request, 'flavourit/tool_filter.html', {'utensilios': utensilios})

def search_by_tools(request):
    selected_tools = request.GET.getlist('utensilios')  # Ensure 'tools' matches the input name in your HTML

    if selected_tools:
        # Filter recipes based on selected tool IDs
        recipes = receita.objects.filter(
            receita_utensilio__id_utensilio__id__in=selected_tools
        ).distinct()
    else:
        recipes = receita.objects.all()  # Show all recipes if no tools are selected

    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes})

###