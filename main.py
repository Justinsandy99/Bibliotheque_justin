import listes_import

livres = []
def menu():

    choix = input('Entrez votre choix de numéro(1 à 9): ')
    if choix not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        choix = input('Entrez votre choix de numéro (1 à 9): ')
    match choix:
        case '1':
            listes_import.afficher_all_livres(livres)
            menu()
        case '2':
            listes_import.ajout_de_livre(livres)
            menu()
        case '3':
            listes_import.supprimer_livre(livres)
            menu()
        case '4':
            listes_import.rechercher_livre()
        case '5':
            listes_import.marquer_un_livre()
        case '6':
            listes_import.afficher_listes_livres_lus_et_non_lus()
        case '7':
            listes_import.tries_livres()
        case '8':
            listes_import.sauvegarder_livre(livres)
        case '9':
            listes_import.charger_les_livres()
        case _: 
            menu()
            
print(""" 
    1- Afficher tous les livres.
    2- Ajouter un livre.
    3- Supprimer un livre.
    4- Rechercher un livre.
    5- Marquer un livre comme lu.
    6- Afficher les livres lus ou non lus.
    7- Trier les livres.
    8- Sauvegarder la bibliothèque.
    9- Charger la bibliothèque au démarrage.
""")    

menu()