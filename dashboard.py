# Importation des modules 
from customtkinter import *
from CTkMessagebox import *
from PIL import Image

import style as s

# Création de la fenêtre principale
root = CTk()

# Personnalisation de la fenêtre
root.title("Gestionnaire de stock")
root.geometry("1800x900")
root.resizable(0, 0)
root.configure(fg_color=s.COLORS["bg2"])
# image = CTkImage(Image.open("cover.jpg"), size=(930,500))
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
                        )
disconnect.place(x=1600, y=77)

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
                        cursor="hand2"
                        )
add_button.place(x=26, y=320)




# Lance l'application sur le menu principal puis démarre la boucle graphique.
root.mainloop()
