# Classe de base
class Composant:
    def operation(self):
        print("Fonctionnalité de base du composant")

# Classe décorateur
class Decorateur(Composant):
    def __init__(self, composant):
        self.composant = composant

    def operation(self):
        self.composant.operation()
        self.fonctionnalite_supplementaire()

    def fonctionnalite_supplementaire(self):
        print("Fonctionnalité supplémentaire ajoutée")

# Utilisation du décorateur
composant_base = Composant()
composant_decorateur = Decorateur(composant_base)
composant_decorateur.operation()
