from django.shortcuts import render
from .forms import *
from .models import receita, valores_nutricionais,utensilio
from datetime import datetime
from django.db.models import Count, Q, F


# ======== Views para URLs ========

def menu(request):
    return render(request, 'flavourit/menu.html')

def time_filter(request):
    return render(request, 'flavourit/time_filter.html')

def recipe_results(request):
    return render(request, 'flavourit/recipe_results.html')

def recipe_card(request):
    return render(request, 'flavourit/recipe_card.html')

def account(request):
    return render(request, 'flavourit/account.html')

# ======== Fim de views para URLs ========

# ======== Views para Queries ========

def receitas(request):
    query = "SELECT nome FROM receita"
    form = receita.objects.raw(query)
    
    return render(request, 'templates/flavourit/name_search.html', {'Receitas':form})

## FUNCIONOOOUUUUOOOOOUUOUOUUOOUUOUOUOUO
def ingredient_filter(request):
    ingredients = valores_nutricionais.objects.all()
    return render(request, 'flavourit/ingredient_filter.html', {'ingredients': ingredients})

def search_by_ingredients(request):
    selected_ingredients = request.GET.getlist('ingredients')
    busca_exclusiva = request.GET.get('busca_exclusiva')  # Returns 'on' if checked
    #print("busca:::::::::"+busca_exclusiva);

    if selected_ingredients:
        # Start with recipes that include all selected ingredients
        recipes = receita.objects.filter(ingredient__id_val_Nutri__id__in=selected_ingredients).distinct()

        #if busca_exclusiva == 'on':
        #    recipes = recipes.annotate(
        #        ingredient_count=Count('ingredient'),  # Total ingredients in each recipe
        #        matched_ingredients_count=Count(
        #            'ingredient',
        #            filter=Q(ingredient__id_val_Nutri__id__in=selected_ingredients)
        #       )  # Ingredients that match the selected list
        #    ).filter(
        #        ingredient_count=F('matched_ingredients_count')
        #    )

    else:
        # If no ingredients are selected, return all recipes
        recipes = receita.objects.all()

    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes})


##

## NAME search okay bro!!!!!!!
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

### funciona kkkkkkkkk
def time_filter(request):
    return render(request, 'flavourit/time_filter.html')

def search_by_time(request):
    
    user_time = request.GET.get('recipe-time')  # Retrieve the time input from the form
    
    if user_time:
        # Convert `hh:mm` (user input) to `hh:mm:ss` for compatibility with `tempo`
        user_time_obj = datetime.strptime(user_time, "%H:%M")
        user_time_formatted = user_time_obj.strftime("%H:%M:%S")
        
        # Filter recipes with `tempo` less than or equal to the user's time
        recipes = receita.objects.filter(tempo__lte=user_time_formatted)
    else:
        recipes = receita.objects.all()  # Show all recipes if no time specified

    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes})

###

# ======== Fim de views para Queries ========