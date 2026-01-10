# Appllication de gestion de stock #

def sauv_stock():
    with open("stock.txt", "w", encoding="utf-8") as f:    
            for nom, infos in stocks.items():
                quantite = infos["qte"]
                categorie = infos["cat"]
                f.write(f"{nom} : {int(quantite)} : {categorie}\n")

def charg_stock():
    try:
        with open ("stock.txt", "r", encoding="utf-8") as f:
            for stock_ligne in f:
                stock_prop = stock_ligne.strip()
                stock = stock_prop.split(":")
                if len(stock) == 3:
                    produit = stock[0].strip()
                    quantite = stock[1].strip()
                    categorie = stock[2].strip()
                    stocks[produit] = {"qte" : int(quantite), "cat" : categorie}
    except FileNotFoundError:
        return 0
        
def voir_stock():
    total_stock = len(stocks)
    if total_stock == 0:
        print(f"Aucun produit disponible pour le moment !")
    else:
        print("\n===== Liste des produits en stock =====\n")
        print("-------------------------------")
        print(f"{'Produits':<10} | {'Stock':>5} | {'Catégorie':>10}")
        print("-------------------------------")
        for nom, infos in stocks.items():
            quantite = infos["qte"]
            categorie = infos["cat"]
            print(f"{nom.capitalize():<10} : {quantite:>5}{categorie.capitalize():>10}")
        #print("_________________________________")
    return

def recherche_stock():
    total_stock = len(stocks)
    if total_stock == 0:
        print(f"Aucun produit disponible pour le moment !")
    else:
        print("\n===== Rechercher de produit =====\n")
        while True:
            prod_recherche = input("Entrez le nom du produit a rehchercher (ou 'retour' pour revenir au menu principal) : ").strip().lower()
            if prod_recherche == "retour":
                return
            if prod_recherche == "":
                print("\n❌ Erreur : Vous devez saisir un nom correct : ")
                continue
            if prod_recherche not in stocks:
                print("Erreur : ce produit n'existe pas.")
                continue
            print("Resultat de la recherche : ")
            for nom, infos in stocks.items():
                quantite = infos["qte"]
                categorie = infos["cat"]
                print(f"{nom.capitalize():<10} : {quantite:>5} {categorie.capitalize():>10}")
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
                quantite = int(input(f"\nIl y en a deja {stocks[nom_prod]["qte"]}, combien voulez-vous en ajouter : "))
                while True:
                    if quantite <= 0:
                        quantite = int(input("\n❌ Erreur : Entrez une valeur positive : "))
                    else:
                        #categorie = input("Entrez la catégorie du produit : ")
                        stocks[nom_prod]["qte"] += quantite
                        print("\n✅ Quantité ajouter !")
                        #sauv_stock(nom_prod, quantite)
                        break
            else:
                quantite = int(input("\nEntrez la quantité : "))
                while True:
                    if quantite <= 0:
                        quantite = int(input("\n❌ Erreur : Entrez une valeur positive : "))
                    else:
                        categorie = input("Entrez la catégorie du produit : ")
                        stocks[nom_prod] = {"qte" : int(quantite), "cat" : categorie}
                        print(f"{nom_prod} : {quantite}")
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
                    print(f"Modification de '{prod_modif}' (stock actuel : {stocks[prod_modif]["qte"]}")
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
                                    nouveau_quant = int(input("Entrez la nouvelle quantité : "))
                                    if nouveau_quant <= 0:
                                        print("❌ Erreur : Entrez une valeur positive : ")
                                        continue
                                    else:
                                        qunt_actu = stocks[prod_modif]["qte"]
                                        if nouveau_quant == qunt_actu:
                                            print("❌ Erreur : la valeur existe déjâ.")
                                            continue
                                        stocks[prod_modif]["qte"] = nouveau_quant
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
                    if qunt_vend <= 0:
                        print("❌ Erreur : Entrez une valeur positive : ")
                        continue
                    stock_dispo = stocks[prod_vend]["qte"]
                    if qunt_vend > stock_dispo:
                        print("\n❌ Erreur : vous avez depassez la quantité disponible en stock !")
                        continue
                    else:
                        stocks[prod_vend]["qte"] -= qunt_vend
                        if stocks[prod_vend]["qte"] <= 0:
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
    print("2. Rechercher un produit")
    print("3. Ajouter du stock")
    print("4. Vendre un produit")
    print("5. Supprimer un produit")
    print("6. Modifier un produit")
    print("7. Quitter")
    print("====================")

    try:
        option = int(input("Veuillez Choisir : "))
        if not (1 <= option <= 7) :
            print("❌ Erreur : Le chiffre doit être entre (1 et 6)") 
            continue   
    except ValueError:
        print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
        continue

    match option:
        case 1:
            voir_stock()
        case 2:
            recherche_stock()
        case 3:
            ajout_stock()
        case 4:
            vendre_produit()
        case 5:
            supprimer_stock()
        case 6:
            modifier_prod()
        case 7:
            sauv_stock()
            break
