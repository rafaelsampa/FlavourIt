from django.core.management.base import BaseCommand
from FlavourIt_app.utils import insert_recipe
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
    hamburguer,
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
        insert_recipe('Arroz branco', '00:20:00', '<li>Rinse the rice thoroughly until the water runs clear.In a pot, heat oil and sauté garlic until fragrant.<li>Add rice, stir liiefly, then add boiling water and salt. Cover and cook on low heat until the water is absorbed.', arrozbranco.ingredientes, arrozbranco.utensilios)
        insert_recipe('Batata Suica', '00:25:00', 'Grate raw potatoes, squeeze out excess liquid, and season with salt and pepper.<li>Heat butter in a non-stick skillet, add a layer of potatoes, and cook until golden.<li>Flip carefully, cook the other side, and serve hot.', batatasuica.ingredientes, batatasuica.utensilios)
        insert_recipe('Biscoito de Aveia com Hortela', '00:15:00', 'Mix oats, flour, chopped mint, and sugar in a bowl.<li>Add melted butter and milk, stirring until combined.<li>Shape into cookies and bake at 180°C until golden.', biscoitodeaveiacomhortela.ingredientes, biscoitodeaveiacomhortela.utensilios)
        insert_recipe('Brigadeiro', '00:15:00', 'Mix condensed milk, cocoa powder, and butter in a saucepan.<li>Cook over medium heat, stirring constantly, until the mixture thickens and pulls away from the sides of the pan.<li>Allow to cool, then shape into balls and roll in chocolate sprinkles.', brigadeiro.ingredientes, brigadeiro.utensilios)
        insert_recipe('Macarrao alho e oleo', '00:15:00', '<li>Cook spaghetti in boiling salted water until al dente.<li>In a skillet, sauté garlic in olive oil until golden.<li>Toss the drained spaghetti in the skillet with garlic and oil. Season with salt, pepper, and parsley.', macarraoalhoeoleo.ingredientes, macarraoalhoeoleo.utensilios)
        insert_recipe('Massa de panqueca', '00:10:00', '<li>Mix flour, milk, eggs, and a pinch of salt until smooth.<li>Heat a non-stick skillet and pour a small amount of batter, swirling to coat the bottom.<li>Cook until edges lift, flip, and cook liiefly on the other side.', massadepanqueca.ingredientes, massadepanqueca.utensilios)
        insert_recipe('Omelete', '00:10:00', '<li>Beat eggs with a pinch of salt, pepper, and optional fillings like cheese or vegetables.<li>Heat butter in a skillet, pour in the eggs, and let set.<li>Fold the omelet in half and cook liiefly until the cheese melts.', omelete.ingredientes, omelete.utensilios)
        insert_recipe('Panqueca de Banana', '00:10:00', '<li>Mash bananas and mix with eggs, flour, and a pinch of cinnamon.<li>Heat a non-stick skillet and pour small portions of batter.<li>Cook until bubbles form, flip, and cook the other side.', panquecadebanana.ingredientes, panquecadebanana.utensilios)
        insert_recipe('Pipoca', '00:05:00', '<li>Heat oil in a large pot and add popcorn kernels.<li>Cover the pot, leaving a small vent, and shake occasionally.<li>Once popping slows, remove from heat, season, and serve.', pipoca.ingredientes, pipoca.utensilios)
        insert_recipe('Pure de Batata', '00:35:00', '<li>Boil peeled and cubed potatoes in salted water until tender.<li>Mash the potatoes with butter, warm milk, salt, and pepper until smooth.<li>Serve hot as a side dish.', puredebatata.ingredientes_pure, puredebatata.utensilios_pure)


        insert_recipe('Frango Assado', '01:20:00', '<li>Preheat oven to 200°C (400°F).<li>Season the chicken with salt, pepper, garlic, and herbs.<li>Place in a baking dish and roast until golden liown and juices run clear.', frangoassado.ingredientes, frangoassado.utensilios)
        insert_recipe('Lasanha', '01:30:00', '<li>Cook lasagna noodles until al dente.<li>Prepare the meat sauce by sautéing garlic, onions, and ground beef, then adding tomato sauce.<li>Layer noodles, sauce, and cheese in a baking dish. Bake at 180°C until bubbly.', lasanha.ingredientes, lasanha.utensilios)
        insert_recipe('Quiche de Queijo', '00:50:00', '<li>Mix flour and butter to form a dough, then press into a pie dish.<li>Whisk eggs, cream, cheese, and seasoning, then pour into the crust.<li>Bake at 180°C until set and golden.', quichedequeijo.ingredientes, quichedequeijo.utensilios)

        insert_recipe('Coxinha', '01:10:00', '<li>Boil chicken with seasoning, then shred.<li>Make dough with flour and lioth, then wrap around the chicken filling.<li>liead and deep-fry until golden liown.', coxinha.ingredientes, coxinha.utensilios)

        insert_recipe('Moqueca de Peixe', '00:40:00', '<li>Marinate fish in lime juice, garlic, and salt.<li>Layer fish, peppers, onions, and tomatoes in a pot.<li>Cook with coconut milk until the fish is tender and the flavors meld.', moquecadepeixe.ingredientes, moquecadepeixe.utensilios)

        insert_recipe('Feijoada', '02:00:00', '<li>Soak black beans overnight and cook until tender.<li>Sauté garlic, onions, and pork cuts, then add to the beans.<li>Simmer with spices and serve with rice, orange slices, and greens.', feijoada.ingredientes, feijoada.utensilios)

        insert_recipe('Tapioca', '00:10:00', '<li>Heat a non-stick pan and sprinkle tapioca flour evenly to form a pancake.<li>Add desired fillings like cheese, ham, or coconut.<li>Fold in half and serve warm.', tapioca.ingredientes, tapioca.utensilios)

        insert_recipe('Bolo de Cenoura', '00:50:00', '<li>Blend carrots, oil, and eggs until smooth.<li>Mix with sugar, flour, and baking powder, then pour into a greased pan.<li>Bake at 180°C until a toothpick comes out clean.', bolodecenoura.ingredientes, bolodecenoura.utensilios)

        insert_recipe('Escondidinho de Carne', '00:45:00', '<li>Prepare mashed potatoes as a base.<li>Cook ground beef with onions, garlic, and tomato sauce.<li>Layer beef and mashed potatoes in a baking dish, top with cheese, and bake.', escondidinhodecarne.ingredientes, escondidinhodecarne.utensilios)

        insert_recipe('Caldinho de Feijão', '00:30:00', '<li>Cook beans with garlic, onions, and seasoning.<li>Blend until smooth, adding lioth to adjust consistency.<li>Serve hot with croutons or bacon bits as garnish.', caldinhodefeijao.ingredientes, caldinhodefeijao.utensilios)

        insert_recipe('Sopa de Abóbora', '00:40:00', '<li>Peel and cube the pumpkin.<li>Sauté onions and garlic in a pot, then add pumpkin and lioth.<li>Cook until tender, blend until smooth, and season to taste.', sopadeabobora.ingredientes, sopadeabobora.utensilios)

        insert_recipe('Polenta Cremosa', '00:30:00', '<li>liing water or lioth to a boil.<li>Gradually whisk in cornmeal, stirring constantly.<li>Cook until thickened, then mix in butter and cheese.', polentacremosa.ingredientes, polentacremosa.utensilios)

        insert_recipe('Pizza Marguerita', '01:20:00', '<li>Prepare pizza dough and let it rise.<li>Spread tomato sauce over the dough and top with mozzarella and basil.<li>Bake at 220°C until crust is golden and cheese is melted.', pizzamarguerita.ingredientes, pizzamarguerita.utensilios)

        insert_recipe('Arroz Doce', '00:50:00', '<li>Cook rice with water until almost tender.<li>Add milk, sugar, and cinnamon, and simmer until creamy.<li>Serve warm or chilled with cinnamon on top.', arrozdoce.ingredientes, arrozdoce.utensilios)

        insert_recipe('Salada de Quinoa', '00:25:00', '<li>Cook quinoa in boiling water until fluffy.<li>Mix with chopped vegetables, olive oil, lemon juice, and herbs.<li>Chill before serving.', saladadequinoa.ingredientes, saladadequinoa.utensilios)

        insert_recipe('Ceviche', '00:20:00', '<li>Dice fresh fish and marinate in lime juice.<li>Add onions, chili peppers, cilantro, and salt.<li>Chill before serving with tortilla chips or crackers.', ceviche.ingredientes, ceviche.utensilios)

        insert_recipe('Risoto de Cogumelos', '00:45:00', '<li>Sauté mushrooms, garlic, and onions in butter.<li>Add arborio rice, stirring until coated.<li>Slowly add lioth, stirring constantly, until rice is creamy and tender.', risotodecogumelos.ingredientes, risotodecogumelos.utensilios)

        insert_recipe('Hambúrguer Caseiro', '00:30:00', '<li>Mix ground beef with salt, pepper, and optional spices.<li>Shape into patties and cook on a grill or skillet.<li>Assemble with buns, lettuce, cheese, and condiments.', hamburguer.ingredientes, hamburguer.utensilios)

        insert_recipe('Torta de Limão', '01:10:00', '<li>Make a crust with crushed biscuits and butter.<li>Mix condensed milk, lime juice, and cream, then pour into the crust.<li>Chill for 2 hours and serve with whipped cream.', tortadelimao.ingredientes, tortadelimao.utensilios)

        insert_recipe('Churrasco', '01:30:00', '<li>Season meats with coarse salt.<li>Grill over charcoal until desired doneness.<li>Serve with chimichurri and sides like farofa or salad.', churrasco.ingredientes, churrasco.utensilios)

        insert_recipe('Paella', '01:20:00', '<li>Sauté onions, garlic, and bell peppers in olive oil.<li>Add rice, lioth, saffron, and seafood or chicken.<li>Cook until the rice absorbs the liquid.', paella.ingredientes, paella.utensilios)

        insert_recipe('Yakissoba', '00:35:00', '<li>Boil noodles and set aside.<li>Stir-fry vegetables, meat, and soy sauce in a wok.<li>Add noodles, toss, and serve hot.', yakissoba.ingredientes, yakissoba.utensilios)

        insert_recipe('Strogonoff de Frango', '00:30:00', '<li>Sauté chicken with onions and garlic.<li>Add tomato sauce, cream, and mushrooms.<li>Simmer and serve with rice and potato sticks.', strogonoffdefrango.ingredientes, strogonoffdefrango.utensilios)

        insert_recipe('Bolo de Chocolate', '00:50:00', '<li>Mix flour, sugar, cocoa, eggs, and butter.<li>Pour into a greased pan and bake at 180°C.<li>Top with chocolate ganache.', bolodechocolate.ingredientes, bolodechocolate.utensilios)

        insert_recipe('Esfirra Aberta', '01:20:00', '<li>Make a yeast dough and let it rise.<li>Shape into discs, top with ground beef filling.<li>Bake at 200°C until golden.', esfirraaberta.ingredientes, esfirraaberta.utensilios)

        insert_recipe('Doce de Leite', '01:00:00', '<li>Cook milk and sugar over low heat, stirring constantly.<li>Simmer until it thickens and caramelizes.<li>Cool before serving.', docedeleite.ingredientes, docedeleite.utensilios)

        insert_recipe('Bacalhau à brás', '00:50:00', '<li>Soak and shred salted cod.<li>Sauté onions, then mix with cod, eggs, and fried potatoes.<li>Garnish with olives and parsley.', bacalhauabras.ingredientes, bacalhauabras.utensilios)

        insert_recipe('Creme brulée', '01:20:00', '<li>Whisk cream, sugar, and egg yolks, then bake in ramekins in a water bath.<li>Chill and sprinkle sugar on top.<li>Caramelize with a torch before serving.', cremebrulee.ingredientes, cremebrulee.utensilios)

        insert_recipe('Tacos', '00:30:00', '<li>Cook seasoned ground beef or chicken.<li>Fill tortillas with meat, lettuce, cheese, and salsa.<li>Serve with guacamole or sour cream.', tacos.ingredientes, tacos.utensilios)

        insert_recipe('Cachorro-Quente', '00:15:00', '<li>Cook hot dogs in boiling water.<li>Assemble with buns, ketchup, mustard, and optional toppings.<li>Serve immediately.', cachorroquente.ingredientes, cachorroquente.utensilios)

        insert_recipe('Empanadas', '01:00:00', '<li>Make a dough and prepare a meat or vegetable filling.<li>Fill, fold, and seal into half-moon shapes.<li>Bake at 200°C until golden.', empanadas.ingredientes, empanadas.utensilios)

        insert_recipe('Chili con Carne', '00:50:00', '<li>Cook ground beef with onions, garlic, and spices.<li>Add beans, tomatoes, and simmer.<li>Serve with rice or tortilla chips.', chilicomcarne.ingredientes, chilicomcarne.utensilios)

        insert_recipe('Lentilha Refogada', '00:40:00', '<li>Cook lentils until tender.<li>Sauté onions, garlic, and spices, then mix with lentils.<li>Serve as a side or over rice.', lentilharefogada.ingredientes, lentilharefogada.utensilios)

        insert_recipe('Gnocchi', '01:00:00', '<li>Mix mashed potatoes, flour, and egg to form a dough.<li>Shape into rolls, cut into pieces, and boil.<li>Serve with sauce of choice.', gnocchi.ingredientes, gnocchi.utensilios)

        insert_recipe('Bolo de Fubá', '00:50:00', '<li>Mix cornmeal, sugar, milk, eggs, and butter.<li>Pour into a greased pan and bake at 180°C.<li>Serve with coffee or tea.', bolodefuba.ingredientes, bolodefuba.utensilios)

        insert_recipe('Sushi', '01:30:00', '<li>Cook sushi rice and season with vinegar.<li>Slice fresh fish and vegetables.<li>Assemble rolls with nori, rice, and fillings.', sushi.ingredientes, sushi.utensilios)

        insert_recipe('Minestrone', '00:50:00', '<li>Sauté onions, garlic, and vegetables.<li>Add lioth, beans, and pasta, and simmer until tender.<li>Season to taste and serve with grated cheese.', minestrone.ingredientes, minestrone.utensilios)

        insert_recipe('Panna Cotta', '00:20:00', '<li>Heat cream, sugar, and gelatin until dissolved.Pour into molds and chill until set.<li>Serve with fruit sauce.', panacotta.ingredientes, panacotta.utensilios)

        insert_recipe('Crepe', '00:20:00', '<li>Mix flour, milk, eggs, and a pinch of salt to form batter.<li>Cook thin layers in a non-stick pan.<li>Fill with sweet or savory fillings.', crepe.ingredientes, crepe.utensilios)