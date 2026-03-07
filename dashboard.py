# ============================================================
#  dashboard.py  —  Tableau de bord / gestion des produits
# ============================================================

# --- Imports ---
from customtkinter import *
from CTkMessagebox import *
from PIL import Image
import pymysql

import style as s


# ============================================================
#  Helpers base de données
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_db_connection():
    """Retourne une connexion à la base stocks_manager."""
    return pymysql.connect(
        host="localhost",
        user="gestion",
        password="admine",
        database="stocks_manager"
    )

# ============================================================
#  Logique métier
# ============================================================

def add_product():
    nom           = prod_name_entry.get().strip()
    quantite_str  = prod_quantity_entry.get().strip()
    prix_str      = prod_price_entry.get().strip()
    categorie     = prod_category_entry.get().strip()

    # ── 1. Vérification champs vides ──────────────────────
    if not nom or not quantite_str or not prix_str or not categorie:
        CTkMessagebox(title="Erreur",
                      message="Veuillez remplir tous les champs",
                      icon="cancel")
        return

    # ── 2. Validation types numériques ────────────────────
    try:
        quantite = int(quantite_str)
        prix     = float(prix_str)
    except ValueError:
        CTkMessagebox(title="Erreur",
                      message="La quantité doit être un entier\net le prix un nombre décimal.",
                      icon="cancel")
        return

    # ── 3. Règles métier (AVANT la BDD) ───────────────────
    # BUG CORRIGÉ : ces vérifications étaient faites APRÈS la requête SELECT,
    # ce qui pouvait lancer une requête inutile avec des données invalides.
    if quantite <= 0 or prix <= 0:
        CTkMessagebox(title="Erreur",
                      message="La quantité et le prix doivent être supérieurs à 0",
                      icon="cancel")
        return

    # ── 4. Opérations base de données ─────────────────────
    db  = None
    cur = None
    try:
        db  = get_db_connection()
        cur = db.cursor()

        cur.execute("SELECT 1 FROM articles WHERE nom = %s", (nom,))
        row = cur.fetchone()

        if row is not None:
            # Produit existant → mise à jour de la quantité
            cur.execute(
                "UPDATE articles SET quantite = quantite + %s WHERE nom = %s",
                (quantite, nom)
            )
            db.commit()  # BUG CORRIGÉ : commit manquant après UPDATE
            CTkMessagebox(title="Mise à jour",
                          message=f"Stock de '{nom}' mis à jour (+{quantite})",
                          icon="info")
        else:
            # Nouveau produit → insertion
            cur.execute(
                "INSERT INTO articles (nom, quantite, prix_unitaire, categorie) "
                "VALUES (%s, %s, %s, %s)",
                (nom, quantite, prix, categorie)
            )
            db.commit()
            CTkMessagebox(message="Article ajouté avec succès", icon="info")

        # Remise à zéro des champs après succès
        for entry in (prod_name_entry, prod_quantity_entry,
                      prod_price_entry, prod_category_entry):
            entry.delete(0, END)

    except pymysql.MySQLError as e:
        CTkMessagebox(title="Erreur",
                      message=f"Erreur base de données :\n{e}",
                      icon="cancel")

    finally:
        # BUG CORRIGÉ : close() dans un bloc finally → toujours exécuté,
        # même si une exception est levée.
        if cur: cur.close()
        if db:  db.close()


# ============================================================
#  Fenêtre principale
# ============================================================

root = CTk()
root.title("Gestionnaire de stock")
root.geometry("1800x900")
root.resizable(0, 0)
root.configure(fg_color=s.COLORS["bg2"])

# ── Header ─────────────────────────────────────────────────
top_frame = CTkFrame(root,
                     fg_color=s.COLORS["primary"],
                     width=1800, height=150,
                     corner_radius=25)
top_frame.place(x=0, y=-25)

CTkLabel(top_frame,
         text="Gestionnaire de stock",
         justify="center",
         font=s.FONTS["h1"],
         text_color=s.COLORS["white"]).place(x=50, y=75)

# ── Déconnexion ────────────────────────────────────────────
def confirm_logout():
    response = CTkMessagebox(
        title="Confirmation de déconnexion",
        message="Êtes-vous sûr de vouloir vous déconnecter ?",
        icon="question",
        option_1="Oui",
        option_2="Non"
    )
    # BUG CORRIGÉ : CTkMessagebox.get() retourne le texte du bouton cliqué.
    # L'ancienne comparaison `response == "Oui"` comparait un objet à une string
    # → toujours False, la déconnexion ne fonctionnait jamais.
    if response.get() == "Oui":
        root.destroy()
        import main_gui  # Retour à l'écran de connexion

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



