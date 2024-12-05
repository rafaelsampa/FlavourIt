from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import receita, valores_nutricionais, utensilio, ingredient,client
from datetime import datetime
from math import floor
from decimal import Decimal
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
import os
from django.core.files.storage import FileSystemStorage
from django.urls import reverse

def registerView(request):
    if request.method == "POST":
        # name = request.POST['name']
        username = request.POST['username']
        birthDate = request.POST['birth_date']
        email = request.POST['email']
        password = request.POST['password']
        weight = request.POST['weight']
        height = request.POST['height']
        activity = request.POST['activity']
        
        user_data_has_error = False
        
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, 'Username already exists')
        
        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, 'Email already exists')
        
        if len(password) < 8:
            user_data_has_error = True
            messages.error(request, 'Password must be at least 8 characters')
        
        if not user_data_has_error:
            auth = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user = client(
                # nome = name,
                Birth_Date = birthDate,
                altura = height,
                peso = weight,
                Atividade = activity
            )
            user.save()
            messages.success(request, 'Account created. Login now')
            return redirect('login')
        else:
            return redirect('signup')
    return render(request, 'registration/signup.html')

def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    return render(request, 'registration/login.html')

def logoutView(request):
    logout(request)
    return redirect('menu')

def menu(request):
    return render(request, 'flavourit/menu.html')

def time_filter(request):
    return render(request, 'flavourit/time_filter.html')

def recipe_results(request):
    return render(request, 'flavourit/recipe_results.html')

def nutritional_data(request):
    return render(request, 'flavourit/nutritional_data.html')


def adicionar_receitas(request):

    ingredients = valores_nutricionais.objects.all()
    utensilios=utensilio.objects.all()

    return render(request, 'flavourit/adicionar_receita.html', {'ingredients': ingredients, 'utensilios': utensilios})

def add_recipe(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        tempo = request.POST.get('tempo')
        instructions = request.POST.get('instructions')
        selected_ingredients = request.POST.getlist('ingredients')
        selected_utensilios = request.POST.getlist('utensilios')
        imagem = request.FILES.get('imagem')

        if(imagem):
            # Define the folder path where the image will be saved
            folder_path = os.path.join(settings.BASE_DIR, 'FlavourIt_app/static/graphics/img_recipes/')
            # Create the folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)
            # Save the file
            fs = FileSystemStorage(location=folder_path)
            file_name = fs.save(nome+".png", imagem)  # Save the file with its original name
            file_path = fs.path(file_name)  # Get the full path to the saved file
    
            #print(nome)
            #print(file_path)

        # Check if a recipe with the same name already exists
        if receita.objects.filter(nome=nome).exists():
            ingredients = valores_nutricionais.objects.all()
            utensilios=utensilio.objects.all()
            error_message = "A recipe with this name already exists. Please choose another name."
            context = {
                'error_message': error_message,
                'ingredients': ingredients,
                'utensilios': utensilios
            }
            return render(request, 'flavourit/adicionar_receita.html', context)


        user_time_obj = datetime.strptime(tempo, "%H:%M")
        user_time_formatted = user_time_obj.strftime("%H:%M:%S")
        
        receita1=receita.objects.create(
            nome=nome,
            tempo=user_time_formatted,
            instructions=instructions,
            id_Cliente=client.objects.get(id=request.user.id)
        )
        ##receita colocada na database^^

        #print(selected_ingredients)
        for ingrediente in selected_ingredients:

            idint=int(ingrediente)
            ingredient1 = valores_nutricionais.objects.get(id=idint)
            ingredient_id=valores_nutricionais.objects.get(id=ingredient1.id)

            quantity_key = f"quantity_{ingrediente}"
            unit_key = f"unit_{ingrediente}"
            quant = request.POST.get(quantity_key, 0)  # Default to 0 if not provided
            if(quant):
                quant=Decimal(quant);
            else:
                quant=0;

            unidade = request.POST.get(unit_key, '')
            #print(unidade)

            ingredient.objects.create(
                id_receita=receita1,
                id_val_Nutri=ingredient_id,
                quant=quant,
                unidade=unidade
            )
            #print(i.id_val_Nutri)


        for utensilios in selected_utensilios:

            idint=int(utensilios)
            utensilio1 = utensilio.objects.get(id=idint)
            utensilio_id=utensilio.objects.get(id=utensilio1.id)

            receita_utensilio.objects.create(
                id_receita=receita1,
                id_utensilio=utensilio_id
            )


    recipes=receita.objects.all()

    cliente=client.objects.get(id=request.user.id);
    recipes = recipes.filter(Q(id_Cliente__isnull=True) | Q(id_Cliente=cliente))

    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes})

###

