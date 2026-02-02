# Importation de données depuis les differents fichiers
import data
import fonctions as f

# Programme principal

# Chargement de données du disque dur
data.charg_stock()

# Affichage du menu
while True:
    print("\n\n====== MENU GESTION STOCK ======")
    print("1. Voir le stock")
    print("2. Voir l'historique")
    print("3. Rechercher un article")
    print("4. Ajouter un article")
    print("5. Vendre un article")
    print("6. Supprimer un article")
    print("7. Modifier un article")
    print("8. Quitter")
    print("====================")
# Validation du choix
    try:
        # Lecture et validation de l'option utilisateur.
        option = int(input("Veuillez choisir : "))
        if not (1 <= option <= 8) : # Doit être entre 1 et 8
            print("❌ Erreur : Le chiffre doit être entre 1 et 8.") 
            continue   # on remonte au debut de la boucle
    except ValueError:
        print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
        continue

    # Routage vers la fonction correspondant au choix.
    match option:
        case 1:
            f.voir_stock()
        case 2:
            #print("\n⏳ Bientot disponible")
            data.voir_historique()
        case 3:
            f.recherche_stock()
        case 4:
            f.ajout_stock()
        case 5:
            f.vendre_produit()
        case 6:
            f.supprimer_stock()
        case 7:
            f.modifier_prod()
        case 8:
            data.sauv_stock()
            break

# Rien à ajouter après cette ligne