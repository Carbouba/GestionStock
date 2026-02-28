# Importation des modules
from customtkinter import *
from CTkMessagebox import *
from PIL import Image

import style as s

# Création de la fenêtre principale
root = CTk()

# Personnalisation de la fenêtre
root.title("Se connecter")
root.geometry("930x578")
root.resizable(0, 0)
root.configure(fg_color=s.COLORS["surface"])
image = CTkImage(Image.open("/home/boubacar/Mes_projets_code/GestionStock/cover.jpg"),
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

# def switch_main_image(switc_shoix):
#     image = CTkImage(Image.open("/home/boubacar/Mes_projets_code/GestionStock/images/authentication.png"),
#                  size=(500,470))
#     if switc_shoix == "signup":
#         image.CTkImage.configure(Image.open("/home/boubacar/Mes_projets_code/GestionStock/images/man-with-join-us-sign-for-open-recruitment.png"),
#                  size=(500,470))
#         sign_up_form()


#
def nettoyage():
    for widgets in type_zone_frame.winfo_children():
        widgets.destroy()

def go_dashboard():
    import dashboard


def login_form():

    nettoyage()

    type_zone_frame.configure(height=320)

    """ Fonction qui verifie si les champs du formulaire sont vides ou pas,
    si oui elle affiche un message d'erreur et met en surbrillance les champs vides,
    sinon elle ajoute l'employé à la base de données et affiche un message de succès. """

    def login_infos_check():
        if user_name_entry.get() == "" or user_mdp_entry.get() == "":
            user_name_entry.configure(border_color=s.COLORS["danger_light"])
            user_mdp_entry.configure(border_color=s.COLORS["danger_light"])
            user_name_entry.after(3000, lambda:user_name_entry.configure(border_color="white"))
            user_mdp_entry.after(3000, lambda:user_mdp_entry.configure(border_color="white"))
            msg = CTkLabel(type_zone_frame,
                    text="Veuillez remplir tous les champs", justify="center",
                    font=("Roboto", 13),
                    text_color=s.COLORS["danger_light"])
            msg.place(relx=0.5, y=280, anchor=CENTER)
            msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes


        elif user_name_entry.get() == "adm" and user_mdp_entry.get() == "adm":
            root.destroy()
            go_dashboard()

        else:
            msg = CTkLabel(type_zone_frame,
                    text="Nom d'utilisateur ou \n mot de passe incorrect", justify="center",
                    font=("Roboto", 13),
                    text_color=s.COLORS["danger_light"])
            msg.place(relx=0.5, y=280, anchor=CENTER)

            user_name_entry.delete(0, END)
            user_mdp_entry.delete(0, END)
            msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes

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
                        text="Email ou nom d'utilisateur",
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

    # check_box = CTkCheckBox(type_zone_frame,
    #                         text="Afficher le mot de passe",
    #                         command=lambda: toggle_password_visibility(user_mdp_entry.get()))
    # check_box.place(x=32, y=215)

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

def sign_up_form():

    nettoyage()

    type_zone_frame.configure( height=350)


    """ Fonction qui verifie si les champs du formulaire sont vides ou pas,
    si oui elle affiche un message d'erreur et met en surbrillance les champs vides,
    sinon elle ajoute l'employé à la base de données et affiche un message de succès. """


    def sign_up_infos_check():
        if user_name_entry.get() == "" or user_mdp_entry.get() == "" or conf_user_mdp_entry.get() == "":
            user_name_entry.configure(border_color=s.COLORS["danger_light"])
            user_mdp_entry.configure(border_color=s.COLORS["danger_light"])
            conf_user_mdp_entry.configure(border_color=s.COLORS["danger_light"])
            user_name_entry.after(3000, lambda:user_name_entry.configure(border_color="white"))
            user_mdp_entry.after(3000, lambda:user_mdp_entry.configure(border_color="white"))
            conf_user_mdp_entry.after(3000, lambda:conf_user_mdp_entry.configure(border_color="white"))
            msg = CTkLabel(type_zone_frame,
                    text="Veuillez remplir tous les champs", justify="center",
                    font=("Roboto", 13),
                    text_color=s.COLORS["danger_light"])
            msg.place(x=33, y=295)
            msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes

        elif conf_user_mdp_entry.get() != user_mdp_entry.get():
            user_mdp_entry.configure(border_color=s.COLORS["danger_light"])
            conf_user_mdp_entry.configure(border_color=s.COLORS["danger_light"])
            user_mdp_entry.after(3000, lambda:user_mdp_entry.configure(border_color="white"))
            conf_user_mdp_entry.after(3000, lambda:conf_user_mdp_entry.configure(border_color="white"))
            msg = CTkLabel(type_zone_frame,
                    text="Les mots de passe \nne correspondent pas", justify="center",
                    font=("Roboto", 13),
                    text_color=s.COLORS["danger_light"])
            msg.place(relx=0.5, y=315, anchor=CENTER)
            msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes

        else:
            pass
            # user_name_entry.delete(0, END)
            # user_mdp_entry.delete(0, END)
            # msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes

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

    user_name_frame = CTkFrame(type_zone_frame, fg_color=s.COLORS["bg"])
    user_name_frame.place(x=34, y=65)

    username_plas_label = CTkLabel(user_name_frame,
                        text="Nom d'utilisateur",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    username_plas_label.place(x=0, y=0)

    user_name_entry = CTkEntry(user_name_frame,
                            placeholder_text="",
                            text_color="black",
                            fg_color="white",
                            border_width=2,
                            border_color=s.COLORS["bg"],
                            width=190,
                            height=30,
                            corner_radius=5
                            )
    user_name_entry.place(x=0, y=0)

    username_mail_label = CTkLabel(type_zone_frame,
                        text="Adresse email",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    username_mail_label.place(x=34, y=65)

    user_mail_entry = CTkEntry(type_zone_frame,
                            placeholder_text="",
                            text_color="black",
                            fg_color="white",
                            border_width=2,
                            border_color=s.COLORS["bg"],
                            width=190,
                            height=30,
                            corner_radius=5
                            )
    user_mail_entry.place(x=32, y=85)


    mdp_plas_label = CTkLabel(type_zone_frame,
                        text="Mot de passe",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    mdp_plas_label.place(x=34, y=115)

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
    user_mdp_entry.place(x=32, y=135)

    conf_mdp_plas_label = CTkLabel(type_zone_frame,
                        text="Confirmez le mot de passe",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    conf_mdp_plas_label.place(x=34, y=165)

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
    conf_user_mdp_entry.place(x=32, y=185)

    sign_up_btn = CTkButton(type_zone_frame,
                        text="Créer un compte",
                        font=("Roboto", 15),
                        text_color="white",
                        fg_color=s.COLORS["success"],
                        hover_color=s.COLORS["success_hover"],
                        corner_radius=5,
                        cursor="hand2",
                        command=sign_up_infos_check,
                        width=190
                        )
    sign_up_btn.place(x=32, y=225)

    creat_new_label = CTkLabel(type_zone_frame,
                        text="Vous avez deja un compte ?",
                        text_color=s.COLORS["muted"],
                        font=("Roboto", 10)
                        )
    creat_new_label.place(x=63, y=255)

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
    creat_new_link.place(x=80, y=275)

##################################################################################

def forgot_password_form():
    nettoyage()

    type_zone_frame.configure(height=220)

    """ Fonction qui verifie si les champs du formulaire sont vides ou pas,
    si oui elle affiche un message d'erreur et met en surbrillance les champs vides,
    sinon elle ajoute l'employé à la base de données et affiche un message de succès. """


    def sign_up_infos_check():
        if user_name_recover_entry.get() == "":
            user_name_recover_entry.configure(border_color=s.COLORS["danger_light"])
            user_name_recover_entry.after(3000, lambda:user_name_recover_entry.configure(border_color="white"))
            msg = CTkLabel(type_zone_frame,
                    text="Veuillez remplir tous les champs", justify="center",
                    font=("Roboto", 13),
                    text_color=s.COLORS["danger_light"])
            msg.place(x=33, y=190)
            msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes

        elif user_name_recover_entry.get() != "adm":
            user_name_recover_entry.configure(border_color=s.COLORS["danger_light"])
            user_name_recover_entry.after(3000, lambda:user_name_recover_entry.configure(border_color="white"))
            msg = CTkLabel(type_zone_frame,
                    text="Ce nom d'utilisateur n'existe pas",
                    justify="center",
                    font=("Roboto", 13),
                    text_color=s.COLORS["danger_light"])
            msg.place(relx=0.5, y=200, anchor=CENTER)
            msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes
        else:
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
         text="Entrez votre nom d'utilisateur pour \nréinitialiser votre mot de passe",
            text_color=s.COLORS["muted"],
            font=("Roboto", 10),
            justify="center"
            )
    label.place(relx=0.5, y=50, anchor=CENTER)

    user_name_recover_label = CTkLabel(type_zone_frame,
                        text="Nom d'utilisateur",
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
    submit_btn.place(relx=0.5, y=140, anchor=CENTER)

    label_cancel = CTkButton(type_zone_frame,
                        text="Annuler",
                        font=("Roboto", 15),
                      text_color="white",
                        fg_color=s.COLORS["danger"],
                        hover_color=s.COLORS["danger_hover"],
                        corner_radius=5,
                        cursor="hand2",
                        width=190,
                        command=login_form
                        )
    label_cancel.place(relx=0.5, y=170, anchor=CENTER)




# Démarrage
login_form()
# Lance l'application sur le menu principal puis démarre la boucle graphique.
root.mainloop()

