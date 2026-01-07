# Appllication de gestion de stock #

def sauv_stock():
    with open("stock.txt", "w", encoding="utf-8") as f:    
            for pro, qnt in stocks.items():
                f.write(f"{pro} : {qnt}\n")

def charg_stock():
    try:
        with open ("stock.txt", "r", encoding="utf-8") as f:
            for stock_ligne in f:
                stock_prop = stock_ligne.strip()
                stock = stock_prop.split(":")
                if len(stock) == 2:
                    produit = stock[0].strip()
                    quantite = stock[1].strip()
                    stocks[produit] = int(quantite)
    except FileNotFoundError:
        return 0
        
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
            nom_prod = input("\nEntrez le nom du produit (ou 'retour' pour revenir au menu principal) : ").strip().lower()
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
                        #sauv_stock(nom_prod, quantite)
                        break
            else:
                quantite = int(input("\nEntrez la quantité : "))
                while True:
                    if quantite <= 0:
                        quantite = int(input("\n❌ Erreur : Entrez une valeur positive : "))
                    else:
                        stocks[nom_prod] = quantite
                        print("\n✅ Le produit a ete ajouté ➕!")
                       #sauv_stock(nom_prod, quantite)
                        break
                            
        except ValueError:
            print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
            continue
    
        sauv_stock()

def modifier_prod():
    voir_stock()
    while True:
                prod_modif = input("\nQuel produit souhaitez vous modifier (ou 'retour' pour revenir au menu principal) : ").strip().lower()
                if prod_modif == "retour":
                    return
                if prod_modif not in stocks:
                    print("Erreur : ce produit n'existe pas.")
                    continue
                else:
                    print(f"Modification de '{prod_modif}' (stock actuel : {stocks[prod_modif]}")
                    print("1. Rennomer")
                    print("2. Corriger la quantité")
                    while True:
                        try:
                            choix = int(input("Votre choix : "))
                            if not (1 <= choix <= 2):
                                print("Erreur : choix invalide choisissez (1-2)")
                                continue
                            if choix == 1:
                                nouveau_nom = input("Entrez le nouveau nom : ")
                                if nouveau_nom in stocks:
                                    print(f"❌ Erreur : Le produit '{nouveau_nom}' existe déjà !")
                                    return
                                else:
                                    stocks[nouveau_nom] = stocks.pop(prod_modif)
                                    print("\n✅ Nom changé !")
                                    sauv_stock()
                                    return
                            else:
                                while True:
                                    qunt_modif = int(input("Entrez la nouvelle quantité : "))
                                    if qunt_modif <= 0:
                                        print("❌ Erreur : Entrez une valeur positive : ")
                                        continue
                                    else:
                                        qunt_actu = stocks[prod_modif]
                                        if qunt_modif == qunt_actu:
                                            print("❌ Erreur : la valeur existe déjâ.")
                                            continue
                                        stocks[prod_modif] = qunt_modif
                                        print("\n✅ Quantité corrigé !")
                                        sauv_stock()
                                        return
                        except ValueError:
                            print("❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")

def vendre_produit():
    voir_stock()
    while True:
        prod_vend = input("\nQuel produit souhaitez vous vendre (ou 'retour' pour revenir au menu principal) : ").strip().lower()
        if prod_vend == "retour":
                return
        if prod_vend not in stocks:
            print("\n❌ Erreur : ce produit n'existe pas !")
            continue
        while True:
            try:
                    qunt_vend = int(input("\nCombien voulez vous vendre : "))
                    stock_dispo = stocks[prod_vend]
                    if qunt_vend > stock_dispo:
                        print("\n❌ Erreur : vous avez depassez la quantité disponible en stock !")
                        continue
                    else:
                        stocks[prod_vend] -= qunt_vend
                        if stocks[prod_vend] <= 0:
                            stocks.pop(prod_vend, None)
                            print(f"\n✅ {qunt_vend} {prod_vend} vendu. Stock épuisée.\n")
                        else:
                            print(f"\n✅ {qunt_vend} {prod_vend} vendu. Stock restant : {stocks[prod_vend]}\n")    
                        sauv_stock()
                    return
            except ValueError:
                    print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
                    continue
                
def supprimer_stock():
    voir_stock()
    while True:
            prod_supp = input("\nQuel produit souhaitez vous supprimer (ou 'retour' pour revenir au menu principal) : ").strip().lower()
            if prod_supp == "retour":
                return
            if prod_supp not in stocks:
                print("\n❌ Erreur : ce produit n'existe pas !")
                continue
            else:
                while True:
                    confirmation = input(f"\nÊtes-vous sûr de vouloir supprimer le produit '{prod_supp}' ? (oui/non) : ").strip().lower()
                    if confirmation != "oui" and confirmation != "non":
                        print("\n❌ Erreur : Veuillez répondre par 'oui' ou 'non'.")
                        continue
                    if confirmation == "non":
                        print("\nSuppression annulée.\n")
                        break
                    else:
                        stocks.pop(prod_supp, None)
                        print(f"Le produit {prod_supp} a ete supprimer 🗑️\n")
                        sauv_stock()
                        return
        
stocks = {}

# Programme principale
charg_stock()

while True:
    print("\n\n====== MENU GESTION STOCK ======")
    print("1. Voir le stock")
    print("2. Ajouter du stock")
    print("3. Vendre un produit")
    print("4. Supprimer un produit")
    print("5. Modifier un produit")
    print("6. Quitter")
    print("====================")

    try:
        option = int(input("Veuillez Choisir : "))
        if not (1 <= option <= 6) :
            print("❌ Erreur : Le chiffre doit être entre (1 et 6)")    
    except ValueError:
        print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
        continue

    match option:
        case 1:
            voir_stock()
        case 2:
            ajout_stock()
        case 3:
            vendre_produit()
        case 4:
            supprimer_stock()
        case 5:
            modifier_prod()
        case 6:
            sauv_stock()
            break
