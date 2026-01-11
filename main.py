# Importation de données depuis les differents fichiers
from data import stocks, charg_stock, sauv_stock
from fonctions import voir_stock, recherche_stock, vendre_produit, ajout_stock, vendre_produit, supprimer_stock, modifier_prod

# Programme principale

# Chargement de données du disque dur
charg_stock()

# Affichage du menu
while True:
    print("\n\n====== MENU GESTION STOCK ======")
    print("1. Voir le stock")
    print("2. Rechercher un article")
    print("3. Ajouter un article")
    print("4. Vendre un article")
    print("5. Supprimer un article")
    print("6. Modifier un article")
    print("7. Quitter")
    print("====================")
# Validation du choix
    try:
        option = int(input("Veuillez Choisir : "))
        if not (1 <= option <= 7) : # Dois etre entre 1 et 7
            print("❌ Erreur : Le chiffre doit être entre (1 et 6)") 
            continue   # on remonte au debut de la boucle
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
