# Importation de données des differents fichiers
import data

# Fonction pour afficher la liste des articles
def voir_stock():
    # Affiche le stock sous forme de tableau lisible.
    total_stock = len(data.stocks)
    # Cas particulier: stock vide.
    if total_stock == 0:
        print(f"Aucun article disponible pour le moment !")
    else:
        # En-tête d'affichage.
        print("\n===== Liste des articles en stock =====\n")
        print("-" * 65)
        print(f"{'Article':<15} | {'Stock':>6} | {'Catégorie':<15} | {'Prix unitaire':>12}")
        print("-" * 65)
        # Parcours et affichage des articles.
        for nom, infos in data.stocks.items(): # On parcour le dictionaire tout entier
            quantite = infos['qte']
            categorie = infos["cat"]
            prix_unitaire = infos["prx"]
            print(f"{nom.capitalize():<15} | {quantite:>6} | {categorie.capitalize():<15} | {prix_unitaire:>10} Franc CFA")
        #print("_________________________________")
    return

# Fonction pour rechercher un article
def recherche_stock():
    # Gère la recherche interactive d'un article par son nom.
    total_stock = len(data.stocks)
    # Cas particulier: stock vide.
    if total_stock == 0:
        print(f"Aucun article disponible pour le moment !")
    else:
        print("\n===== Rechercher un article =====\n")
        while True:
            # Saisie du nom à rechercher ou retour au menu.
            prod_recherche = input("Entrez le nom de l'article à rechercher (ou 'retour' pour revenir au menu principal) : ").strip().lower()
            if prod_recherche == "retour":
                return
            if prod_recherche == "": # Si l'utilisateur ne tape rien et valide
                print("\n❌ Erreur : Vous devez saisir un nom correct : ")
                continue
            # Validation de l'existence de l'article.
            if prod_recherche not in data.stocks:
                print("Erreur : cet article n'existe pas.")
                continue
            else:
                print("\nRésultat de la recherche : ")
                quantite = data.stocks[prod_recherche]['qte']
                categorie = data.stocks[prod_recherche]["cat"]
                prix_unitaire = data.stocks[prod_recherche]["prx"]
                # Affichage du résultat trouvé.
                print("-" * 50)
                print(f"{prod_recherche:<10} {quantite:>5} {categorie:>10} {prix_unitaire:>10} Franc CFA")
                print("-" * 50)
            #print("_________________________________")
    return

def ajout_stock():
    # Ajoute un nouvel article ou augmente la quantité d'un article existant.
    while True:
        try:
            # Saisie du nom du produit ou retour.
            nom_prod = input("\nEntrez le nom de l'article (ou 'retour' pour revenir au menu principal) : ").strip().lower()
            if nom_prod == "retour":
                return
            if nom_prod == "":
                print("\n❌ Erreur : Vous devez saisir un nom correct : ")
                continue
            
            # Si l'article existe déjà, on ajoute une quantité.
            if nom_prod in data.stocks:
                # Message d'information affiché une seule fois.
                print(f"\nIl y en a déjà {data.stocks[nom_prod]['qte']}.")
                while True:
                    # Redemande tant que la quantité n'est pas valide.
                    quantite = int(input("Combien voulez-vous en ajouter : "))
                    if quantite <= 0:
                        print("\n❌ Erreur : Entrez une valeur positive : ")
                    else:
                        #categorie = input("Entrez la catégorie du produit : ")
                        data.stocks[nom_prod]['qte'] += quantite
                        print("\n✅ Quantité ajoutée !")
                        #sauv_stock(nom_prod, quantite)
                        break
            else:
                # Sinon, création d'un nouvel article.
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
                        data.stocks[nom_prod] = {'qte' : int(quantite), "cat" : categorie, "prx" : int(prix_unitaire)}
                        print("\n✅ Article ajouté !")
                        break
                    break              
        except ValueError:
            print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
            continue
    
        # Trace et sauvegarde après ajout.
        data.historique(f"Ajout ({nom_prod} : +{quantite})")
        data.sauv_stock()
        

