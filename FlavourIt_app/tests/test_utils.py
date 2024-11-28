from django.test import TestCase
from decimal import Decimal
from FlavourIt_app.utils import insert_recipe
from FlavourIt_app.models import receita, ingredient, valores_nutricionais, utensilio

# Esses testes abrangem:
# - Inserir receitas basicas
# - Criar receitas com múltiplos ingredientes  
# - Criar receitas com múltiplos utensílios  
# - Reutilizar valores nutricionais existentes  
# - Reutilizar utensílios existentes

class UtilsTests(TestCase):
    def test_insert_basic_recipe(self):
        nome = "Teste de Receita"
        tempo = "30min"
        instrucoes = "Teste de intrucoes"
        ingredientes = [{
            'nutrition_info': {
                'nome': 'Teste de ingredientes',
                'gordura': Decimal('5.50'),
                'carboidrato': Decimal('20.50'),
                'proteina': Decimal('10.00'),
                'porcao': Decimal('100.00'),
                'unidade': 'g'
            },
            'quantidade': Decimal('100.00'),
            'unidade': 'g'
        }]
        utensilios = [{'nome': 'Teste Utensilio'}]

        insert_recipe(nome, tempo, instrucoes, ingredientes, utensilios)
        
        # Verificacao de recceita criada
        recipe = receita.objects.get(nome=nome)
        self.assertEqual(recipe.tempo, tempo)
        self.assertEqual(recipe.instructions, instrucoes)

        # Verificacao de ingrediente criado
        ing = ingredient.objects.filter(id_receita=recipe).first()
        self.assertIsNotNone(ing)
        self.assertEqual(ing.quant, Decimal('100.00'))
        
        # Verificacao de utensilio criado
        uten = utensilio.objects.filter(nome='Teste Utensilio').first()
        self.assertIsNotNone(uten)
        
    
    def test_insert_recipe_multiple_ingredients(self):
        nome = "Receita de Multiplos ingredientes"
        tempo = "45min"
        instrucoes = "Teste de Receita com Multiplos ingredientes"
        ingredientes = [
            {
                'nutrition_info': {
                    'nome': 'Primeiro ingrediente',
                    'gordura': Decimal('5.50'),
                    'carboidrato': Decimal('20.50'),
                    'proteina': Decimal('10.00'),
                    'porcao': Decimal('100.00'),
                    'unidade': 'g'
                },
                'quantidade': Decimal('150.00'),
                'unidade': 'g'
            },
            {
                'nutrition_info': {
                    'nome': 'Segundo ingrediente',
                    'gordura': Decimal('2.50'),
                    'carboidrato': Decimal('30.50'),
                    'proteina': Decimal('5.00'),
                    'porcao': Decimal('100.00'),
                    'unidade': 'ml'
                },
                'quantidade': Decimal('200.00'),
                'unidade': 'ml'
            }
        ]
        utensilios = [{'nome': 'Utensilio 1'}, {'nome': 'Utensilio 2'}]

        insert_recipe(nome, tempo, instrucoes, ingredientes, utensilios)
        
        recipe = receita.objects.get(nome=nome)
        self.assertEqual(ingredient.objects.filter(id_receita=recipe).count(), 2)
        self.assertEqual(utensilio.objects.filter(nome__in=['Utensilio 1', 'Utensilio 2']).count(), 2)

    def test_insert_recipe_reuse_existing_nutrition(self):
        # Testa se os mesmos valores nutricionais n sao duplicados
        existing_nutrition = valores_nutricionais.objects.create(
            nome='Ingrediente Existente',
            gordura=Decimal('5.50'),
            carboidrato=Decimal('20.50'),
            proteina=Decimal('10.00'),
            porção=Decimal('100.00'),
            unidade='g'
        )

        nome = "Reutilizar Receita Nutricional"
        tempo = "20min"
        instrucoes = "Teste reutilizando nutricao"
        ingredientes = [{
            'nutrition_info': {
                'nome': 'Ingrediente Existente',
                'gordura': Decimal('5.50'),
                'carboidrato': Decimal('20.50'),
                'proteina': Decimal('10.00'),
                'porcao': Decimal('100.00'),
                'unidade': 'g'
            },
            'quantidade': Decimal('75.00'),
            'unidade': 'g'
        }]
        utensilios = [{'nome': 'Teste Utensilio'}]

        insert_recipe(nome, tempo, instrucoes, ingredientes, utensilios)
        
        # Verificar se nenhum novo objeto de nutrição foi criado
        self.assertEqual(
            valores_nutricionais.objects.filter(nome='Ingrediente Existente').count(),
            1
        )

    def test_insert_recipe_reuse_existing_utensil(self):
        
        # Testar se o mesmo utensílio não é duplicado
        existing_utensil = utensilio.objects.create(nome='Utensilio Existente')

        nome = "Reutilizar Receita com Utensilio"
        tempo = "25min"
        instrucoes = "Teste reutilizando utensilio"
        ingredientes = [{
            'nutrition_info': {
                'nome': 'Testar ingrediente',
                'gordura': Decimal('5.50'),
                'carboidrato': Decimal('20.50'),
                'proteina': Decimal('10.00'),
                'porcao': Decimal('100.00'),
                'unidade': 'g'
            },
            'quantidade': Decimal('100.00'),
            'unidade': 'g'
        }]
        utensilios = [{'nome': 'Utensilio Existente'}]

        insert_recipe(nome, tempo, instrucoes, ingredientes, utensilios)
        
        # Verificar
        self.assertEqual(
            utensilio.objects.filter(nome='Utensilio Existente').count(),
            1
        )
        
        
        
