def voir_stock():
    print("Salut")
    return
def ajout_stock():
    return
def vendre_produit():
    return

stocks = {}

# Programme principale
while True:
    print("\n\n====== MENU GESTION STOCK ======\n")
    print("1. Voir le stock")
    print("2. Ajouter du stock (Approvisionnement)")
    print("3. Vendre un produit (Retrait)")
    print("4. Quitter")
    print("====================")

    try:
        option = int(input("Vzuillez Choisir : "))
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
