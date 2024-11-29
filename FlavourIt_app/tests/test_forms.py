from django.test import TestCase
from FlavourIt_app.forms import IngredientForm, FavoritadoForm
from FlavourIt_app.models import receita, client, valores_nutricionais

class Teste_do_forms(TestCase):
    def setUp(self):
        self.recipe = receita.objects.create(
            nome="Teste da Receita",
            tempo="30min",
            instructions="Teste de instrucoes"
        )
        self.client_data = client.objects.create(
            nome="Teste Cliente Joaozinho",
            altura=1.75,
            peso=70.5,
            Atividade="Moderada"
        )
        self.nutrition = valores_nutricionais.objects.create(
            nome="Teste de Nutricao",
            gordura=5.5,
            carboidrato=20.5,
            proteina=10.0,
            porção=100.0,
            unidade="g"
        )

    def teste_forms_ingrediente_valido(self):
        form_data = {
            'id_receita': self.recipe,
            'id_val_Nutri': self.nutrition,
            'quant': 100.00,
            'unidade': 'g'
        }
        form = IngredientForm(data=form_data)
        print(form.errors)  # Vamo ver oq ta dando errado
        self.assertTrue(form.is_valid())

    def teste_favorito_form_valido(self):
        form_data = {
            'id_Cliente': self.client_data,
            'id_Receita': self.recipe 
        }
        form = FavoritadoForm(data=form_data)
        print(form.errors) # Vamo ver isso
        self.assertTrue(form.is_valid())

