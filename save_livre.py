import json
import os

def sauvegarder_livre(livres):
    MA_BIBLIOTHEQUE = os.path.join(os.path.dirname(__file__), "livres.json")
    with open(MA_BIBLIOTHEQUE, "a") as f:
        json.dump(livres, f, indent=4)