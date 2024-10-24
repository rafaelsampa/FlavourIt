from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.receitasView, name='name_search')
]
