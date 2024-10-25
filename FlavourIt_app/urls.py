from django.urls import path
from . import views

urlpatterns = [
    path('name_search/?', views.receita, name='name_search'),
]
