# ============================================================
#  main_gui.py  —  Fenêtre de connexion / inscription
# ============================================================

# --- Imports ---
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image
import pymysql
import os

import style as s

# ============================================================
#  Helpers base de données
# ============================================================
def get_db_connection():
    """Retourne une connexion à la base users_data.

    Note: en production, ne pas laisser les identifiants en dur.
    """
    return pymysql.connect(
        host="localhost",
        user="gestion",
        password="admine",
        database="users_data"
    )

# ============================================================
#  Fenêtre principale
# ============================================================
root = CTk()

# Personnalisation de la fenêtre
root.title("Se connecter")
root.geometry("930x578")
root.resizable(0, 0)
root.configure(fg_color=s.COLORS["surface"])
image = CTkImage(Image.open("/home/boubacar/Mes_projets_code/GestionStock/images/cover.jpg"),
                 size=(800,470))
imagelabel = CTkLabel(root, image=image, text="")
imagelabel.place(x=180 , y=50)

# Titre pricipal
titre = CTkLabel(root,
                 text="Systéme de gestion de stock",
                 justify="center",
                 font=s.FONTS["title"],
                 text_color=s.COLORS["primary"],
                 bg_color=s.COLORS["surface"]
                 )
titre.place(x=65, y=90)

subtitle = CTkLabel(root,
                text="Gérez votre stock facilement et efficacement",
                justify="center",
                font=s.FONTS["subtitle"],
                text_color=s.COLORS["muted"],
                bg_color=s.COLORS["surface"]
                )
subtitle.place(x=65, y=120)

# Zone de saisie
type_zone_frame = CTkFrame(root,
                           fg_color=s.COLORS["bg"],
                           width=250, height=300,
                           corner_radius=10)
type_zone_frame.place(x=60, y= 160)

# ============================================================
#  Utilitaires UI
# ============================================================

def nettoyage():
    """Supprime tous les widgets du panneau de formulaire."""
    for widgets in type_zone_frame.winfo_children():
        widgets.destroy()

def go_dashboard():
    # Import local volontaire: évite les imports circulaires au chargement du fichier.
    # Ce module est importé uniquement après connexion réussie.
    import dashboard


def show_error(frame, message, y):
    """Affiche un message d'erreur temporaire (3 s) dans le frame donné."""
    msg = CTkLabel(frame,
                   text=message,
                   justify="center",
                   text_color=s.COLORS["danger_light"],
                   font=("Roboto", 13))
    msg.place(relx=0.5, y=y, anchor=CENTER)
    msg.after(3000, msg.destroy)


def highlight_error(*entries, delay=3000):
    """Met les champs en rouge, puis les remet en blanc après `delay` ms."""
    for entry in entries:
        entry.configure(border_color=s.COLORS["danger_light"])
        entry.after(delay, lambda e=entry: e.configure(border_color="white"))

# ============================================================
#  Formulaire de connexion
# ============================================================

