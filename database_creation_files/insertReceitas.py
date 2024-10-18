import sqlite3
import puredebat
import pipoca
import omelete
import macarraoalhoeoleo
import batatasuica
import massadepanqueca
import brigadeiro
import arrozyakubiano

conn = sqlite3.connect('FlavourIt.db')
cursor = conn.cursor()

def get_next_id(table_name, id_column):
    cursor.execute(f"SELECT MAX(CAST({id_column} AS INTEGER)) FROM {table_name}")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        return 1
    return max_id + 1

def get_nutrition_id(nome):
    cursor.execute("SELECT Id FROM Valores_Nutricionais WHERE Nome = ?", (nome,))
    result = cursor.fetchone()
    if result is None:
        return None
    return result[0]

def get_utensilio_id(nome):
    cursor.execute("SELECT Id FROM Utensilio WHERE Nome = ?", (nome,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return None

def insert_nutrition(id_n, nome, gordura, carboidrato, proteina, porcao, unidade):
    cursor.execute("INSERT INTO Valores_Nutricionais (Id, Nome, Gordura, Carboidrato, Proteina, Porção, Unidade) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (id_n, nome, gordura, carboidrato, proteina, porcao, unidade))

def insert_recipe(nome, tempo, instruções, ingredientes, utensilios):

    try:
        receita_id = get_next_id('Receita', 'Id')
        cursor.execute("INSERT INTO Receita (Id, Nome, Tempo, Instruções) VALUES (?, ?, ?, ?)",
                    (receita_id, nome, tempo, instruções))

        for ingrediente in ingredientes:

            nutrition_info = ingrediente['nutrition_info']
            #print("passou aq1"+nutrition_info['nome'])
            if get_nutrition_id(nutrition_info['nome']) is None:
                #print("passou aq2: "+ nutrition_info['nome'])
                id_n=get_next_id('Valores_Nutricionais','Id')
                insert_nutrition(id_n, nutrition_info['nome'], nutrition_info['gordura'], nutrition_info['carboidrato'], nutrition_info['proteina'], nutrition_info['porcao'], nutrition_info['unidade'])
            
            #print("passou aq3")

            nutrition_id = get_nutrition_id(nutrition_info['nome'])

            ingrediente_id = get_next_id('Ingrediente', 'Id')
            cursor.execute("INSERT INTO Ingrediente (Id, Id_Receita, Id_Val_Nutri, Quantidade, Unidade) VALUES (?, ?, ?, ?, ?)",
                        (ingrediente_id, receita_id, nutrition_id, ingrediente['quantidade'], ingrediente['unidade']))
            #print("passou aq4")

        for utensilio in utensilios:

            if get_utensilio_id(utensilio['nome']) is None:
                utensilio_id = get_next_id('Utensilio', 'Id')
                cursor.execute("INSERT INTO Utensilio (Id, Nome) VALUES (?, ?)",
                            (utensilio_id, utensilio['nome']))

            utensilio_id = get_utensilio_id(utensilio['nome'])
            receita_utensilio_id = get_next_id('Receita_Utensilio', 'Id')
            cursor.execute("INSERT INTO Receita_Utensilio (Id, Id_Receita, Id_Utensilio) VALUES (?, ?, ?)",
                        (receita_utensilio_id, receita_id, utensilio_id))
        
        conn.commit()
        print("Receita adicionada.")

    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    
    # finally:
       # conn.close()


insert_recipe('Pipoca', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', pipoca.ingredientes, pipoca.utensilios)
insert_recipe('Pure de Batata', '00:35:00', '1-muchotexto<br>2-muchotexto<br>3-muchotexto,l.lk', puredebat.ingredientes_pure, puredebat.utensilios_pure)
insert_recipe('Omelete', '00:35:00', '1-muchotexto<br>2-muchotexto<br>3-muchotexto,l.lk', omelete.ingredientes, omelete.utensilios)
insert_recipe('Macarrao alho e oleo', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', macarraoalhoeoleo.ingredientes, macarraoalhoeoleo.utensilios)
insert_recipe('Batata suica', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', batatasuica.ingredientes, batatasuica.utensilios)
insert_recipe('Massa de panqueca', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', massadepanqueca.ingredientes, massadepanqueca.utensilios)
insert_recipe('Brigadeiro', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', brigadeiro.ingredientes, brigadeiro.utensilios)
insert_recipe('Arroz yakubiano', '00:05:00', '1-asdfghjklasdfgh<br>2-asdfghnjmk,dfg<br>3-sdfghjkm,l.lk', arrozyakubiano.ingredientes, arrozyakubiano.utensilios)

conn.close()