def modifier_prod():
    # Permet de renommer un article ou d'ajuster sa quantité.
    voir_stock()
    while True:
                # Saisie de l'article à modifier.
                prod_modif = input("\nQuel article souhaitez-vous modifier (ou 'retour' pour revenir au menu principal) : ").strip().lower()
                if prod_modif == "retour":
                    return
                if prod_modif not in data.stocks:
                    print("Erreur : cet article n'existe pas.")
                    continue
                else:
                    print(f"Modification de '{prod_modif}' (stock actuel : {data.stocks[prod_modif]['qte']})")
                    print("1. Renommer")
                    print("2. Corriger la quantité")
                    while True:
                        try:
                            # Choix du type de modification.
                            choix = int(input("Votre choix : "))
                            if not (1 <= choix <= 2):
                                print("Erreur : choix invalide, choisissez (1-2).")
                                continue
                            if choix == 1:
                                # Renommage de l'article.
                                nouveau_nom = input("Entrez le nouveau nom (ou 'Annuler' pour revenir au menu principal): ").strip().lower()
                                if nouveau_nom == "":
                                    print("❌ Erreur : Vous devez saisir un nom correct : ")
                                    continue
                                if nouveau_nom == "annuler":
                                    return
                                if nouveau_nom in data.stocks:
                                    print(f"❌ Erreur : L'article '{nouveau_nom}' existe déjà !")
                                    return
                                else:
                                    data.stocks[nouveau_nom] = data.stocks.pop(prod_modif)
                                    print("\n✅ Nom changé !")
                                    data.sauv_stock()
                                    data.historique(f"Renommage ({prod_modif} -> {nouveau_nom})")
                                    return
                            else:
                                while True:
                                    # Mise à jour de la quantité.
                                    nouveau_quant = int(input("Entrez la nouvelle quantité (ou 'Annuler' pour revenir au menu principal) : "))
                                    if nouveau_quant == "annuler":
                                        return
                                    if nouveau_quant <= 0:
                                        print("❌ Erreur : Entrez une valeur positive : ")
                                        continue
                                    else:
                                        qunt_actu = data.stocks[prod_modif]['qte']
                                        if nouveau_quant == qunt_actu:
                                            print("❌ Erreur : la valeur existe déjà.")
                                            continue
                                        data.stocks[prod_modif]['qte'] = nouveau_quant
                                        print("\n✅ Quantité corrigée !")
                                        data.historique(f"Quantité modifiée ({prod_modif} : {qunt_actu} -> {nouveau_quant})")
                                        data.sauv_stock()
                                        
                                        return
                        except ValueError:
                            print("❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")

def vendre_produit():
    # Décrémente le stock d'un article suite à une vente.
    voir_stock()
    while True:
        # Saisie de l'article à vendre.
        prod_vend = input("\nQuel article souhaitez-vous vendre (ou 'retour' pour revenir au menu principal) : ").strip().lower()
        if prod_vend == "retour":
                return
        if prod_vend not in data.stocks:
            print("\n❌ Erreur : cet article n'existe pas !")
            continue
        while True:
            try:
                    # Saisie de la quantité à vendre.
                    qunt_vend = int(input("\nCombien voulez-vous vendre : "))
                    if qunt_vend <= 0:
                        print("❌ Erreur : Entrez une valeur positive : ")
                        continue
                    stock_dispo = data.stocks[prod_vend]['qte']
                    # Validation du stock disponible.
                    if qunt_vend > stock_dispo:
                        print("\n❌ Erreur : vous avez dépassé la quantité disponible en stock !")
                        continue
                    else:
                        stock_epuise = False
                        data.stocks[prod_vend]['qte'] -= qunt_vend
                        # Si le stock tombe à zéro, on supprime l'article.
                        if data.stocks[prod_vend]['qte'] <= 0:
                            data.stocks.pop(prod_vend, None)
                            stock_epuise = True
                            print(f"\n✅ {qunt_vend} {prod_vend} vendu. Stock épuisé.\n")
                        else:
                            print(f"\n✅ {qunt_vend} {prod_vend} vendu. Stock restant : {data.stocks[prod_vend]['qte']}\n")    
                        # Trace et sauvegarde après vente.
                        if stock_epuise:
                            data.historique(f"Vente de {qunt_vend} {prod_vend} (stock épuisé)")
                        else:
                            stock_restant = data.stocks[prod_vend]['qte']
                            data.historique(f"Vente de {qunt_vend} {prod_vend} (stock restant : {stock_restant})")
                        data.sauv_stock()
                        prix_unitaire = data.stocks[prod_vend]['prx']
                        total = qunt_vend * prix_unitaire
                        print("===== FACTURE DE VENTE =====\n")
                        print("-" * 70)
                        print(f"{'Designation':<15} | {'Quantité':>6} | {'Prix unitaire':<15} | {'Total':>12}")
                        print("-" * 70)
                        print(f"{prod_vend.capitalize():<15} | {qunt_vend:>8} | {prix_unitaire:>5} Franc CFA | {total:>8} Franc CFA")

                        
                    return
            except ValueError:
                    print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
                    continue
                
def supprimer_stock():
    # Supprime un article du stock après confirmation.
    voir_stock()
    while True:
            # Saisie de l'article à supprimer.
            prod_supp = input("\nQuel article souhaitez-vous supprimer (ou 'retour' pour revenir au menu principal) : ").strip().lower()
            if prod_supp == "retour":
                return
            if prod_supp not in data.stocks:
                print("\n❌ Erreur : ce produit n'existe pas !")
                continue
            else:
                while True:
                    # Confirmation explicite avant suppression.
                    confirmation = input(f"\nÊtes-vous sûr de vouloir supprimer l'article '{prod_supp}' ? (oui/non) : ").strip().lower()
                    if confirmation != "oui" and confirmation != "non":
                        print("\n❌ Erreur : Veuillez répondre par 'oui' ou 'non'.")
                        continue
                    if confirmation == "non":
                        print("\nSuppression annulée.\n")
                        break
                    else:
                        data.stocks.pop(prod_supp, None)
                        print(f"Le produit {prod_supp} a été supprimé 🗑️\n")
                        # Trace et sauvegarde après suppression.
                        data.historique(f"Suppression ({prod_supp})")
                        data.sauv_stock()
                        
                        return

# Rien à ajouter après cette ligne

