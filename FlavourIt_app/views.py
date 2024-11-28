from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import receita, valores_nutricionais, utensilio, ingredient
from datetime import datetime
from FlavourIt_app.models import receita, client
from math import floor
from decimal import Decimal
from django.http import JsonResponse



# ======== Views para URLs ========

def menu(request):
    return render(request, 'flavourit/menu.html')

def time_filter(request):
    return render(request, 'flavourit/time_filter.html')

def recipe_results(request):
    return render(request, 'flavourit/recipe_results.html')

def nutritional_data(request):
    return render(request, 'flavourit/nutritional_data.html')

def recipe_card(request, recipe_id):
    recipe = get_object_or_404(receita, id=recipe_id)
    user_quantities = request.session.get('user_quantities', {})
    ingredients = ingredient.objects.filter(id_receita=recipe).select_related('id_val_Nutri')
    utensils = utensilio.objects.filter(receita_utensilio__id_receita=recipe)

    recipe_ingredients = ingredient.objects.filter(id_receita=recipe)

    portions=-1

    for rec_ingredient in recipe_ingredients:
        ingredient_id = rec_ingredient.id_val_Nutri.id  #Get the nutritional value ID
        #print("AQUI: ");
        #print(ingredient_id);
        quant_needed = rec_ingredient.quant  #Quantity needed for the recipe

        #print(f"Type of user_quantities keys: {type(next(iter(user_quantities.values()), None))}")

        #print(user_quantities);
        if str(ingredient_id) not in user_quantities:
            #print(f"Type of ingredient_id: {type(ingredient_id)}")

            portions=-1
            break;  # Missing ingredient, stop calculation

        user_quant = Decimal(user_quantities[str(ingredient_id)])  # Quantity provided by the user
        porcao = floor(user_quant / quant_needed)  # Calculate portions based on this ingredient
        #print(f"Type of user_quant: {type(user_quant)}")
        #print(f"Type of porcao: {type(porcao)}")
        #print(porcao)

        # Update menor_porcao
        if portions==-1 or porcao < portions:
            portions = porcao

    #print("PORTIONS: ")
    #print(portions)
    if portions==-1:
        portions=None

    ingredient_data = []
    for ing in ingredients:
        ingredient_data.append({
            'quant': ing.quant,
            'unidade': ing.unidade,
            'nutrition_info': {
                'nome': ing.id_val_Nutri.nome,
                'gordura': ing.id_val_Nutri.gordura,
                'carboidrato': ing.id_val_Nutri.carboidrato,
                'proteina': ing.id_val_Nutri.proteina,
                'porcao': ing.id_val_Nutri.porção,
                'unidade': ing.id_val_Nutri.unidade,
            }
        })

    return render(request, 'flavourit/recipe_card.html', {
        'recipe': recipe,
        'ingredients': ingredient_data,
        'utensils': utensils,
        'portions': portions,
    })

def receitas_favoritadas(request):

    try:
        member = client.objects.get(id=request.user.id)  # Assuming the user is logged in and request.user is available
    except:
        print("DEU ERRADO");
        return redirect(request.META.get('HTTP_REFERER', '/'))

    id_user=member.id
    recipes = receita.objects.filter(favoritado__id_Cliente=id_user)
    
    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes})


def favoritar(request):
    if request.method == "POST":
        receita_id = request.POST.get("id_receita")  # Ensure the ID is sent in the POST request
        try:
            member = client.objects.get(id=request.user.id)  # Assuming the user is logged in and request.user is available
        except:
            print("DEU ERRADO");
            return redirect(request.META.get('HTTP_REFERER', '/'))

        # Check if the favorite already exists
        favorite = favoritado.objects.filter(id_Receita_id=receita_id, id_Cliente_id=member.id).first()

        if favorite:
            # If it exists, remove the favorite (unfavorite)
            favorite.delete()
            print("FOI1")
        else:
            # If it doesn't exist, create a new favorite
            favoritado.objects.create(id_Receita_id=receita_id, id_Cliente_id=member.id)
            print("FOI2")

    # Redirect back to the current page
    return redirect(request.META.get('HTTP_REFERER', '/'))



