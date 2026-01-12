# Dictionaire pricipale
from datetime import datetime
stocks = {}

# Fonction pour sauvegarder vers le disque dur
def sauv_stock():
    with open("stock.txt", "w", encoding="utf-8") as f: # On ouvre le fichier en mode ecriture    
            for nom, infos in stocks.items(): # On le parcour
                quantite = infos["qte"]
                categorie = infos["cat"]
                prix = infos["prx"]
                f.write(f"{nom} : {int(quantite)} : {categorie} : {prix}\n")

# Fonction pour charger depuis le disque dur
def charg_stock():
    try:
        with open ("stock.txt", "r", encoding="utf-8") as f: # Ouverture enn mode lecture
            for stock_ligne in f: # On le parcours
                stock_prop = stock_ligne.strip()
                stock = stock_prop.split(":")
                if len(stock) == 4:
                    produit = stock[0].strip()
                    quantite = stock[1].strip()
                    categorie = stock[2].strip()
                    prix = stock[3].strip()
                    stocks[produit] = {"qte" : int(quantite), "cat" : categorie, "prx" : int(prix)}
    except FileNotFoundError:
        return 0
        
def historique(message):
    maintenant = datetime.now()
    date = maintenant.strftime("%d/%m/%Y à %H:%M")
    with open("journal.txt", "a", encoding= "utf_8") as f:
        f.write(f"[{date}] : {message}\n")
    return

def voir_historique():
    try:
        with open("journal.txt", "r", encoding= "utf_8") as f:
            lines = f.readlines()
            if not lines :
                print("L'historique est vide")
                return
            else:
                print("\n===== HISTORIQUE DES ACTIVITES =====\n")
                print("_" * 30)
                print(f"{'Date':<10} | {'Action':>10}")
                print("_" * 30)
                for ligne in lines:
                    ligne_propre = ligne.strip()
                    histo = ligne_propre.split("] ")
                    if len(histo) >= 2:
                        date = histo[0] + "]"
                        action = histo[1]
                    print(f"{date:<10} {action:>10}")
    except FileNotFoundError:
        print("(Aucun historique pour l'instant")
    return
