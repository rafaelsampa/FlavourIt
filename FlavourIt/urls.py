"""
URL configuration for FlavourIt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from FlavourIt_app import views

urlpatterns = [
    path('',views.menu,name='menu'),
    path('time_filter/',views.time_filter,name='time_filter'),
    path('search/',views.name_search,name='name_search'),
    path('time_filter/',views.time_filter,name='time_filter'),
    path('recipe_card/',views.recipe_card,name='recipe_card'),
    
    path('name_search/', views.name_search, name='name_search'),
    path('search_by_name/', views.search_by_name, name='search_by_name'),

    path('results/',views.recipe_results,name='recipe_results'),

    path('ingredient_filter/',views.ingredient_filter,name='ingredient_filter'),
    path('search_by_ingredients/', views.search_by_ingredients, name='search_by_ingredients'),

    path('tool_filter/',views.tool_filter,name='tool_filter'),
    path('search_by_tools/', views.search_by_tools, name='search_by_tools'),

]
