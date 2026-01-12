# Importation de données des differents fichiers
import data

# Fonction pour afficher la liste des articles
def voir_stock():
    total_stock = len(data.stocks)
    if total_stock == 0:
        print(f"Aucun article disponible pour le moment !")
    else:
        print("\n===== Liste des articles en stock =====\n")
        print("-" * 50)
        print(f"{'Article':<10} | {'Stock':>5} | {'Catégorie':>10} | {'Prix unitaire':>10}")
        print("-" * 50)
        for nom, infos in data.stocks.items(): # On parcour le dictionaire tout entier
            quantite = infos["qte"]
            categorie = infos["cat"]
            prix_unitaire = infos["prx"]
            print(f"{nom.capitalize():<13} {quantite:>3} {categorie.capitalize():>13} {prix_unitaire:>10}")
        #print("_________________________________")
    return

# Fonction pour rechercher un article
def recherche_stock():
    total_stock = len(data.stocks)
    if total_stock == 0:
        print(f"Aucun article disponible pour le moment !")
    else:
        print("\n===== Rechercher un article =====\n")
        while True:
            prod_recherche = input("Entrez le nom de l'article a rehchercher (ou 'retour' pour revenir au menu principal) : ").strip().lower()
            if prod_recherche == "retour":
                return
            if prod_recherche == "": # Si l'utilisateur ne tape rien et valide
                print("\n❌ Erreur : Vous devez saisir un nom correct : ")
                continue
            if prod_recherche not in data.stocks:
                print("Erreur : cet article n'existe pas.")
                continue
            else:
                print("\nResultat de la recherche : ")
                quantite = data.stocks[prod_recherche]["qte"]
                categorie = data.stocks[prod_recherche]["cat"]
                Prix_unitaire = data.stocks[prod_recherche]["prx"]
                print("-" * 50)
                print(f"{prod_recherche:<10} {quantite:>5} {categorie:>10} {Prix_unitaire:>10}")
                print("-" * 50)
            #print("_________________________________")
    return

def ajout_stock():
    while True:
        try:
            nom_prod = input("\nEntrez le nom de l'article (ou 'retour' pour revenir au menu principal) : ").strip().lower()
            if nom_prod == "retour":
                return
            if nom_prod == "":
                print("\n❌ Erreur : Vous devez saisir un nom correct : ")
                continue
            
            if nom_prod in data.stocks:
                quantite = int(input(f"\nIl y en a deja {data.stocks[nom_prod]["qte"]}, combien voulez-vous en ajouter : "))
                while True:
                    if quantite <= 0:
                        quantite = int(input("\n❌ Erreur : Entrez une valeur positive : "))
                    else:
                        #categorie = input("Entrez la catégorie du produit : ")
                        data.stocks[nom_prod]["qte"] += quantite
                        print("\n✅ Quantité ajouté !")
                        #sauv_stock(nom_prod, quantite)
                        break
            else:
                while True:
                    quantite = int(input("\nEntrez la quantité : "))
                    if quantite <= 0 :
                        print("\n❌ Erreur : Entrez une valeur positive")
                        continue
                    while True:
                        prix_unitaire = int(input("Entrez le prix unitaire : "))
                        if  prix_unitaire <= 0:
                            print("\n❌ Erreur : Entrez une valeur positive")
                            continue
                        categorie = input("Entrez la catégorie de l'article : ")
                        data.stocks[nom_prod] = {"qte" : int(quantite), "cat" : categorie, "prx" : int(prix_unitaire)}
                        print("\n✅ Article ajouté ➕!")
                        break
                    break              
        except ValueError:
            print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
            continue
    
        data.historique(f"Ajout de {quantite} {nom_prod}")
        data.sauv_stock()
        

