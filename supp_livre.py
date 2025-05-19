def supprimer_livre(livres):
     id_supp = int(input("Entrez l'ID du livre à supprimer: "))
     for livre in livres:
          if livre["ID"] == id_supp:
               confirmation = input(f"Confirmer la suppression de '{livre['Titre']}' ? (o/n): ")
               if confirmation.lower() == 'o':
                    livres.remove(livre)
                    print("Livre supprimé.")
               return
     print("Livre non trouvé.")