import sqlite3

# Création de la base de donnée
db = sqlite3.connect("Stock.db")

# Création d'un curseur pour executer des requetes
cur  = db.cursor()

# Créer une requéte pour générer une table (USERS)
cur.execute("""
CREAT TABLE IN NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_name TEXT NOT NULL,
email TEXT NUNIQUE NOT NULL,
mdp TEXT NOT NULL,
date_creation  TEXT DEFAULT (datetime("now, "localtime"))
)
""")

# Inseré un utilisateur
cur.execute("INSERT INTO users (user_name, email, mdp ) VALUES (?, ?, ?)", ("Carbouba", "bso@gmail.com"))

db.commit()
db.close()