def modifier_prod():
    voir_stock()
    while True:
                prod_modif = input("\nQuel article souhaitez vous modifier (ou 'retour' pour revenir au menu principal) : ").strip().lower()
                if prod_modif == "retour":
                    return
                if prod_modif not in data.stocks:
                    print("Erreur : cet article n'existe pas.")
                    continue
                else:
                    print(f"Modification de '{prod_modif}' (stock actuel : {data.stocks[prod_modif]["qte"]}")
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
                                if nouveau_nom in data.stocks:
                                    print(f"❌ Erreur : L'article '{nouveau_nom}' existe déjà !")
                                    return
                                else:
                                    data.stocks[nouveau_nom] = data.stocks.pop(prod_modif)
                                    print("\n✅ Nom changé !")
                                    data.sauv_stock()
                                    data.historique(f"Rennomage de l'article {prod_modif} vers {nouveau_nom}")
                                    return
                            else:
                                while True:
                                    nouveau_quant = int(input("Entrez la nouvelle quantité : "))
                                    if nouveau_quant <= 0:
                                        print("❌ Erreur : Entrez une valeur positive : ")
                                        continue
                                    else:
                                        qunt_actu = data.stocks[prod_modif]["qte"]
                                        if nouveau_quant == qunt_actu:
                                            print("❌ Erreur : la valeur existe déjâ.")
                                            continue
                                        data.stocks[prod_modif]["qte"] = nouveau_quant
                                        print("\n✅ Quantité corrigé !")
                                        data.historique(f"Nouvelle quantité pour l'article {prod_modif} {qunt_actu} vers {nouveau_quant}")
                                        data.sauv_stock()
                                        
                                        return
                        except ValueError:
                            print("❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")

def vendre_produit():
    voir_stock()
    while True:
        prod_vend = input("\nQuel article souhaitez vous vendre (ou 'retour' pour revenir au menu principal) : ").strip().lower()
        if prod_vend == "retour":
                return
        if prod_vend not in data.stocks:
            print("\n❌ Erreur : cet article n'existe pas !")
            continue
        while True:
            try:
                    qunt_vend = int(input("\nCombien voulez vous vendre : "))
                    if qunt_vend <= 0:
                        print("❌ Erreur : Entrez une valeur positive : ")
                        continue
                    stock_dispo = data.stocks[prod_vend]["qte"]
                    if qunt_vend > stock_dispo:
                        print("\n❌ Erreur : vous avez depassez la quantité disponible en stock !")
                        continue
                    else:
                        data.stocks[prod_vend]["qte"] -= qunt_vend
                        if data.stocks[prod_vend]["qte"] <= 0:
                            data.stocks.pop(prod_vend, None)
                            print(f"\n✅ {qunt_vend} {prod_vend} vendu. Stock épuisée.\n")
                        else:
                            print(f"\n✅ {qunt_vend} {prod_vend} vendu. Stock restant : {data.stocks[prod_vend]["qte"]}\n")    
                        data.historique(f"Vente de {qunt_vend} {prod_vend}")
                        data.sauv_stock()
                        
                    return
            except ValueError:
                    print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
                    continue
                
def supprimer_stock():
    voir_stock()
    while True:
            prod_supp = input("\nQuel article souhaitez vous supprimer (ou 'retour' pour revenir au menu principal) : ").strip().lower()
            if prod_supp == "retour":
                return
            if prod_supp not in data.stocks:
                print("\n❌ Erreur : ce produit n'existe pas !")
                continue
            else:
                while True:
                    confirmation = input(f"\nÊtes-vous sûr de vouloir supprimer l'article '{prod_supp}' ? (oui/non) : ").strip().lower()
                    if confirmation != "oui" and confirmation != "non":
                        print("\n❌ Erreur : Veuillez répondre par 'oui' ou 'non'.")
                        continue
                    if confirmation == "non":
                        print("\nSuppression annulée.\n")
                        break
                    else:
                        data.stocks.pop(prod_supp, None)
                        print(f"Le produit {prod_supp} a ete supprimer 🗑️\n")
                        data.historique(f"Suppresion de l'article {prod_supp}")
                        data.sauv_stock()
                        
                        return