import json

# Define Person class
class Person:
    # Constructor
    def __init__(self, prenom, age, genre):
        self.prenom = prenom
        self.age = age
        self.genre = genre

    # Set attributes method
    def set_attributs(self, prenom, age, genre):
        self.prenom = prenom
        self.age = age
        self.genre = genre

    # Dictionary method
    def dict(self):
        tableau = {
            "prenom": self.prenom,
            "age": self.age,
            "genre": self.genre
        }
        return tableau

    # JSON method
    def to_json(self):
        return json.dumps(self.dict(), ensure_ascii=False)

# Define Group class
class Group:
    # Constructor
    def __init__(self):
        self.personnes = []

    # Add person method
    def ajouter_personne(self, personne):
        self.personnes.append(personne)

    # Dictionary method
    def dict(self):
        return {"personnes": [personne.dict() for personne in self.personnes]}

    # JSON method
    def to_json(self):
        return json.dumps(self.dict(), ensure_ascii=False)


# Create a group
groupe = Group()

# Add a person to the group
alice = Person("Ramzy", 30, "homme")
groupe.ajouter_personne(alice)

# Add a person to the group
bob = Person("Eric", 28, "Homme")
groupe.ajouter_personne(bob)

# Add a person to the group
carole = Person("Carole", 25, "Femme")
groupe.ajouter_personne(carole)

# Add a person to the group
jamel = Person("Jamel", 30, "Homme")
groupe.ajouter_personne(jamel)
print(groupe.to_json())
