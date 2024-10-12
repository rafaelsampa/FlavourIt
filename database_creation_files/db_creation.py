import sqlite3

conn = sqlite3.connect('FlavourIt.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE Cliente (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Altura REAL,
    Peso REAL,
    Atividade TEXT
);""")

cursor.execute("""
CREATE TABLE Favoritado (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Id_Receita INT,
    Id_Cliente INT,
    FOREIGN KEY (Id_Receita) REFERENCES Receita(Id),
    FOREIGN KEY (Id_Cliente) REFERENCES Cliente(Id)
);""")

cursor.execute("""
CREATE TABLE Ingrediente (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Id_Receita INT,
    Id_Val_Nutri INT,
    Quantidade REAL,
    Unidade TEXT,
    FOREIGN KEY (Id_Receita) REFERENCES Receita(Id),
    FOREIGN KEY (Id_Val_Nutri) REFERENCES Valores_Nutricionais(Id)
);""")

cursor.execute("""
CREATE TABLE Valores_Nutricionais (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Gordura REAL,
    Carboidrato REAL,
    Proteina REAL,
    Porção REAL,
    Unidade TEXT
);""")

cursor.execute("""
CREATE TABLE Receita_Utensilio (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Id_Receita INT,
    Id_Utensilio INT,
    FOREIGN KEY (Id_Receita) REFERENCES Receita(Id),
    FOREIGN KEY (Id_Utensilio) REFERENCES Utensilio(Id)
);""")

cursor.execute("""
CREATE TABLE Utensilio (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL
);""")

cursor.execute("""
CREATE TABLE Receita (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Tempo TEXT NOT NULL,
    Instruções TEXT NOT NULL
);""")

conn.commit()
conn.close()
