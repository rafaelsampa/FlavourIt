from django.shortcuts import render
from .forms import *

def menu(request):
    return render(request, 'flavourit/menu.html')

def ingredient_filter(request):
    return render(request, 'flavourit/ingredient_filter.html')

def tool_filter(request):
    return render(request, 'flavourit/tool_filter.html')

def time_filter(request):
    return render(request, 'flavourit/time_filter.html')

def recipe_results(request):
    return render(request, 'flavourit/recipe_results.html')

def name_search(request):
    return render(request, 'flavourit/name_search.html')

def recipe_card(request):
    return render(request, 'flavourit/recipe_card.html')

def name_search(request):
    return render(request, 'flavourit/name_search.html')

def receitas(request):
    form = receita.objects.all()
    
    return render(request, 'name_search.html', {'Receitas':form})