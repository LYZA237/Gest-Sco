class Etudiant:
    def __init__(self, id=None, matricule="", nom="", prenom="", id_niveau=None, id_user=None):
        self.id = id
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.id_niveau = id_niveau
        self.id_user = id_user

    def to_dict(self):
        return {
            "id": self.id,
            "matricule": self.matricule,
            "nom": self.nom,
            "prenom": self.prenom,
            "id_niveau": self.id_niveau
        }