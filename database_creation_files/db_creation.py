import sqlite3

conn = sqlite3.connect('FlavourIt.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Cliente (
    Id TEXT PRIMARY KEY,
    Nome TEXT NOT NULL,
    Altura REAL,
    Peso REAL,
    Atividade TEXT
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Valores_Nutricionais (
    Id text primary key,
    Nome TEXT,
    Gordura REAL,
    Carboidrato REAL,
    Proteina REAL,
    Porção REAL,
    Unidade TEXT
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Favoritado (
    Id_Receita TEXT,
    Id_val_nutri INT,
    FOREIGN KEY(Id_Receita) REFERENCES Receita(Id),
    FOREIGN KEY(Id_Val_Nutri) REFERENCES Valores_Nutricionais(Id)
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Ingrediente (
    Id TEXT PRIMARY KEY,
    Id_Receita TEXT,
    Id_Val_Nutri INT,
    Quantidade REAL,
    Unidade TEXT,
    FOREIGN KEY(Id_Receita) REFERENCES Receita(Id),
    FOREIGN KEY(Id_Val_Nutri) REFERENCES Valores_Nutricionais(Id)
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Receita_Utensilio (
    Id TEXT PRIMARY KEY,
    Id_Receita TEXT,
    Id_Utensilio TEXT,
    FOREIGN KEY (Id_Receita) REFERENCES Receita(Id),
    FOREIGN KEY (Id_Utensilio) REFERENCES Utensilio(Id)
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Utensilio (
    Id TEXT PRIMARY KEY,
    Nome TEXT NOT NULL
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Receita (
    Id TEXT PRIMARY KEY,
    Nome TEXT NOT NULL,
    Tempo TEXT NOT NULL,
    Instruções TEXT NOT NULL
)''')
conn.commit()
conn.close()
