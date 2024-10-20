from django.shortcuts import render

def menu(request):
    return render(request, 'flavourit/menu.html')

def ingredient_filter(request):
    return render(request, 'flavourit/ingredient_filter.html')

def tool_filter(request):
    return render(request, 'flavourit/tool_filter.html')

def time_filter(request):
    return render(request, 'flavourit/time_filter.html')
