from decimal import Decimal
from .models import receita, ingredient, utensilio, valores_nutricionais, receita_utensilio

def insert_recipe(nome, tempo, instrucoes, ingredientes, utensilios):
    receita1 = receita.objects.create(nome=nome, tempo=tempo, instructions=instrucoes)

    for ingrediente in ingredientes:
        nutrition_info = ingrediente['nutrition_info']
        nutrition, created= valores_nutricionais.objects.get_or_create(
            nome=nutrition_info['nome'],
            gordura = nutrition_info['gordura'],
            carboidrato = nutrition_info['carboidrato'],
            proteina = nutrition_info['proteina'],
            porção = nutrition_info['porcao'],
            unidade=nutrition_info['unidade'],
        )

        ingredient.objects.create(
            id_receita=receita1,
            id_val_Nutri=nutrition,
            quant=ingrediente['quantidade'],
            unidade=ingrediente['unidade']
        )

    for utensilio1 in utensilios:
        utensilio_obj, created= utensilio.objects.get_or_create(nome=utensilio1['nome'])
        receita_utensilio.objects.create(id_receita=receita1, id_utensilio=utensilio_obj)
