
# Import the random module
import random

# Create the Citation class
class Citation:
    def __init__(self, citation):
        self._citation = citation

    def get_citation(self):
        return self._citation

    def set_citation(self, citation):
        self._citation = citation

# Create the CitationsAleatoires class
class CitationsAleatoires:
    def __init__(self):
        self._citations = []

    def ajouter_citation(self, citation):
        self._citations.append(Citation(citation))

    def afficher_citation_aleatoire(self):
        citation_aleatoire = random.choice(self._citations)
        print(citation_aleatoire.get_citation())

# Create the main function
def main():
    citations = CitationsAleatoires()

    citations.ajouter_citation("Va falloir que tu m'aides à redorer mon blouson")
    citations.ajouter_citation("Eh oh, j'suis pas un leader moi. J'ai jamais vendu de drogue")
    citations.ajouter_citation("Sabri, il y a ta soeur qui a accouché, ça y est t'es papa !")
    citations.ajouter_citation(" Ce week-end je vais lui faire le grand jeu: je vais l’emmener à la Halle aux Chaussures.")
    

    citations.afficher_citation_aleatoire()

# Call the main function
main()
