# Dictionaire pricipale
stocks = {}

# Fonction pour sauvegarder vers le disque dur
def sauv_stock():
    with open("stock.txt", "w", encoding="utf-8") as f: # On ouvre le fichier en mode ecriture    
            for nom, infos in stocks.items(): # On le parcour
                quantite = infos["qte"]
                categorie = infos["cat"]
                f.write(f"{nom} : {int(quantite)} : {categorie}\n")

# Fonction pour charger depuis le disque dur
def charg_stock():
    try:
        with open ("stock.txt", "r", encoding="utf-8") as f: # Ouverture enn mode lecture
            for stock_ligne in f: # On le parcours
                stock_prop = stock_ligne.strip()
                stock = stock_prop.split(":")
                if len(stock) == 3:
                    produit = stock[0].strip()
                    quantite = stock[1].strip()
                    categorie = stock[2].strip()
                    stocks[produit] = {"qte" : int(quantite), "cat" : categorie}
    except FileNotFoundError:
        return 0
        