def configAccount(request):
    if request.method == "POST":
        birthDate = request.POST.get('birth_date', None)
        weight = request.POST.get('weight', None)
        height = request.POST.get('height', None)
        activity = request.POST['activity']
        
        try:
            member = client.objects.get(id=request.user.id)
            member.Birth_Date = birthDate
            member.peso = weight
            member.altura = height
            member.Atividade = activity
            member.save()
        except client.DoesNotExist:
            member = client(Birth_Date=birthDate,peso=weight, altura=height, Atividade=activity)
            member.save()
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
    #for ingredientes in selected_ingredients:
    #    print(ingredientes)

    #qtd informada pelo user
    user_quantities = {
        int(key.split('_')[1]): float(value)
        for key, value in request.GET.items() if key.startswith('quantity_') and value
    }

    if selected_ingredients:
        # Start with recipes that include all selected ingredients
        recipes = receita.objects.filter(ingredient__id_val_Nutri__id__in=selected_ingredients).distinct()

        if busca_exclusiva == 'on':
            exclusive_recipe_ids = []
            for recipe in recipes:
                #print(f"Recipe: {recipe.nome},")
                # Get all ingredient IDs in this recipe
                recipe_ingredient_ids = set(recipe.ingredient_set.values_list('id_val_Nutri__id', flat=True))
                #for ingredientes in recipe_ingredient_ids:
                #    print(ingredientes)

                # string to int
                selected_ingredients = set(map(int, selected_ingredients))
                # Check if recipe ingredients are a subset of selected ingredients
                if recipe_ingredient_ids.issubset(selected_ingredients):
                    exclusive_recipe_ids.append(recipe.id)


            # Filter to only include recipes that matched the exclusive criteria
            recipes = recipes.filter(id__in=exclusive_recipe_ids)

    else:
        # If no ingredients are selected, return all recipes
        recipes = receita.objects.all()


    request.session['user_quantities'] = user_quantities

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
    busca_exclusiva = request.GET.get('busca_exclusiva')

    if selected_tools:
        # Filter recipes based on selected tool IDs
        recipes = receita.objects.filter(receita_utensilio__id_utensilio__id__in=selected_tools).distinct()

        if busca_exclusiva == 'on':
            exclusive_recipe_ids = []
            for recipe in recipes:
                #print(f"Recipe: {recipe.nome},")
                # Get all ingredient IDs in this recipe
                recipe_tools_ids = set(recipe.receita_utensilio_set.values_list('id_utensilio__id', flat=True))
                #for ingredientes in recipe_ingredient_ids:
                #    print(ingredientes)

                # string to int
                selected_tools = set(map(int, selected_tools))
                # Check if recipe ingredients are a subset of selected ingredients
                if recipe_tools_ids.issubset(selected_tools):
                    exclusive_recipe_ids.append(recipe.id)


            # Filter to only include recipes that matched the exclusive criteria
            recipes = recipes.filter(id__in=exclusive_recipe_ids)


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


def nutritional_data(request, recipe_id):
    recipe = get_object_or_404(receita, id=recipe_id)

    ingredientes = ingredient.objects.filter(id_receita=recipe).select_related('id_val_Nutri')

    ingredient_data = []
    for ing in ingredientes:
        ingredient_data.append({
            'quantidade': ing.quant,
            'unidade': ing.unidade,
            'nutrition_info': {
                'nome': ing.id_val_Nutri.nome,
                'gordura': ing.id_val_Nutri.gordura,
                'carboidrato': ing.id_val_Nutri.carboidrato,
                'proteina': ing.id_val_Nutri.proteina,
                'porcao': ing.id_val_Nutri.porção,
                'unidade': ing.id_val_Nutri.unidade,
            }
        })

    return render(request, 'flavourit/nutritional_data.html', {
        'recipe': recipe,
        'ingredientes': ingredient_data,
    })

    def recipeCardFavorite(request):
        receita_id = request.GET['receita_id']

        if favoritado.objects.filter(id_Client_id = request.user.id, id_Receita_id = receita_id).exists():
            result = True
        else:
            result = False
        return render(request, 'recipe_card.html', {'results': result})

###

# ======== Fim de views para Queries ========