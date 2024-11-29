from django.core.management.base import BaseCommand
from FlavourIt_app.utils import insert_recipe
#from FlavourIt_app.receitas import arrozbranco
#from FlavourIt_app.receitas import arrozdoce
#from FlavourIt_app.receitas import bacalhauabras
#from FlavourIt_app.receitas import batatasuica
#from FlavourIt_app.receitas import biscoitodeaveiacomhortela
#from FlavourIt_app.receitas import bolodecenoura
#from FlavourIt_app.receitas import bolodechocolate
#from FlavourIt_app.receitas import bolodefuba
#from FlavourIt_app.receitas import brigadeiro
#from FlavourIt_app.receitas import cachorroquente
#from FlavourIt_app.receitas import caldinhodefeijao
#from FlavourIt_app.receitas import ceviche
#from FlavourIt_app.receitas import chilicomcarne
#from FlavourIt_app.receitas import churrasco
#from FlavourIt_app.receitas import coxinha
#from FlavourIt_app.receitas import cremebrulee
#from FlavourIt_app.receitas import crepe
#from FlavourIt_app.receitas import docedeleite
#from FlavourIt_app.receitas import empanadas
#from FlavourIt_app.receitas import escondidinhodecarne
#from FlavourIt_app.receitas import macarraoalhoeoleo
#from FlavourIt_app.receitas import massadepanqueca
#from FlavourIt_app.receitas import omelete
#from FlavourIt_app.receitas import panquecadebanana
#from FlavourIt_app.receitas import pipoca
#from FlavourIt_app.receitas import puredebatata
#from FlavourIt_app.receitas import batatasuica

