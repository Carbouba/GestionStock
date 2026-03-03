# Importation des modules
from customtkinter import *
from CTkMessagebox import *
from PIL import Image
import pymysql

import style as s


def get_db_connection():
        return pymysql.connect(
            host="localhost",
            user="manager",
            password="manager",
            database="stocks_manager",
        )

def add_product():
    nom = prod_name_entry.get().strip()
    quantite_str = prod_quantity_entry.get().strip()
    prix_str = prod_price_entry.get().strip()
    categorie = prod_category_entry.get().strip()

    # Verification des champs
    if not nom or not quantite_str or not prix_str or not categorie:
        CTkMessagebox(
            title="Erreur",
            message="Veuillez remplir tous les champs",
            icon="cancel"
            )
        return

    try:
        quantite = int(quantite_str)
        prix = float(prix_str)
    except ValueError:
        CTkMessagebox(
            title="Erreur",
            message="Veuillez entrer des valeurs numériques valides",
            icon="cancel"
            )
        return

    try:
        # Connexion à la base de données#
        db = get_db_connection()
        cur = db.cursor()
        # Création de la table si elle n'existe pas
        #cur.execute("CREATE TABLE IF NOT EXISTS articles (nom VARCHAR(255), quantite INT, prix_unitaire DECIMAL(10,2), categorie VARCHAR(255))")
        # Vérification si le produit existe déjà
        cur.execute("SELECT * FROM articles WHERE nom = %s", (nom,))
        # Récupération des résultats
        row = cur.fetchone()

        if quantite <= 0 or prix <= 0:
            CTkMessagebox(
                title="Erreur",
                message="La quantité et le prix doivent être supérieurs à 0",
                icon="cancel"
            )
            return

        if row is not None : # None signifie que le produit n'existe pas
            # Si le produit existe, on met à jour la quantité
            cur.execute("UPDATE articles SET quantite = quantite + %s WHERE nom = %s", (quantite, nom))
            # Fermeture des requetes et la base de données
            db.commit()
            cur.close()
            db.close()
            CTkMessagebox(title="Succés", message=f"Article ajouter avec succès", icon="info")
            prod_name_entry.delete(0, END)
            prod_quantity_entry.delete(0, END)
            prod_price_entry.delete(0, END)
            prod_category_entry.delete(0, END)
        else:
            # Si le produit n'existe pas, on l'ajoute
            cur.execute("INSERT INTO articles (nom, quantite, prix_unitaire, categorie) VALUES (%s, %s, %s, %s)", (nom, quantite, prix, categorie))
            # Fermeture des requetes et la base de données
            db.commit()
            cur.close()
            db.close()
            CTkMessagebox(title="Succés", message=f"Article ajouter avec succès", icon="info")
            prod_name_entry.delete(0, END)
            prod_quantity_entry.delete(0, END)
            prod_price_entry.delete(0, END)
            prod_category_entry.delete(0, END)
    except pymysql.MySQLError as er:
        CTkMessagebox(title="Erreur", message=f"Erreur lors de la connexion à la base de données {er}", icon="cancel")





# Création de la fenêtre principale
root = CTk()

# Personnalisation de la fenêtre
root.title("Gestionnaire de stock")
root.geometry("1800x900")
root.resizable(0, 0)
root.configure(fg_color=s.COLORS["bg2"])
# image = CTkImage(Image.open("/home/boubacar/Mes_projets_code/GestionStock/images/cover.jpg"), size=(930,500))
# imagelabel = CTkLabel(root, image=image)
# imagelabel.place(x=50 , y=0)

# Titre pricipal
top_frame = CTkFrame(root,
                 fg_color=s.COLORS["primary"],
                 width=1800, height=150,
                 corner_radius=25)
top_frame.place(x=0, y= -25)

titre = CTkLabel(top_frame,
                 text="Gestionnaire de stock",
                 justify="center",
                 font=s.FONTS["h1"],
                 text_color=s.COLORS["white"],

                 )
titre.place(x=50, y=75)

# Bouton de deconnexion
# Confirtmation de deconnexion
def confirm_logout():
    response = CTkMessagebox(title="Confirmation de déconnexion",
                             message="Êtes-vous sûr de vouloir vous déconnecter ?",
                             icon="question",
                             option_1="Oui",
                             option_2="Non")
    if response == "Oui":
        root.destroy()  # Ferme la fenêtre principale

user_icon = CTkImage(Image.open("/home/boubacar/Mes_projets_code/GestionStock/images/round-account-button-with-user-inside_icon-icons.com_72596.png"),
                     size=(35, 35))
user_icon_label = CTkLabel(top_frame,
                           image=user_icon,
                           text="",
                           )
user_icon_label.place(x=1650, y=77)

disconnect = CTkButton(top_frame,
                        text="Se déconnecter",
                        font=s.FONTS["button"],
                        fg_color=s.COLORS["success"],
                        hover_color=s.COLORS["success_hover"],
                        text_color=s.COLORS["btn_texte_color"],
                        width=120,
                        height=40,
                        corner_radius=5,
                        cursor="hand2",
                        command=confirm_logout
                        )
disconnect.place(x=1500, y=77)

# Frame principale
main_frame = CTkFrame(root,
                           fg_color=s.COLORS["white"],
                           width=1000, height=500,
                           corner_radius=10)
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

titre = CTkLabel(main_frame,
                 text="Ajouter un produit",
                 justify="center",
                 font=s.FONTS["title"],
                 text_color=s.COLORS["black"],

                 )
titre.place(x=30, y=35)

# Champs de saisies
# Nom du produit
prod_name_entry = CTkEntry(main_frame,
                            placeholder_text="Nom du produit",
                            text_color="black",
                            fg_color="white",
                            border_width=1,
                            border_color=s.COLORS["muted"],
                            width=950,
                            height=30,
                            corner_radius=5,

                            )
prod_name_entry.place(relx=0.5, y=100, anchor=CENTER)

# Quantité
prod_quantity_entry = CTkEntry(main_frame,
                            placeholder_text="Quantité",
                            text_color="black",
                            fg_color="white",
                            border_width=1,
                            border_color=s.COLORS["muted"],
                            width=950,
                            height=30,
                            corner_radius=5
                            )
prod_quantity_entry.place(relx=0.5, y=155, anchor=CENTER)

# Prix Unitaire
prod_price_entry = CTkEntry(main_frame,
                            placeholder_text="Prix Unitaire",
                            text_color="black",
                            fg_color="white",
                            border_width=1,
                            border_color=s.COLORS["muted"],
                            width=950,
                            height=30,
                            corner_radius=5
                            )
prod_price_entry.place(relx=0.5, y=210, anchor=CENTER)

# Catégorie
prod_category_entry = CTkEntry(main_frame,
                            placeholder_text="Catégorie",
                            text_color="black",
                            fg_color="white",
                            border_width=1,
                            border_color=s.COLORS["muted"],
                            width=950,
                            height=30,
                            corner_radius=5
                            )
prod_category_entry.place(relx=0.5, y=265, anchor=CENTER)

# Bouton d'ajout
add_button = CTkButton(main_frame,
                        text="Ajouter",
                        font=s.FONTS["button"],
                        fg_color=s.COLORS["success"],
                        hover_color=s.COLORS["success_hover"],
                        text_color=s.COLORS["btn_texte_color"],
                        width=120,
                        height=40,
                        corner_radius=5,
                        cursor="hand2",
                        command=add_product
                        )
add_button.place(x=26, y=320)

# Lance l'application sur le menu principal puis démarre la boucle graphique.
root.mainloop()



