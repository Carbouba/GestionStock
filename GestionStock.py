def voir_stock():
    total_stock = len(stocks)
    if total_stock == 0:
        print(f"Aucun produit disponible pour le moment !")
    else:
        print("\n===== Liste des produits en stock =====")
        for stck, qnte in stocks.items():
            print(f"{stck.capitalize():5} : {qnte:>5}")
        print("====================\n")
    
    return
def ajout_stock():
    while True:
        try:
            nom_prod = input("Entrez le nom du produit : ").strip().lower()
            if nom_prod == "":
                print("❌ Erreur : Vous devez saisir un nom correct : ")
                continue
            
            if nom_prod in stocks:
                quantite = int(input("❌ Erreur : le produit existe deja, combien voulez-vous en ajouter ❓: "))
                while True:
                    if 0 <= quantite:
                        print("❌ Erreur : Entrez une valeur positive")
                    else:
                        stocks[nom_prod] += quantite
                        print("✅ Quantité ajouter !")
                        return
            else:
                quantite = int(input("Entrez la quantité : "))
                stocks[nom_prod.lower()] = quantite
                print("✅ Le produit a ete ajouté ➕!")
                return
        except ValueError:
            print("\n❌ Erreur : Vous devez entré un  CHIFFRE, pas une lettre.")


    
def vendre_produit():
    prod_vent = input("Entrez le nom du produit a vendre : ").strip()
    return

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
        if 1 > option and 4 < option :
            break
        else:
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