from FlavourIt_app.receitas import (
    arrozbranco,
    batatasuica,
    biscoitodeaveiacomhortela,
    brigadeiro,
    macarraoalhoeoleo,
    massadepanqueca,
    omelete,
    panquecadebanana,
    pipoca,
    puredebatata,
    frangoassado,
    lasanha,
    quichedequeijo,
    coxinha,
    moquecadepeixe,
    feijoada,
    tapioca,
    bolodecenoura,
    escondidinhodecarne,
    caldinhodefeijao,
    sopadeabobora,
    polentacremosa,
    pizzamarguerita,
    arrozdoce,
    saladadequinoa,
    ceviche,
    risotodecogumelos,
    hamburger,
    tortadelimao,
    churrasco,
    paella,
    yakissoba,
    strogonoffdefrango,
    bolodechocolate,
    esfirraaberta,
    docedeleite,
    bacalhauabras,
    cremebrulee,
    tacos,
    cachorroquente,
    empanadas,
    chilicomcarne,
    lentilharefogada,
    gnocchi,
    bolodefuba,
    sushi,
    minestrone,
    panacotta,
    crepe,
)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #insert_recipe('Arroz branco', '00:20:00', '1-Rinse the rice thoroughly until the water runs clear.<br>2-In a pot, heat oil and sauté garlic until fragrant.<br>3-Add rice, stir briefly, then add boiling water and salt. Cover and cook on low heat until the water is absorbed.', arrozbranco.ingredientes, arrozbranco.utensilios)
        #insert_recipe('Batata Suica', '00:25:00', '1-Grate raw potatoes, squeeze out excess liquid, and season with salt and pepper.<br>2-Heat butter in a non-stick skillet, add a layer of potatoes, and cook until golden.<br>3-Flip carefully, cook the other side, and serve hot.', batatasuica.ingredientes, batatasuica.utensilios)
        #insert_recipe('Biscoito de Aveia com Hortela', '00:15:00', '1-Mix oats, flour, chopped mint, and sugar in a bowl.<br>2-Add melted butter and milk, stirring until combined.<br>3-Shape into cookies and bake at 180°C until golden.', biscoitodeaveiacomhortela.ingredientes, biscoitodeaveiacomhortela.utensilios)
        #insert_recipe('Brigadeiro', '00:15:00', '1-Mix condensed milk, cocoa powder, and butter in a saucepan.<br>2-Cook over medium heat, stirring constantly, until the mixture thickens and pulls away from the sides of the pan.<br>3-Allow to cool, then shape into balls and roll in chocolate sprinkles.', brigadeiro.ingredientes, brigadeiro.utensilios)
        #insert_recipe('Macarrao alho e oleo', '00:15:00', '1-Cook spaghetti in boiling salted water until al dente.<br>2-In a skillet, sauté garlic in olive oil until golden.<br>3-Toss the drained spaghetti in the skillet with garlic and oil. Season with salt, pepper, and parsley.', macarraoalhoeoleo.ingredientes, macarraoalhoeoleo.utensilios)
        #insert_recipe('Massa de panqueca', '00:10:00', '1-Mix flour, milk, eggs, and a pinch of salt until smooth.<br>2-Heat a non-stick skillet and pour a small amount of batter, swirling to coat the bottom.<br>3-Cook until edges lift, flip, and cook briefly on the other side.', massadepanqueca.ingredientes, massadepanqueca.utensilios)
        #insert_recipe('Omelete', '00:10:00', '1-Beat eggs with a pinch of salt, pepper, and optional fillings like cheese or vegetables.<br>2-Heat butter in a skillet, pour in the eggs, and let set.<br>3-Fold the omelet in half and cook briefly until the cheese melts.', omelete.ingredientes, omelete.utensilios)
        #insert_recipe('Panqueca de Banana', '00:10:00', '1-Mash bananas and mix with eggs, flour, and a pinch of cinnamon.<br>2-Heat a non-stick skillet and pour small portions of batter.<br>3-Cook until bubbles form, flip, and cook the other side.', panquecadebanana.ingredientes, panquecadebanana.utensilios)
        #insert_recipe('Pipoca', '00:05:00', '1-Heat oil in a large pot and add popcorn kernels.<br>2-Cover the pot, leaving a small vent, and shake occasionally.<br>3-Once popping slows, remove from heat, season, and serve.', pipoca.ingredientes, pipoca.utensilios)
        insert_recipe('Pure de Batata', '00:35:00', '1-Boil peeled and cubed potatoes in salted water until tender.<br>2-Mash the potatoes with butter, warm milk, salt, and pepper until smooth.<br>3-Serve hot as a side dish.', puredebatata.ingredientes_pure, puredebatata.utensilios_pure)

        ##
        #insert_recipe('Frango Assado', '01:20:00', '1-Preheat oven to 200°C (400°F).<br>2-Season the chicken with salt, pepper, garlic, and herbs.<br>3-Place in a baking dish and roast until golden brown and juices run clear.', frangoassado.ingredientes, frangoassado.utensilios)
        #insert_recipe('Lasanha', '01:30:00', '1-Cook lasagna noodles until al dente.<br>2-Prepare the meat sauce by sautéing garlic, onions, and ground beef, then adding tomato sauce.<br>3-Layer noodles, sauce, and cheese in a baking dish. Bake at 180°C until bubbly.', lasanha.ingredientes, lasanha.utensilios)
        #insert_recipe('Quiche de Queijo', '00:50:00', '1-Mix flour and butter to form a dough, then press into a pie dish.<br>2-Whisk eggs, cream, cheese, and seasoning, then pour into the crust.<br>3-Bake at 180°C until set and golden.', quichedequeijo.ingredientes, quichedequeijo.utensilios)

        #insert_recipe('Coxinha', '01:10:00', '1-Boil chicken with seasoning, then shred.<br>2-Make dough with flour and broth, then wrap around the chicken filling.<br>3-Bread and deep-fry until golden brown.', coxinha.ingredientes, coxinha.utensilios)

        #insert_recipe('Moqueca de Peixe', '00:40:00', '1-Marinate fish in lime juice, garlic, and salt.<br>2-Layer fish, peppers, onions, and tomatoes in a pot.<br>3-Cook with coconut milk until the fish is tender and the flavors meld.', moquecadepeixe.ingredientes, moquecadepeixe.utensilios)

        #insert_recipe('Feijoada', '02:00:00', '1-Soak black beans overnight and cook until tender.<br>2-Sauté garlic, onions, and pork cuts, then add to the beans.<br>3-Simmer with spices and serve with rice, orange slices, and greens.', feijoada.ingredientes, feijoada.utensilios)

        #insert_recipe('Tapioca', '00:10:00', '1-Heat a non-stick pan and sprinkle tapioca flour evenly to form a pancake.<br>2-Add desired fillings like cheese, ham, or coconut.<br>3-Fold in half and serve warm.', tapioca.ingredientes, tapioca.utensilios)

        #insert_recipe('Bolo de Cenoura', '00:50:00', '1-Blend carrots, oil, and eggs until smooth.<br>2-Mix with sugar, flour, and baking powder, then pour into a greased pan.<br>3-Bake at 180°C until a toothpick comes out clean.', bolodecenoura.ingredientes, bolodecenoura.utensilios)

        #insert_recipe('Escondidinho de Carne', '00:45:00', '1-Prepare mashed potatoes as a base.<br>2-Cook ground beef with onions, garlic, and tomato sauce.<br>3-Layer beef and mashed potatoes in a baking dish, top with cheese, and bake.', escondidinhodecarne.ingredientes, escondidinhodecarne.utensilios)

        #insert_recipe('Caldinho de Feijão', '00:30:00', '1-Cook beans with garlic, onions, and seasoning.<br>2-Blend until smooth, adding broth to adjust consistency.<br>3-Serve hot with croutons or bacon bits as garnish.', caldinhodefeijao.ingredientes, caldinhodefeijao.utensilios)

        #insert_recipe('Sopa de Abóbora', '00:40:00', '1-Peel and cube the pumpkin.<br>2-Sauté onions and garlic in a pot, then add pumpkin and broth.<br>3-Cook until tender, blend until smooth, and season to taste.', sopadeabobora.ingredientes, sopadeabobora.utensilios)

        #insert_recipe('Polenta Cremosa', '00:30:00', '1-Bring water or broth to a boil.<br>2-Gradually whisk in cornmeal, stirring constantly.<br>3-Cook until thickened, then mix in butter and cheese.', polentacremosa.ingredientes, polentacremosa.utensilios)

        #insert_recipe('Pizza Marguerita', '01:20:00', '1-Prepare pizza dough and let it rise.<br>2-Spread tomato sauce over the dough and top with mozzarella and basil.<br>3-Bake at 220°C until crust is golden and cheese is melted.', pizzamarguerita.ingredientes, pizzamarguerita.utensilios)

        #insert_recipe('Arroz Doce', '00:50:00', '1-Cook rice with water until almost tender.<br>2-Add milk, sugar, and cinnamon, and simmer until creamy.<br>3-Serve warm or chilled with cinnamon on top.', arrozdoce.ingredientes, arrozdoce.utensilios)

        #insert_recipe('Salada de Quinoa', '00:25:00', '1-Cook quinoa in boiling water until fluffy.<br>2-Mix with chopped vegetables, olive oil, lemon juice, and herbs.<br>3-Chill before serving.', saladadequinoa.ingredientes, saladadequinoa.utensilios)

        #insert_recipe('Ceviche', '00:20:00', '1-Dice fresh fish and marinate in lime juice.<br>2-Add onions, chili peppers, cilantro, and salt.<br>3-Chill before serving with tortilla chips or crackers.', ceviche.ingredientes, ceviche.utensilios)

        #insert_recipe('Risoto de Cogumelos', '00:45:00', '1-Sauté mushrooms, garlic, and onions in butter.<br>2-Add arborio rice, stirring until coated.<br>3-Slowly add broth, stirring constantly, until rice is creamy and tender.', risotodecogumelos.ingredientes, risotodecogumelos.utensilios)

        #insert_recipe('Hambúrguer Caseiro', '00:30:00', '1-Mix ground beef with salt, pepper, and optional spices.<br>2-Shape into patties and cook on a grill or skillet.<br>3-Assemble with buns, lettuce, cheese, and condiments.', hamburguercaseiro.ingredientes, hamburguercaseiro.utensilios)

        #insert_recipe('Torta de Limão', '01:10:00', '1-Make a crust with crushed biscuits and butter.<br>2-Mix condensed milk, lime juice, and cream, then pour into the crust.<br>3-Chill for 2 hours and serve with whipped cream.', tortadelimao.ingredientes, tortadelimao.utensilios)

        #insert_recipe('Churrasco', '01:30:00', '1-Season meats with coarse salt.<br>2-Grill over charcoal until desired doneness.<br>3-Serve with chimichurri and sides like farofa or salad.', churrasco.ingredientes, churrasco.utensilios)

        #insert_recipe('Paella', '01:20:00', '1-Sauté onions, garlic, and bell peppers in olive oil.<br>2-Add rice, broth, saffron, and seafood or chicken.<br>3-Cook until the rice absorbs the liquid.', paella.ingredientes, paella.utensilios)

        #insert_recipe('Yakissoba', '00:35:00', '1-Boil noodles and set aside.<br>2-Stir-fry vegetables, meat, and soy sauce in a wok.<br>3-Add noodles, toss, and serve hot.', yakissoba.ingredientes, yakissoba.utensilios)

        #insert_recipe('Strogonoff de Frango', '00:30:00', '1-Sauté chicken with onions and garlic.<br>2-Add tomato sauce, cream, and mushrooms.<br>3-Simmer and serve with rice and potato sticks.', strogonoffdefrango.ingredientes, strogonoffdefrango.utensilios)

        #insert_recipe('Bolo de Chocolate', '00:50:00', '1-Mix flour, sugar, cocoa, eggs, and butter.<br>2-Pour into a greased pan and bake at 180°C.<br>3-Top with chocolate ganache.', bolodechocolate.ingredientes, bolodechocolate.utensilios)

        #insert_recipe('Esfirra Aberta', '01:20:00', '1-Make a yeast dough and let it rise.<br>2-Shape into discs, top with ground beef filling.<br>3-Bake at 200°C until golden.', esfirraaberta.ingredientes, esfirraaberta.utensilios)

        #insert_recipe('Doce de Leite', '01:00:00', '1-Cook milk and sugar over low heat, stirring constantly.<br>2-Simmer until it thickens and caramelizes.<br>3-Cool before serving.', docedeleite.ingredientes, docedeleite.utensilios)

        #insert_recipe('Bacalhau à Brás', '00:50:00', '1-Soak and shred salted cod.<br>2-Sauté onions, then mix with cod, eggs, and fried potatoes.<br>3-Garnish with olives and parsley.', bacalhauabras.ingredientes, bacalhauabras.utensilios)

        #insert_recipe('Creme Brulée', '01:20:00', '1-Whisk cream, sugar, and egg yolks, then bake in ramekins in a water bath.<br>2-Chill and sprinkle sugar on top.<br>3-Caramelize with a torch before serving.', cremebrulee.ingredientes, cremebrulee.utensilios)

        #insert_recipe('Tacos', '00:30:00', '1-Cook seasoned ground beef or chicken.<br>2-Fill tortillas with meat, lettuce, cheese, and salsa.<br>3-Serve with guacamole or sour cream.', tacos.ingredientes, tacos.utensilios)

        #insert_recipe('Cachorro-Quente', '00:15:00', '1-Cook hot dogs in boiling water.<br>2-Assemble with buns, ketchup, mustard, and optional toppings.<br>3-Serve immediately.', cachorroquente.ingredientes, cachorroquente.utensilios)

        #insert_recipe('Empanadas', '01:00:00', '1-Make a dough and prepare a meat or vegetable filling.<br>2-Fill, fold, and seal into half-moon shapes.<br>3-Bake at 200°C until golden.', empanadas.ingredientes, empanadas.utensilios)

        #insert_recipe('Chili con Carne', '00:50:00', '1-Cook ground beef with onions, garlic, and spices.<br>2-Add beans, tomatoes, and simmer.<br>3-Serve with rice or tortilla chips.', chiliconcarne.ingredientes, chiliconcarne.utensilios)

        #insert_recipe('Lentilha Refogada', '00:40:00', '1-Cook lentils until tender.<br>2-Sauté onions, garlic, and spices, then mix with lentils.<br>3-Serve as a side or over rice.', lentilharefogada.ingredientes, lentilharefogada.utensilios)

        #insert_recipe('Gnocchi', '01:00:00', '1-Mix mashed potatoes, flour, and egg to form a dough.<br>2-Shape into rolls, cut into pieces, and boil.<br>3-Serve with sauce of choice.', gnocchi.ingredientes, gnocchi.utensilios)

        #insert_recipe('Bolo de Fubá', '00:50:00', '1-Mix cornmeal, sugar, milk, eggs, and butter.<br>2-Pour into a greased pan and bake at 180°C.<br>3-Serve with coffee or tea.', bolodefuba.ingredientes, bolodefuba.utensilios)

        #insert_recipe('Sushi', '01:30:00', '1-Cook sushi rice and season with vinegar.<br>2-Slice fresh fish and vegetables.<br>3-Assemble rolls with nori, rice, and fillings.', sushi.ingredientes, sushi.utensilios)

        #insert_recipe('Minestrone', '00:50:00', '1-Sauté onions, garlic, and vegetables.<br>2-Add broth, beans, and pasta, and simmer until tender.<br>3-Season to taste and serve with grated cheese.', minestrone.ingredientes, minestrone.utensilios)

        #insert_recipe('Panna Cotta', '00:20:00', '1-Heat cream, sugar, and gelatin until dissolved.<br>2-Pour into molds and chill until set.<br>3-Serve with fruit sauce.', pannacotta.ingredientes, pannacotta.utensilios)

        #insert_recipe('Crepe', '00:20:00', '1-Mix flour, milk, eggs, and a pinch of salt to form batter.<br>2-Cook thin layers in a non-stick pan.<br>3-Fill with sweet or savory fillings.', crepe.ingredientes, crepe.utensilios)