def login_form():
    """Construit et affiche le formulaire de connexion."""
    nettoyage()
    type_zone_frame.configure(height=320)

    # ── Connexion BDD ──────────────────────────────────────
    def main_database():
        # Vérifie les identifiants en base puis redirige vers le dashboard.
        try:
            db = get_db_connection()
            cur = db.cursor()
            cur.execute(
                "SELECT * FROM users WHERE user_name = %s AND user_mdp = %s",
                (user_name_entry.get(), user_mdp_entry.get())
            )
            row = cur.fetchone()
            cur.close()
            db.close()

            if row is not None:
                root.destroy()
                go_dashboard()
            else:
                show_error(type_zone_frame, "Nom d'utilisateur ou\nmot de passe incorrect", 280)
                user_name_entry.delete(0, END)
                user_mdp_entry.delete(0, END)

        except pymysql.MySQLError as e:
            CTkMessagebox(title="Erreur",
                          message=f"Erreur de connexion à la base de données :\n{e}",
                          icon="cancel")

    # ── Validation formulaire ──────────────────────────────
    def login_infos_check():
        # Évite un aller-retour DB si les champs sont déjà vides.
        if not user_name_entry.get() or not user_mdp_entry.get():
            highlight_error(user_name_entry, user_mdp_entry)
            show_error(type_zone_frame, "Veuillez remplir tous les champs", 280)
        else:
            main_database()

    # ── Widgets ────────────────────────────────────────────
    titre_label = CTkLabel(type_zone_frame,
        text="Se connecter",
        text_color=s.COLORS["primary"],
        font=("Helvetica", 18, "bold"),
    )
    titre_label.place(x=32, y=12)

    sub_new_label = CTkLabel(type_zone_frame,
        text="Saisissez les identifiants de votre compte",
        text_color=s.COLORS["muted"],
        font=("Roboto", 10)
    )
    sub_new_label.place(x=32, y=30)

    username_plas_label = CTkLabel(type_zone_frame,
        text="Nom d'utilisateur",
        text_color=s.COLORS["muted"],
        font=("Roboto", 10)
    )
    username_plas_label.place(x=34, y=53)

    user_name_entry = CTkEntry(type_zone_frame,
        placeholder_text="",
        text_color="black",
        fg_color="white",
        border_width=2,
        border_color=s.COLORS["bg"],
        width=190,
        height=30,
        corner_radius=5
    )
    user_name_entry.place(x=32, y=75)

    mdp_plas_label = CTkLabel(type_zone_frame,
        text="Mot de passe",
        text_color=s.COLORS["muted"],
        font=("Roboto", 10)
    )
    mdp_plas_label.place(x=34, y=105)

    user_mdp_entry = CTkEntry(type_zone_frame,
        placeholder_text="",
        text_color="black",
        fg_color="white",
        border_width=2,
        border_color=s.COLORS["bg"],
        width=190,
        height=30,
        corner_radius=5,
        show="*"
    )
    user_mdp_entry.place(x=32, y=125)

    forgot_mdp_link = CTkButton(
        type_zone_frame,
        text="Mot de passe oublié ?",
        text_color=s.COLORS["muted"],
        font=("Roboto", 10),
        fg_color=s.COLORS["bg"],
        bg_color=s.COLORS["bg"],
        hover=False,
        cursor="hand2",
        width=100,
        height=5,
        command=forgot_password_form
    )
    forgot_mdp_link.place(x=123, y=155)

    login_btn = CTkButton(type_zone_frame,
        text="Se connecter",
        font=("Roboto", 15),
        text_color="white",
        fg_color=s.COLORS["success"],
        hover_color=s.COLORS["success_hover"],
        corner_radius=5,
        cursor="hand2",
        command=login_infos_check,
        width=190
    )
    login_btn.place(x=32, y=185)

    creat_new_label = CTkLabel(type_zone_frame,
                        text="Vous n'avez pas encore de compte ?",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    creat_new_label.place(x=43, y=215)

    creat_new_link = CTkButton(type_zone_frame,
                        text="Créer un compte",
                        text_color=s.COLORS["primary"],
                        font=("Roboto", 13, "bold"),
                        fg_color=s.COLORS["bg"],
                        cursor="hand2",
                        hover=False,
                        height=20,
                        width=50,
                        command=sign_up_form
                        )
    creat_new_link.place(x=63, y=235)

#######################################################################################

# ============================================================
#  Formulaire d'inscription
# ============================================================

def sign_up_form():
    """Construit et affiche le formulaire de création de compte."""
    nettoyage()
    type_zone_frame.configure(height=390)

    # ── Connexion BDD ──────────────────────────────────────
    def main_database():
        name  = user_name_entry.get().strip()
        mail  = email_entry.get().strip()
        mdp   = user_mdp_entry.get()

        try:
            db  = get_db_connection()
            cur = db.cursor()

            # Contrôle d'unicité: on bloque si le nom utilisateur OU l'email existe déjà.
            cur.execute(
                "SELECT 1 FROM users WHERE user_name = %s OR user_email = %s",
                (name, mail)
            )
            rows = cur.fetchall()

            if rows:
                show_error(type_zone_frame,
                           "Cet email ou nom d'utilisateur\nexiste déjà", y=365)
            else:
                cur.execute(
                    "INSERT INTO users (user_name, user_email, user_mdp) VALUES (%s, %s, %s)",
                    (name, mail, mdp)
                )
                db.commit()
                CTkMessagebox(title="Succès",
                              message="Compte créé avec succès. Connectez-vous.",
                              icon="info")
                # Nettoyage du formulaire après succès pour repartir sur un état propre.
                for entry in (user_name_entry, email_entry,
                              user_mdp_entry, conf_user_mdp_entry):
                    entry.delete(0, END)
                login_form()

            cur.close()
            db.close()

        except pymysql.MySQLError as e:
            CTkMessagebox(title="Erreur",
                          message=f"Erreur de connexion à la base de données :\n{e}",
                          icon="cancel")

    # ── Validation formulaire ──────────────────────────────
    def sign_up_infos_check():
        # Chaîne de validations: on s'arrête au premier problème rencontré.
        name  = user_name_entry.get()
        mail  = email_entry.get()
        mdp   = user_mdp_entry.get()
        cmdp  = conf_user_mdp_entry.get()

        if not name or not mail or not mdp or not cmdp:
            highlight_error(user_name_entry, email_entry,
                            user_mdp_entry, conf_user_mdp_entry)
            show_error(type_zone_frame, "Veuillez remplir tous les champs", 365)

        elif "@" not in mail or "." not in mail.split("@")[-1]:
            # Validation email générique (pas seulement @gmail.com)
            highlight_error(email_entry)
            show_error(type_zone_frame, "Adresse email invalide. \nex: votrenom@gmail.com", 365)

        elif mdp != cmdp:
            highlight_error(user_mdp_entry, conf_user_mdp_entry)
            show_error(type_zone_frame, "Les mots de passe\nne correspondent pas", 365)

        elif " " in mdp:
            show_error(type_zone_frame,
                       "Les espaces ne sont pas autorisés\ndans le mot de passe.", 365)

        elif len(mdp) < 6:
            highlight_error(user_mdp_entry, conf_user_mdp_entry)
            show_error(type_zone_frame,
                       "Le mot de passe doit contenir\nau moins 6 caractères.", 365)

        else:
            main_database()

    # ── Widgets ────────────────────────────────────────────
    titre_label = CTkLabel(type_zone_frame,
                       text="Créer un compte",
                       text_color=s.COLORS["primary"],
                       font=("Helvetica", 18, "bold"),

                       )
    titre_label.place(x=32, y=12)

    sub_new_label = CTkLabel(type_zone_frame,
                        text="Remplissez les champs suivants pour \ncréer un compte",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10),
                        justify="left"
                        )
    sub_new_label.place(x=32, y=35)

    # Grille : LABEL_ENTRY_GAP=20px (placeholder→entry), FIELD_SPACING=14px (entre couples)
    Y_START, LABEL_ENTRY_GAP = 70, 20
    FIELD_SPACING = 0

    y = Y_START
    username_plas_label = CTkLabel(type_zone_frame,
                        text="Nom d'utilisateur",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    username_plas_label.place(x=34, y=y)
    y += LABEL_ENTRY_GAP
    user_name_entry = CTkEntry(type_zone_frame,
                            placeholder_text="",
                            text_color="black",
                            fg_color="white",
                            border_width=2,
                            border_color=s.COLORS["bg"],
                            width=190,
                            height=30,
                            corner_radius=5
                            )
    user_name_entry.place(x=34, y=y)

    y += 30 + FIELD_SPACING
    email_plas_label = CTkLabel(type_zone_frame,
                        text="Email",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    email_plas_label.place(x=34, y=y)
    y += LABEL_ENTRY_GAP
    email_entry = CTkEntry(type_zone_frame,
                            placeholder_text="",
                            text_color="black",
                            fg_color="white",
                            border_width=2,
                            border_color=s.COLORS["bg"],
                            width=190,
                            height=30,
                            corner_radius=5
                            )
    email_entry.place(x=34, y=y)

    y += 30 + FIELD_SPACING
    mdp_plas_label = CTkLabel(type_zone_frame,
                        text="Mot de passe",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    mdp_plas_label.place(x=34, y=y)
    y += LABEL_ENTRY_GAP
    user_mdp_entry = CTkEntry(type_zone_frame,
                            placeholder_text="",
                            text_color="black",
                            fg_color="white",
                            border_width=2,
                            border_color=s.COLORS["bg"],
                            width=190,
                            height=30,
                            corner_radius=5,
                            show="*"
                            )
    user_mdp_entry.place(x=34, y=y)

    y += 30 + FIELD_SPACING
    conf_mdp_plas_label = CTkLabel(type_zone_frame,
                        text="Confirmez le mot de passe",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    conf_mdp_plas_label.place(x=34, y=y)
    y += LABEL_ENTRY_GAP
    conf_user_mdp_entry = CTkEntry(type_zone_frame,
                            placeholder_text="",
                            text_color="black",
                            fg_color="white",
                            border_width=2,
                            border_color=s.COLORS["bg"],
                            width=190,
                            height=30,
                            corner_radius=5,
                            show="*"
                            )
    conf_user_mdp_entry.place(x=34, y=y)

    y += 40 + FIELD_SPACING
    sign_up_btn = CTkButton(type_zone_frame,
                        text="Créer un compte",
                        font=("Roboto", 15),
                        text_color="white",
                        fg_color=s.COLORS["success"],
                        hover_color=s.COLORS["success_hover"],
                        corner_radius=5,
                        cursor="hand2",
                        command=sign_up_infos_check,
                        width=190,
                        )
    sign_up_btn.place(x=34, y=y)

    y += 42
    creat_new_label = CTkLabel(type_zone_frame,
                        text="Vous avez deja un compte ?",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    creat_new_label.place(relx=0.5, y=y, anchor=CENTER)

    creat_new_link = CTkButton(type_zone_frame,
                        text="Se connecter",
                        text_color=s.COLORS["primary"],
                        font=("Roboto", 13, "bold"),
                        fg_color=s.COLORS["bg"],
                        cursor="hand2",
                        hover=False,
                        height=20,
                        width=50,
                        command=login_form
                        )
    creat_new_link.place(relx=0.5, y=y+15, anchor=CENTER)

##################################################################################

# ============================================================
#  Formulaire mot de passe oublié
# ============================================================

def forgot_password_form():
    """Construit le formulaire de récupération mot de passe (version UI simple)."""
    nettoyage()

    type_zone_frame.configure(height=240)

    def sign_up_infos_check():
        # TODO: remplacer ce contrôle local par une vraie vérification en base + envoi mail.
        if user_name_recover_entry.get() == "":
            user_name_recover_entry.configure(border_color=s.COLORS["danger_light"])
            user_name_recover_entry.after(3000, lambda:user_name_recover_entry.configure(border_color="white"))

            show_error(type_zone_frame, "Veuillez remplir tous les champs",220)

        elif user_name_recover_entry.get() != "adm":
            user_name_recover_entry.configure(border_color=s.COLORS["danger_light"])
            user_name_recover_entry.after(3000, lambda:user_name_recover_entry.configure(border_color="white"))

            show_error(type_zone_frame, "Ce email n'existe pas", 220)

        else:
            # Emplacement prévu pour l'action réelle de récupération.
            pass
            # user_name_recover_entry.delete(0, END)
            # msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes


    titre_label = CTkLabel(type_zone_frame,
         text="Reinitialiser le mot de passe",
            text_color=s.COLORS["primary"],
            font=("Helvetica", 15, "bold"),

            )
    titre_label.place(x=32, y=12)

    label = CTkLabel(type_zone_frame,
         text="Entrez votre email pour \nréinitialiser votre mot de passe",
            text_color=s.COLORS["muted"],
            font=("Roboto", 12),
            justify="center"
            )
    label.place(relx=0.5, y=50, anchor=CENTER)

    user_name_recover_label = CTkLabel(type_zone_frame,
                        text="Email",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    user_name_recover_label.place(x=34, y=70)

    user_name_recover_entry = CTkEntry(type_zone_frame,
                            placeholder_text="",
                            text_color="black",
                            fg_color="white",
                            border_width=2,
                            border_color=s.COLORS["bg"],
                            width=190,
                            height=30,
                            corner_radius=5
                            )
    user_name_recover_entry.place(x=32, y=90)


    submit_btn = CTkButton(type_zone_frame,
                        text="Envoyer",
                        font=("Roboto", 15),
                        text_color="white",
                        fg_color=s.COLORS["success"],
                        hover_color=s.COLORS["success_hover"],
                        corner_radius=5,
                        cursor="hand2",
                        command=sign_up_infos_check,
                        width=190
                        )
    submit_btn.place(relx=0.5, y=145, anchor=CENTER)

    label_cancel = CTkButton(type_zone_frame,
                        text="Annuler",
                        font=("Roboto", 15),
                        text_color=s.COLORS["danger"],
                        fg_color=s.COLORS["bg"],
                        hover_color=s.COLORS["danger_light"],
                        corner_radius=5,
                        border_color=s.COLORS["danger_light"],
                        border_width=2,
                        cursor="hand2",
                        width=190,
                        command=login_form
                        )
    label_cancel.place(relx=0.5, y=185, anchor=CENTER)

############################################################################
# Démarrage
login_form()
# Lance l'application sur le menu principal puis démarre la boucle graphique.
root.mainloop()

# Aucune ligne de code ne doit être ajoutée après cette ligne.
