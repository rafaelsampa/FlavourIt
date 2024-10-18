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


palavra=input("**digite para filtrar por palavra**: ") #pegar input do usuario
filtrarPorNome(palavra)

conn.close()