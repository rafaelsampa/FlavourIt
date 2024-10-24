from django.forms import ModelForm
from .models import *

class ClientForm(ModelForm):
    class meta:
        model = client
        fields = '__all__'

class ReceitaForm(ModelForm):
    class meta:
        model = receita
        fields = '__all__'

class ValoresNutricionaisForm(ModelForm):
    class meta:
        model = valores_nutricionais
        fields = '__all__'
        
class UtensilioForm(ModelForm):
    class meta:
        model = utensilio
        fields = '__all__'

class FavoritadoForm(ModelForm):
    class meta:
        model = favoritado
        fields = '__all__'

class IngredientForm(ModelForm):
    class meta:
        model = ingredient
        fields = '__all__'
        
class ReceitaUtensilioForm(ModelForm):
    class meta:
        model = receita_utensilio
        fields = '__all__'