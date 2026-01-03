def voir_stock():
    total_stock = len(stocks)
    if total_stock == 0:
        print(f"Aucun produit disponible pour le moment !")
    else:
        print("\n===== Liste des produits en stock =====\n")
        print("-------------------------------")
        print(f"Produits\t|\tStocks")
        print("-------------------------------")
        for stck, qnte in stocks.items():
            print(f"{stck.capitalize():<15} : {qnte:>5}")
        #print("_________________________________")
    
    return
def ajout_stock():
    while True:
        try:
            nom_prod = input("Entrez le nom du produit (ou 'retour' pour revenir au menu principal) : ").strip().lower()
            if nom_prod == "retour":
                return
            if nom_prod == "":
                print("\n❌ Erreur : Vous devez saisir un nom correct : ")
                continue
            
            if nom_prod in stocks:
                quantite = int(input(f"\nIl y en a deja {stocks[nom_prod]}, combien voulez-vous en ajouter : "))
                while True:
                    if quantite <= 0:
                        quantite = int(input("\n❌ Erreur : Entrez une valeur positive : "))
                    else:
                        stocks[nom_prod] += quantite
                        print("\n✅ Quantité ajouter !")
                        return
            else:
                quantite = int(input("\nEntrez la quantité : "))
                while True:
                    if quantite <= 0:
                        quantite = int(input("\n❌ Erreur : Entrez une valeur positive : "))
                    else:
                        stocks[nom_prod] = quantite
                        print("\n✅ Le produit a ete ajouté ➕!")
                        return
        except ValueError:
            print("\n❌ Erreur : Vous devez entré un  CHIFFRE, pas une lettre.")

def vendre_produit():
    total_stock = len(stocks)
    if total_stock == 0:
        print( "\nAucun produit à vendre pour le moment !\n")
    else:
        prod_vend = input("\nQuel produit souhaitez vous vendre : ").strip().lower()
        if prod_vend not in stocks:
            print("\n❌ Erreur : ce produit n'existe pas !")
            return
        else:
            while True:
                try:
                    qunt_vend = int(input("\nCombien voulez vous vendre : "))
                    stock_dispo = stocks[prod_vend]
                    if qunt_vend > stock_dispo:
                        print("\n❌ Erreur : vous avez depassez la quantité disponible en stock !")
                        continue
                    else:
                        stocks[prod_vend] -= qunt_vend
                        print("\n✅ Produit vendu ")
                        if stocks[prod_vend] == 0:
                            stocks.pop(prod_vend, None)
                    return
                except ValueError:
                    print("\n❌ Erreur : Vous devez entré un  CHIFFRE, pas une lettre.")
                    continue
    
stocks = {}

# Programme principale
while True:
    print("\n\n====== MENU GESTION STOCK ======")
    print("1. Voir le stock")
    print("2. Ajouter du stock")
    print("3. Vendre un produit")
    print("4. Quitter")
    print("====================")

    try:
        option = int(input("Veuillez Choisir : "))
        if not (1 <= option <= 4) :
            print("❌ Erreur : Le chiffre doit être entre (1 et 4)")    
    except ValueError:
        print("\n❌ Erreur : Vous devez entré un  CHIFFRE, pas une lettre.")
        continue

    match option:
        case 1:
            voir_stock()
        case 2:
            ajout_stock()
        case 3:
            vendre_produit()
        case 4:
            print("Au revoir !")
            break
