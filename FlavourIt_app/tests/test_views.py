



from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from decimal import Decimal
from FlavourIt_app.models import (
    receita, valores_nutricionais, utensilio, client
)


class AuthViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='usuarioteste',
            email='test@maluco.com',
            password='senhateste123'
        )

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'usuarioteste',
            'password': 'senhateste123'
        })
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        self.client.login(username='usuarioteste', password='senhateste123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_authentication(self):
        login_successful = self.client.login(
            username='usuarioteste',
            password='senhateste123'
        )
        self.assertTrue(login_successful)
        
# Acabou casos de login/sigup

class SearchViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.recipe = receita.objects.create(
            nome="Teste da Receita",
            tempo="30min",
            instructions="Teste de instrucoes"
        )

    def test_search_by_name(self):
        response = self.client.get(
            reverse('search_by_name'),
            {'name': 'Test'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teste da Receita")

    def test_search_by_ingredients(self):
        ingredient = valores_nutricionais.objects.create(
            nome="Teste de ingredientes",
            gordura=Decimal('5.50'),
            carboidrato=Decimal('20.50'),
            proteina=Decimal('10.00'),
            porção=Decimal('100.00'),
            unidade='g'
        )
        response = self.client.get(
            reverse('ingredient_filter')
        )
        self.assertEqual(response.status_code, 200)

    def test_search_by_tools(self):
        tool = utensilio.objects.create(nome="Teste de utensilio")
        response = self.client.get(
            reverse('tool_filter')
        )
        self.assertEqual(response.status_code, 200)

class RecipeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.recipe = receita.objects.create(
            nome="Teste da Receita",
            tempo="30min",
            instructions="Teste de instrucoes"
        )

    def test_recipe_card_view(self):
        response = self.client.get(
            reverse('recipe_card', args=[self.recipe.id])
        )
        self.assertEqual(response.status_code, 200)
        




class RecipeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Construir uma receita teste
        self.recipe = receita.objects.create(
            nome="Teste da Receita",
            tempo="30min",
            instructions="Teste de instrucoes"
        )

    def test_recipe_search(self):
        # Verificar se foi realemnte criada, pq ta dando merda
        saved_recipe = receita.objects.get(nome="Teste da Receita")
        self.assertIsNotNone(saved_recipe)
        
        # WARING ============
        # Busca
        response = self.client.get(
            reverse('search_by_name'), 
            {'name': 'Teste da Receita'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teste da Receita")

    def test_recipe_card(self):
        response = self.client.get(reverse('recipe_card', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)



class IngredientFilterTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.ingredient = valores_nutricionais.objects.create(
            nome="Teste de ingredientes",
            gordura=Decimal('5.50'),
            carboidrato=Decimal('20.50'),
            proteina=Decimal('10.00'),
            porção=Decimal('100.00'),
            unidade="g"
        )

    
    def test_ingredient_filter(self):
        response = self.client.get(reverse('ingredient_filter'))
        self.assertEqual(response.status_code, 200)


