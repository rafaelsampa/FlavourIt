from decimal import Decimal
from django.test import TestCase
from FlavourIt_app.models import (
    client, receita, 
    valores_nutricionais, utensilio,
    ingredient
)

class ClientModelTest(TestCase):
    def setUp(self):
        self.client_data = client.objects.create(
            nome="Teste do Cliente",
            altura=Decimal('1.75'),
            peso=Decimal('70.50'),
            Atividade="Moderada"
        )
    
    def test_client_creation(self):
        self.assertEqual(self.client_data.nome, "Teste do Cliente")
        self.assertEqual(float(self.client_data.altura), 1.75)
        self.assertEqual(float(self.client_data.peso), 70.5)
        self.assertEqual(self.client_data.Atividade, "Moderada")

class ReceitaModelTests(TestCase):
    def setUp(self):
        self.receita_data = receita.objects.create(
            nome="Teste de Receita",
            tempo="00:30:00",
            instructions="Teste de instrucoes"
        )
    
    def test_receita_creation(self):
        self.assertEqual(self.receita_data.nome, "Teste de Receita")
        self.assertEqual(self.receita_data.tempo, "00:30:00")
        self.assertEqual(self.receita_data.instructions, "Teste de instrucoes")
    
    def test_receita_str(self):
        self.assertEqual(str(self.receita_data), "Teste de Receita")
    
    def test_image_url_property(self):
        image_url = self.receita_data.image_url
        self.assertTrue(isinstance(image_url, str))

class ValoresNutricionaisModelTests(TestCase):
    def setUp(self):
        self.valores = valores_nutricionais.objects.create(
            nome="Teste dos Nutrientes",
            gordura=Decimal('5.50'),    # 4 vez valor decimal errado
            carboidrato=Decimal('20.50'), 
            proteina=Decimal('10.00'),    
            porção=Decimal('100.00'),      
            unidade="g"
        )
    
    def test_valores_nutricionais_creation(self):
        self.assertEqual(self.valores.nome, "Teste dos Nutrientes")
        self.assertEqual(float(self.valores.gordura), 5.5)
        self.assertEqual(float(self.valores.carboidrato), 20.5)
        self.assertEqual(float(self.valores.proteina), 10.0)
        self.assertEqual(float(self.valores.porção), 100.0)
        self.assertEqual(self.valores.unidade, "g")

class UtensilioModelTests(TestCase):
    def setUp(self):
        self.utensilio_data = utensilio.objects.create(
            nome="Teste utensilios"
        )
    
    def teste_utensilio_creation(self):
        self.assertEqual(self.utensilio_data.nome, "Teste utensilios")
    
    def test_image_url_property(self):
        image_url = self.utensilio_data.image_url
        self.assertTrue(isinstance(image_url, str))

class IngredientModelTests(TestCase):
    def setUp(self):
        self.receita_data = receita.objects.create(
            nome="Teste de Receita",
            tempo="00:30:00",
            instructions="Teste das instrucoes"
        )
        self.valores = valores_nutricionais.objects.create(
            nome="Teste nutriente",
            gordura=5.50,
            carboidrato=20.50,
            proteina=10.00,
            porção=99.99,
            unidade="g"
        )
        self.ingredient_data = ingredient.objects.create(
            nome="Teste de ingrediente",
            id_receita=self.receita_data,
            id_val_Nutri=self.valores,
            quant=50.00,  # 6 vez - mudanca de valor decimal
            unidade="g"
        )
