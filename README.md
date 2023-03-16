Pour lancer le projet, il faut installer plusieurs librairies python.
Pour cela, il faut ouvrir un terminal et taper la commande suivante:
pip install -r requirements.txt

Partie_1 : Citations aléatoires
==============================
Ce script Python permet de stocker des citations et d'en afficher une de manière aléatoire.

Comment utiliser:
-----------------
Téléchargez le fichier citations_aleatoires.py.
Ouvrez un terminal et placez-vous dans le dossier contenant le fichier téléchargé.
Exécutez la commande `python citations_aleatoires.py`.
Une citation aléatoire sera affichée dans le terminal.
Comment ajouter des citations
Pour ajouter des citations, modifiez la fonction main() en utilisant la méthode ajouter_citation() de la classe CitationsAleatoires.

Par exemple :

def main():
    citations = CitationsAleatoires()

    citations.ajouter_citation("La vie, c'est comme une boîte de chocolats, on ne sait jamais sur quoi on va tomber.")
    citations.ajouter_citation("May the Force be with you.")
    citations.ajouter_citation("Je suis ton père.")
    citations.ajouter_citation("Hasta la vista, baby.")


Partie_2 : Retourner personne en json 
====================================
Ce script Python permet de gérer un groupe de personnes. Chaque personne est représentée par un objet de la classe Personne, qui contient des informations sur le prénom, l'âge et le genre de la personne. Les objets Personne sont stockés dans un objet de la classe Groupe.

Le script permet également de convertir les données du groupe en format JSON à l'aide des méthodes dict() et to_json() de chaque classe.

Comment utiliser
----------------
Téléchargez le fichier `groupe_personnes.py`.
Ouvrez un terminal et placez-vous dans le dossier contenant le fichier téléchargé.
Exécutez la commande `python groupe_personnes.py`.
Le script créera un groupe de personnes avec des données prédéfinies et affichera la version JSON de ces données dans le terminal.
Comment ajouter des personnes
Pour ajouter des personnes, créez un nouvel objet Personne et ajoutez-le au groupe en utilisant la méthode ajouter_personne() de la classe Groupe.

Par exemple :

groupe = Groupe()

alice = Personne("Alice", 30, "Femme")
groupe.ajouter_personne(alice)

bob = Personne("Bob", 28, "Homme")
groupe.ajouter_personne(bob)

carole = Personne("Carole", 25, "Femme")
groupe.ajouter_personne(carole)

Partie_3 : récupérer les informations systèmes
==============================================
Ce script Python permet de récupérer des informations sur le système d'exploitation et le processeur.
Il utilise la librairie Flask pour créer une application web.

Comment utiliser
----------------
Téléchargez le fichier `app.py`.
Ouvrez un terminal et placez-vous dans le dossier contenant le fichier téléchargé.

Exécutez la commande `python app.py`.

Une fenetre web s'ouvre et affiche les informations sur le système d'exploitation et le processeur.
