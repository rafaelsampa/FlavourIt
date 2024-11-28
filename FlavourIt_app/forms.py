from django.forms import ModelForm
from .models import *

class ClientForm(ModelForm):
    class Meta:
        model = client
        fields = '__all__'

class ReceitaForm(ModelForm):
    class Meta:
        model = receita
        fields = '__all__'

class ValoresNutricionaisForm(ModelForm):
    class Meta:
        model = valores_nutricionais
        fields = '__all__'
        
class UtensilioForm(ModelForm):
    class Meta:
        model = utensilio
        fields = '__all__'
        
class FavoritadoForm(ModelForm):
    class Meta:
        model = favoritado
        fields = '__all__'
        
class IngredientForm(ModelForm):
    class Meta:
        model = ingredient
        fields = '__all__'

class ReceitaUtensiio(ModelForm):
    class Meta:
        model = receita_utensilio
        fields = '__all__'
