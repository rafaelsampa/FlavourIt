from django.urls import path
from . import views

urlpatterns = [
    path('name_search/', views.receitasView, name='name_search'),
]
