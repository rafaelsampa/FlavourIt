from django.core.management.base import BaseCommand
from FlavourIt_app.utils import insert_recipe
from FlavourIt_app.receitas import arrozbranco
from FlavourIt_app.receitas import biscoitodeaveiacomhortela
from FlavourIt_app.receitas import brigadeiro
from FlavourIt_app.receitas import macarraoalhoeoleo
from FlavourIt_app.receitas import massadepanqueca
from FlavourIt_app.receitas import omelete
from FlavourIt_app.receitas import panquecadebanana
from FlavourIt_app.receitas import pipoca
from FlavourIt_app.receitas import puredebatata
from FlavourIt_app.receitas import batatasuica

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #insert_recipe('Arroz branco', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', arrozbranco.ingredientes, arrozbranco.utensilios)
        #insert_recipe('Batata Suica', '00:25:00', '1-muchotexto<br>2-muchotexto<br>3-muchotexto,l.lk', batatasuica.ingredientes, batatasuica.utensilios)
        #insert_recipe('Biscoito de Aveia com Hortela', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', biscoitodeaveiacomhortela.ingredientes, biscoitodeaveiacomhortela.utensilios)
        #insert_recipe('Brigadeiro', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', brigadeiro.ingredientes, brigadeiro.utensilios)
        #insert_recipe('Macarrao alho e oleo', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', macarraoalhoeoleo.ingredientes, macarraoalhoeoleo.utensilios)
        #insert_recipe('Massa de panqueca', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', massadepanqueca.ingredientes, massadepanqueca.utensilios)
        #insert_recipe('Omelete', '00:35:00', '1-muchotexto<br>2-muchotexto<br>3-muchotexto,l.lk', omelete.ingredientes, omelete.utensilios)
        #insert_recipe('Panqueca de Banana', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', panquecadebanana.ingredientes, panquecadebanana.utensilios)
        #insert_recipe('Pipoca', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', pipoca.ingredientes, pipoca.utensilios)
        insert_recipe('Pure de Batata', '00:35:00', '1-muchotexto<br>2-muchotexto<br>3-muchotexto,l.lk', puredebatata.ingredientes_pure, puredebatata.utensilios_pure)