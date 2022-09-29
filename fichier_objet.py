###################################### recherche dans une class object via fonction honor
class etudiant:
    def __init__(self, nom, prenom, domaine, score):
        self.nom = nom
        self.prenom = prenom
        self.domaine = domaine
        self.score = score

    def honneur(self):
        if self.score >= 16:
            return True
        else:
            return False

