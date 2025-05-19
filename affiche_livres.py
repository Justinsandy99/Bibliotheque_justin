def afficher_all_livres(livres):
    if not livres:
        print("Aucun livre dans la bibliothèque.")
    for livre in livres:
        statut = "Lu" if livre["Lu"] else "Non lu"
        print(f"ID: {livre['ID']}, Titre: {livre['Titre']}, Auteur: {livre['Auteur']}, Année: {livre['Année']}, Statut: {statut}, Note: {livre.get('Note', 'None')}, Commentaire: {livre.get('Commentaire', '')}")
