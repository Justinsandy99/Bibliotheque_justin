def ajout_de_livre(livres):
    titre = input("Titre du livre: ")
    auteur = input("Auteur: ")
    annee = int(input("Année de publication: "))
    nouvel_id = max([livre["ID"] for livre in livres], default=0) + 1
    livre = {
        "ID": nouvel_id,
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,
        "Note": None,
        "Commentaire": ""
    }
    livres.append(livre)
    print("Livre ajouté avec succès !")