def generate_recipe_pdf(request, recipe_id):
    recipe = receita.objects.get(id=recipe_id)
    ingredients = ingredient.objects.filter(id_receita=recipe).select_related('id_val_Nutri')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{recipe.nome}.pdf"'

    c = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    c.setFont("Courier-Bold", 24)
    c.drawString(100, height - 50, recipe.nome)
    c.setFont("Courier-Bold", 18)
    c.drawString(100, height - 100, "Ingredients:")

    y_position = height - 120
    c.setFont("Courier", 12)
    for ing in ingredients:
        ingredient_text = f"• {ing.quant:.2f} {ing.unidade} of {ing.id_val_Nutri.nome}"
        c.drawString(100, y_position, ingredient_text)
        y_position -= 20

    y_position -= 20

    c.setFont("Courier-Bold", 18)
    c.drawString(100, y_position, "Instructions:")

    y_position -= 30

    raw_instructions = strip_tags(recipe.instructions)
    steps = raw_instructions.split(".")

    styles = getSampleStyleSheet()
    style = styles["BodyText"]
    frame = Frame(100, 50, width - 150, y_position - 50, showBoundary=0)
    story = []
    for i, step in enumerate(steps, start=1):
        if step.strip():
            story.append(Paragraph(f"{i}. {step.strip()}.", style))
            story.append(Spacer(1, 12))

    frame.addFromList(story, c)

    c.save()
    return response


def recipe_card(request, recipe_id):
    recipe = get_object_or_404(receita, id=recipe_id)
    user_quantities = request.session.get('user_quantities', {})
    ingredients = ingredient.objects.filter(id_receita=recipe).select_related('id_val_Nutri')
    utensils = utensilio.objects.filter(receita_utensilio__id_receita=recipe)

    fallback_url = reverse('menu')

    if 'nutritional_data' in request.META.get('HTTP_REFERER', ''):
        return_url = fallback_url
    else:
        return_url = request.META.get('HTTP_REFERER', fallback_url)

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
         'return_url': return_url
    })

def receitas_favoritadas(request):

    try:
        member = client.objects.get(id=request.user.id)  # Assuming the user is logged in and request.user is available
    except:
        print("DEU ERRADO");
        return redirect(request.META.get('HTTP_REFERER', '/'))

    id_user=member.id
    recipes = receita.objects.filter(favoritado__id_Cliente=id_user)
    
    return render(request, 'flavourit/receitas_favoritadas.html', {'recipes': recipes})

def recipeCardFavorite(request):
    receita_id = request.GET['receita_id']
    
    if favoritado.objects.filter(id_Client_id = request.user.id, id_Receita_id = receita_id).exists():
        result = True
    else:
        result = False
    return render(request, 'recipe_card.html', {'results': result})

def favoritar(request):
    if request.method == "POST":
        receita_id = request.POST.get("id_receita")  # Ensure the ID is sent in the POST request
        try:
            member = client.objects.get(id=request.user.id)  # Assuming the user is logged in and request.user is available
        except:
            #print("DEU ERRADO");
            return redirect(request.META.get('HTTP_REFERER', '/'))

        favorite = favoritado.objects.filter(id_Receita_id=receita_id, id_Cliente_id=member.id).first()

        if favorite:
            favorite.delete()
            #print("FOI1")
        else:
            # If it doesn't exist, create a new favorite
            favoritado.objects.create(id_Receita_id=receita_id, id_Cliente_id=member.id)
            #print("FOI2")

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


def Account_View(request):
    if request.method == "GET":
        id_client = request.user.id
        getInfoTableClient = client.objects.get(id=id_client)
        getinfoTableUser = User.objects.get(id=id_client)
        altura = getInfoTableClient.altura
        peso = getInfoTableClient.peso
        atividade = getInfoTableClient.Atividade
        birthDate = getInfoTableClient.Birth_Date
        username = getinfoTableUser.username
        dateJoin = getinfoTableUser.date_joined
        
    return render(request, "flavourit/account_view.html", {'atividade':atividade,'altura':altura, 'peso':peso, 'birthDate':birthDate, 'user': username, 'dataEntrada':dateJoin})
        
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

    cliente=client.objects.get(id=request.user.id);
    recipes = recipes.filter(Q(id_Cliente__isnull=True) | Q(id_Cliente=cliente))

    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes})


##

## NAME search okay bro!!!!!!!
def name_search(request):
    return render(request, 'flavourit/name_search.html')

def search_by_name(request):
    query = request.GET.get('name')  # Get the search query from the GET request
    #print(query)         

    if query:
        # Filter recipes based on the name containing the query string (case-insensitive)
        recipes = receita.objects.filter(nome__icontains=query)
    else:
        recipes = receita.objects.all()  # If no query, show all recipes


    cliente=client.objects.get(id=request.user.id);
    recipes = recipes.filter(Q(id_Cliente__isnull=True) | Q(id_Cliente=cliente))

    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes})

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


    cliente=client.objects.get(id=request.user.id);
    recipes = recipes.filter(Q(id_Cliente__isnull=True) | Q(id_Cliente=cliente))

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

    cliente=client.objects.get(id=request.user.id);
    recipes = recipes.filter(Q(id_Cliente__isnull=True) | Q(id_Cliente=cliente))

    return render(request, 'flavourit/recipe_results.html', {'recipes': recipes})


def nutritional_data(request, recipe_id):
    recipe = get_object_or_404(receita, id=recipe_id)

    ingredientes = ingredient.objects.filter(id_receita=recipe).select_related('id_val_Nutri')

    fallback_url = reverse('recipe_card', args=[recipe_id])

    if 'recipe_card' in request.META.get('HTTP_REFERER', ''):
        return_url = fallback_url
    else:
        return_url = request.META.get('HTTP_REFERER', fallback_url)

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
        'return_url': return_url
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
