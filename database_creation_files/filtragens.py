import sqlite3

conn = sqlite3.connect('FlavourIt.db')
cursor = conn.cursor()

def filtrarPorNome(palavra):
    cursor.execute("SELECT Nome FROM Receita WHERE Nome LIKE ?", ('%'+palavra+'%',))
    results = cursor.fetchall()
    
    if results: #aparecer as receitas
        for row in results:
            print(row)
    else: #mostrar q nao apareceu nada
        print("Nao foram encontradas receitas com essa palavra :(")

def filtrarPorIngrediente(ingredientes):

    query = """
    SELECT DISTINCT r.Nome FROM Receita r
    JOIN Ingrediente ri ON r.Id = ri.id_Receita
    JOIN Valores_Nutricionais i ON ri.Id_val_nutri = i.Id
    WHERE i.Nome IN ({})
    """.format(','.join('?' * len(ingredientes)))  # Dynamically create placeholders

    # Execute the query with the ingredient list and its length (for the HAVING clause)
    params = ingredientes
    cursor.execute(query, params)
    
    itens = cursor.fetchall()
    
    if len(itens) != 0:
        for i in itens:
            print(i)
    else:
        print('\033[1mNão foi encontrado o ingrediente dito\033[0m')

def filtrarPorUtensilios(utensilios):
    query = """
    SELECT DISTINCT r.Nome FROM Receita r
    JOIN Receita_Utensilio ri ON r.Id = ri.id_Receita
    JOIN Utensilio i ON ri.Id_Utensilio = i.Id
    WHERE i.Nome IN ({})
    """.format(','.join('?' * len(utensilios)))  # Dynamically create placeholders

    # Execute the query with the ingredient list and its length (for the HAVING clause)
    params = utensilios
    cursor.execute(query, params)
    
    itens = cursor.fetchall()
    
    if len(itens) != 0:
        for i in itens:
            print(i)
    else:
        print('\033[1mNão foi encontrado o utensilio dito\033[0m')

def filtrarNomeEIngrediente(nome, ingredientes):

    query1="SELECT DISTINCT r.Nome FROM Receita r JOIN ingrediente ri ON r.Id = ri.id_Receita JOIN Valores_Nutricionais i ON ri.Id_val_nutri = i.Id WHERE r.Nome LIKE ?"
    #, ('%'+nome+'%',)
    placeholders = ','.join('?' * len(ingredientes))
    query2 = f" AND i.Nome IN ({placeholders})"
    query=query1+query2

    # Execute the query with both the recipe name (using LIKE) and the ingredient
    params = ['%' + nome + '%']+ingredientes
    cursor.execute(query, params)

    # Fetch and display results
    itens = cursor.fetchall()

    if len(itens) != 0:
        for row in itens:
            print(row)  # Print recipe names
    else:
        print("nao foi encontrada nenhuma receita :(")


def filtrarNomeEUtensilio(nome, utensilios):

    query1="SELECT DISTINCT r.Nome FROM Receita r JOIN Receita_Utensilio ri ON r.Id = ri.id_Receita JOIN utensilio i ON ri.Id_Utensilio = i.Id WHERE r.Nome LIKE ?"
    #, ('%'+nome+'%',)
    placeholders = ','.join('?' * len(utensilios))
    query2 = f" AND i.Nome IN ({placeholders})"
    query=query1+query2

    # Execute the query with both the recipe name (using LIKE) and the ingredient
    params = ['%' + nome + '%']+utensilios
    cursor.execute(query, params)

    # Fetch and display results
    itens = cursor.fetchall()

    if len(itens) != 0:
        for row in itens:
            print(row)  # Print recipe names
    else:
        print("nao foi encontrada nenhuma receita :(")


def filtrarIngredienteEUtensilio(ingredientes, utensilios):

    ingredientes_placeholders = ','.join('?' * len(ingredientes))
    utensilios_placeholders = ','.join('?' * len(utensilios))
    # Build the query
    query = f"""
    SELECT DISTINCT r.Nome
    FROM Receita r
    JOIN ingrediente ri ON r.Id = ri.id_Receita
    JOIN Valores_Nutricionais i ON ri.Id_val_nutri = i.Id
    JOIN Receita_Utensilio u ON r.Id = u.id_Receita
    JOIN Utensilio ON u.Id_Utensilio = utensilio.Id
    WHERE i.Nome IN ({ingredientes_placeholders}) OR utensilio.Nome IN ({utensilios_placeholders})
    """

    # Create parameters list
    params = ingredientes + utensilios  # Combine ingredient and utensil lists

    cursor.execute(query,params)

    itens = cursor.fetchall()

    if len(itens) != 0:
        for row in itens:
            print(row)  # Print recipe names
    else:
        print("nao foi encontrada nenhuma receita :(")


def filtrarNomeEIngredienteEUtensilio(nome, ingredientes, utensilios):

    ingredientes_placeholders = ','.join('?' * len(ingredientes))
    utensilios_placeholders = ','.join('?' * len(utensilios))
    # Build the query
    query = f"""
    SELECT DISTINCT r.Nome
    FROM Receita r
    JOIN ingrediente ri ON r.Id = ri.id_Receita
    JOIN Valores_Nutricionais i ON ri.Id_val_nutri = i.Id
    JOIN Receita_Utensilio u ON r.Id = u.id_Receita
    JOIN Utensilio ON u.Id_Utensilio = utensilio.Id
    WHERE r.nome like ? and (i.Nome IN ({ingredientes_placeholders}) OR utensilio.Nome IN ({utensilios_placeholders}))
    """

    # Create parameters list
    params = ['%'+nome+'%']+ingredientes + utensilios  # Combine ingredient and utensil lists

    cursor.execute(query,params)

    itens = cursor.fetchall()

    if len(itens) != 0:
        for row in itens:
            print(row)  # Print recipe names
    else:
        print("nao foi encontrada nenhuma receita :(")


#palavra=input("**digite para filtrar por palavra**: ") #pegar input do usuario
#filtrarPorNome(palavra)
#nome=input("Enter nome da receita: ")
#ingredientes=input("Enter ingredientes separated by commas: ").split(",")
#utensilios=input("Enter utensilios separated by commas: ").split(",")
#filtrarNomeEIngredienteEUtensilio(nome, ingredientes, utensilios)

conn.close()
