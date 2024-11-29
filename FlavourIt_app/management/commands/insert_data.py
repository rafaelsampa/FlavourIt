from django.core.management.base import BaseCommand
from FlavourIt_app.utils import insert_recipe
from FlavourIt_app.receitas import (
    bananapancake,
    barbecue,
    beanbroth,
    brigadeiro,
    carrotcake,
    cheesequiche,
    chiliconcarne,
    chickenstroganoff,
    chocolatecake,
    cookiewithmint,
    cornmealcake,
    coxinha,
    cremebrulee,
    crepe,
    ceviche,
    empanadas,
    feijoada,
    fishmoqueca,
    glutinousrice,
    gnocchi,
    grilledcod,
    hamburger,
    hotdog,
    lasagna,
    lemonpie,
    margheritapizza,
    mashedpotatoes,
    meatescondidinho,
    milkcream,
    minestronesoup,
    mushroomrisotto,
    omelet,
    openesfiha,
    paella,
    pannacotta,
    pancake,
    pastawithgarlicandoil,
    popcorn,
    pumpkinsoup,
    quinoasalad,
    ratatouille,
    roastedchicken,
    sauteedlentils,
    swisspotato,
    sushi,
    tacos,
    tapioca,
    whiterice,
    yakissoba,
    creamypolenta,
)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        insert_recipe('Ratatouille', '01:00:00', '<li>Preheat oven to 190°C (375°F).<li>Thinly slice zucchini, eggplant, tomatoes, and bell peppers.<li>Prepare a sauce by sautéing onions and garlic in olive oil, then adding crushed tomatoes, salt, pepper, and herbs like thyme and basil.<li>Spread the sauce on the bottom of a baking dish.<li>Arrange the sliced vegetables in overlapping rows over the sauce, alternating colors.<li>Drizzle with olive oil, sprinkle with herbs, and cover with foil.<li>Bake for 40 minutes, then remove the foil and bake for an additional 10 minutes until vegetables are tender and slightly caramelized.', ratatouille.ingredientes, ratatouille.utensilios)

        insert_recipe('White Rice', '00:20:00', '<li>Rinse the rice thoroughly until the water runs clear.In a pot, heat oil and sauté garlic until fragrant.<li>Add rice, stir liiefly, then add boiling water and salt. Cover and cook on low heat until the water is absorbed.', whiterice.ingredientes, whiterice.utensilios)

        insert_recipe('Swiss Potato', '00:25:00', '<li>Grate raw potatoes, squeeze out excess liquid, and season with salt and pepper.<li>Heat butter in a non-stick skillet, add a layer of potatoes, and cook until golden.<li>Flip carefully, cook the other side, and serve hot.', swisspotato.ingredientes, swisspotato.utensilios)

        insert_recipe('Oatmeal Cookie with Mint', '00:15:00', '<li>Mix oats, flour, chopped mint, and sugar in a bowl.<li>Add melted butter and milk, stirring until combined.<li>Shape into cookies and bake at 180°C until golden.', cookiewithmint.ingredientes, cookiewithmint.utensilios)

        insert_recipe('Brigadeiro', '00:15:00', '<li>Mix condensed milk, cocoa powder, and butter in a saucepan.<li>Cook over medium heat, stirring constantly, until the mixture thickens and pulls away from the sides of the pan.<li>Allow to cool, then shape into balls and roll in chocolate sprinkles.', brigadeiro.ingredientes, brigadeiro.utensilios)

        insert_recipe('Pasta with garlic and oil', '00:15:00', '<li>Cook spaghetti in boiling salted water until al dente.<li>In a skillet, sauté garlic in olive oil until golden.<li>Toss the drained spaghetti in the skillet with garlic and oil. Season with salt, pepper, and parsley.', pastawithgarlicandoil.ingredientes, pastawithgarlicandoil.utensilios)

        insert_recipe('Pancake ', '00:10:00', '<li>Mix flour, milk, eggs, and a pinch of salt until smooth.<li>Heat a non-stick skillet and pour a small amount of batter, swirling to coat the bottom.<li>Cook until edges lift, flip, and cook liiefly on the other side.', pancake.ingredientes, pancake.utensilios)

        insert_recipe('Omelet', '00:10:00', '<li>Beat eggs with a pinch of salt, pepper, and optional fillings like cheese or vegetables.<li>Heat butter in a skillet, pour in the eggs, and let set.<li>Fold the omelet in half and cook liiefly until the cheese melts.', omelet.ingredientes, omelet.utensilios)

        insert_recipe('Banana Pancake', '00:10:00', '<li>Mash bananas and mix with eggs, flour, and a pinch of cinnamon.<li>Heat a non-stick skillet and pour small portions of batter.<li>Cook until bubbles form, flip, and cook the other side.', bananapancake.ingredientes, bananapancake.utensilios)

        insert_recipe('Popcorn', '00:05:00', '<li>Heat oil in a large pot and add popcorn kernels.<li>Cover the pot, leaving a small vent, and shake occasionally.<li>Once popping slows, remove from heat, season, and serve.', popcorn.ingredientes, popcorn.utensilios)

        insert_recipe('Smashed potatoes', '00:35:00', '<li>Boil peeled and cubed potatoes in salted water until tender.<li>Mash the potatoes with butter, warm milk, salt, and pepper until smooth.<li>Serve hot as a side dish.', mashedpotatoes.ingredientes_pure, mashedpotatoes.utensilios_pure)

        insert_recipe('Roasted Chicken', '01:20:00', '<li>Preheat oven to 200°C (400°F).<li>Season the chicken with salt, pepper, garlic, and herbs.<li>Place in a baking dish and roast until golden liown and juices run clear.', roastedchicken.ingredientes, roastedchicken.utensilios)

        insert_recipe('Lasagna', '01:30:00', '<li>Cook lasagna noodles until al dente.<li>Prepare the meat sauce by sautéing garlic, onions, and ground beef, then adding tomato sauce.<li>Layer noodles, sauce, and cheese in a baking dish. Bake at 180°C until bubbly.', lasagna.ingredientes, lasagna.utensilios)

        insert_recipe('Cheese Quiche', '00:50:00', '<li>Mix flour and butter to form a dough, then press into a pie dish.<li>Whisk eggs, cream, cheese, and seasoning, then pour into the crust.<li>Bake at 180°C until set and golden.', cheesequiche.ingredientes, cheesequiche.utensilios)

        insert_recipe('Coxinha', '01:10:00', '<li>Boil chicken with seasoning, then shred.<li>Make dough with flour and lioth, then wrap around the chicken filling.<li>liead and deep-fry until golden liown.', coxinha.ingredientes, coxinha.utensilios)

        insert_recipe('Fish Moqueca', '00:40:00', '<li>Marinate fish in lime juice, garlic, and salt.<li>Layer fish, peppers, onions, and tomatoes in a pot.<li>Cook with coconut milk until the fish is tender and the flavors meld.', fishmoqueca.ingredientes, fishmoqueca.utensilios)

        insert_recipe('Feijoada', '02:00:00', '<li>Soak black beans overnight and cook until tender.<li>Sauté garlic, onions, and pork cuts, then add to the beans.<li>Simmer with spices and serve with rice, orange slices, and greens.', feijoada.ingredientes, feijoada.utensilios)

        insert_recipe('Tapioca', '00:10:00', '<li>Heat a non-stick pan and sprinkle tapioca flour evenly to form a pancake.<li>Add desired fillings like cheese, ham, or coconut.<li>Fold in half and serve warm.', tapioca.ingredientes, tapioca.utensilios)

        insert_recipe('Carrot Cake', '00:50:00', '<li>Blend carrots, oil, and eggs until smooth.<li>Mix with sugar, flour, and baking powder, then pour into a greased pan.<li>Bake at 180°C until a toothpick comes out clean.', carrotcake.ingredientes, carrotcake.utensilios)

        insert_recipe('Meat Escondidinho', '00:45:00', '<li>Prepare mashed potatoes as a base.<li>Cook ground beef with onions, garlic, and tomato sauce.<li>Layer beef and mashed potatoes in a baking dish, top with cheese, and bake.', meatescondidinho.ingredientes, meatescondidinho.utensilios)

        insert_recipe('Bean Broth', '00:30:00', '<li>Cook beans with garlic, onions, and seasoning.<li>Blend until smooth, adding lioth to adjust consistency.<li>Serve hot with croutons or bacon bits as garnish.', beanbroth.ingredientes, beanbroth.utensilios)

        insert_recipe('Pumpking Soup', '00:40:00', '<li>Peel and cube the pumpkin.<li>Sauté onions and garlic in a pot, then add pumpkin and lioth.<li>Cook until tender, blend until smooth, and season to taste.', pumpkinsoup.ingredientes, pumpkinsoup.utensilios)

        insert_recipe('Creamy Polenta', '00:30:00', '<li>liing water or lioth to a boil.<li>Gradually whisk in cornmeal, stirring constantly.<li>Cook until thickened, then mix in butter and cheese.', creamypolenta.ingredientes, creamypolenta.utensilios)

        insert_recipe('Marguerita Cheese Pizza', '01:20:00', '<li>Prepare pizza dough and let it rise.<li>Spread tomato sauce over the dough and top with mozzarella and basil.<li>Bake at 220°C until crust is golden and cheese is melted.', margheritapizza.ingredientes, margheritapizza.utensilios)

        insert_recipe('Glutinous Rice', '00:50:00', '<li>Cook rice with water until almost tender.<li>Add milk, sugar, and cinnamon, and simmer until creamy.<li>Serve warm or chilled with cinnamon on top.', glutinousrice.ingredientes, glutinousrice.utensilios)

        insert_recipe('Quinoa Salad', '00:25:00', '<li>Cook quinoa in boiling water until fluffy.<li>Mix with chopped vegetables, olive oil, lemon juice, and herbs.<li>Chill before serving.', quinoasalad.ingredientes, quinoasalad.utensilios)

        insert_recipe('Ceviche', '00:20:00', '<li>Dice fresh fish and marinate in lime juice.<li>Add onions, chili peppers, cilantro, and salt.<li>Chill before serving with tortilla chips or crackers.', ceviche.ingredientes, ceviche.utensilios)

        insert_recipe('Mushroom Risotto', '00:45:00', '<li>Sauté mushrooms, garlic, and onions in butter.<li>Add arborio rice, stirring until coated.<li>Slowly add lioth, stirring constantly, until rice is creamy and tender.', mushroomrisotto.ingredientes, mushroomrisotto.utensilios)

        insert_recipe('Hamburger', '00:30:00', '<li>Mix ground beef with salt, pepper, and optional spices.<li>Shape into patties and cook on a grill or skillet.<li>Assemble with buns, lettuce, cheese, and condiments.', hamburger.ingredientes, hamburger.utensilios)

        insert_recipe('Lemon Pie', '01:10:00', '<li>Make a crust with crushed biscuits and butter.<li>Mix condensed milk, lime juice, and cream, then pour into the crust.<li>Chill for 2 hours and serve with whipped cream.', lemonpie.ingredientes, lemonpie.utensilios)

        insert_recipe('Churrasco', '01:30:00', '<li>Season meats with coarse salt.<li>Grill over charcoal until desired doneness.<li>Serve with chimichurri and sides like farofa or salad.', barbecue.ingredientes, barbecue.utensilios)

        insert_recipe('Paella', '01:20:00', '<li>Sauté onions, garlic, and bell peppers in olive oil.<li>Add rice, lioth, saffron, and seafood or chicken.<li>Cook until the rice absorbs the liquid.', paella.ingredientes, paella.utensilios)

        insert_recipe('Yakissoba', '00:35:00', '<li>Boil noodles and set aside.<li>Stir-fry vegetables, meat, and soy sauce in a wok.<li>Add noodles, toss, and serve hot.', yakissoba.ingredientes, yakissoba.utensilios)

        insert_recipe('Chicken Strogonoff', '00:30:00', '<li>Sauté chicken with onions and garlic.<li>Add tomato sauce, cream, and mushrooms.<li>Simmer and serve with rice and potato sticks.', chickenstroganoff.ingredientes, chickenstroganoff.utensilios)

        insert_recipe('Chocolate Cake', '00:50:00', '<li>Mix flour, sugar, cocoa, eggs, and butter.<li>Pour into a greased pan and bake at 180°C.<li>Top with chocolate ganache.', chocolatecake.ingredientes, chocolatecake.utensilios)

        insert_recipe('Open Esfiha', '01:20:00', '<li>Make a yeast dough and let it rise.<li>Shape into discs, top with ground beef filling.<li>Bake at 200°C until golden.', openesfiha.ingredientes, openesfiha.utensilios)

        insert_recipe('Milk Cream', '01:00:00', '<li>Cook milk and sugar over low heat, stirring constantly.<li>Simmer until it thickens and caramelizes.<li>Cool before serving.', milkcream.ingredientes, milkcream.utensilios)

        insert_recipe('Grilled Cod', '00:50:00', '<li>Soak and shred salted cod.<li>Sauté onions, then mix with cod, eggs, and fried potatoes.<li>Garnish with olives and parsley.', grilledcod.ingredientes, grilledcod.utensilios)

        insert_recipe('Crème Brûlée', '01:20:00', '<li>Whisk cream, sugar, and egg yolks, then bake in ramekins in a water bath.<li>Chill and sprinkle sugar on top.<li>Caramelize with a torch before serving.', cremebrulee.ingredientes, cremebrulee.utensilios)

        insert_recipe('Tacos', '00:30:00', '<li>Cook seasoned ground beef or chicken.<li>Fill tortillas with meat, lettuce, cheese, and salsa.<li>Serve with guacamole or sour cream.', tacos.ingredientes, tacos.utensilios)

        insert_recipe('Hot Dog', '00:15:00', '<li>Cook hot dogs in boiling water.<li>Assemble with buns, ketchup, mustard, and optional toppings.<li>Serve immediately.', hotdog.ingredientes, hotdog.utensilios)

        insert_recipe('Empanadas', '01:00:00', '<li>Make a dough and prepare a meat or vegetable filling.<li>Fill, fold, and seal into half-moon shapes.<li>Bake at 200°C until golden.', empanadas.ingredientes, empanadas.utensilios)

        insert_recipe('Chili con Carne', '00:50:00', '<li>Cook ground beef with onions, garlic, and spices.<li>Add beans, tomatoes, and simmer.<li>Serve with rice or tortilla chips.', chiliconcarne.ingredientes, chiliconcarne.utensilios)

        insert_recipe('Sautéed Lentils', '00:40:00', '<li>Cook lentils until tender.<li>Sauté onions, garlic, and spices, then mix with lentils.<li>Serve as a side or over rice.', sauteedlentils.ingredientes, sauteedlentils.utensilios)

        insert_recipe('Gnocchi', '01:00:00', '<li>Mix mashed potatoes, flour, and egg to form a dough.<li>Shape into rolls, cut into pieces, and boil.<li>Serve with sauce of choice.', gnocchi.ingredientes, gnocchi.utensilios)

        insert_recipe('Cornmeal Cake ', '00:50:00', '<li>Mix cornmeal, sugar, milk, eggs, and butter.<li>Pour into a greased pan and bake at 180°C.<li>Serve with coffee or tea.', cornmealcake.ingredientes, cornmealcake.utensilios)

        insert_recipe('Sushi', '01:30:00', '<li>Cook sushi rice and season with vinegar.<li>Slice fresh fish and vegetables.<li>Assemble rolls with nori, rice, and fillings.', sushi.ingredientes, sushi.utensilios)

        insert_recipe('minestronesoup Soup', '00:50:00', '<li>Sauté onions, garlic, and vegetables.<li>Add lioth, beans, and pasta, and simmer until tender.<li>Season to taste and serve with grated cheese.', minestronesoup.ingredientes, minestronesoup.utensilios)

        insert_recipe('Panna Cotta', '00:20:00', '<li>Heat cream, sugar, and gelatin until dissolved.Pour into molds and chill until set.<li>Serve with fruit sauce.', pannacotta.ingredientes, pannacotta.utensilios)

        insert_recipe('Crepe', '00:20:00', '<li>Mix flour, milk, eggs, and a pinch of salt to form batter.<li>Cook thin layers in a non-stick pan.<li>Fill with sweet or savory fillings.', crepe.ingredientes, crepe.utensilios)