# POO : Programmation Orientée Objet
"""
    Les types de données
    Classe:                 Personne
    Instance / Objet        Jules, Alice, Paul
    Methodes                Parler, Courir, Manger (les fonctions)
    Attributs               Nom, Age, Sexe (les variables)
    Constructeur            __init__

    Classe              ==  Types primitifs
    Instance / Objet    ==  Variable
    Attributs           ==  Variable de l'objet
"""

class Personne:
    # nom = ""
    # prenom = ""
    # sexe = True
    # est_vivant = True

    # Le constructeur de la classe Personne
    def __init__(self, c_nom, c_prenom, c_sexe):
        self.nom = c_nom
        self.prenom = c_prenom
        self.sexe = c_sexe
        self.est_vivant = True

    def __str__(self):
        return f"Nom: {self.nom} Prenom: {self.prenom} Sexe: {self.sexe}"   # type:ignore
    
    def  se_presenter(self):
        return f"Je m'appelle {self.nom} {self.prenom} et je suis un{(" homme" if self.sexe else "e femme")}"   #type:ignore

jules = Personne("MILEGNE", "Jules", True)
didier = Personne(c_sexe = True, c_nom = "AKAKPO", c_prenom = "Didier")
tom = Personne("TOM", "Tom", False)

print(jules.se_presenter())
print(didier.se_presenter())
print(tom.se_presenter())

print(jules.nom, jules.prenom)