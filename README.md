## exoJellysmack

# Install and launch

Requires Python 3 and flask

Clone the repo, and navigate into it with your terminal.

Run the following commands :

- Windows : 
> set FLASK_APP=rickandmorty
> set FLASK_ENV=development

- Linux (untested, exercise was completed on windows): 
$ export FLASK_APP=rickandmorty
$ export FLASK_ENV=development

Then run 'flask init-db' to initialize the database.
Then run 'flask run', then go on either :

'http://127.0.0.1:5000/list/episodes' to view episode list
'http://127.0.0.1:5000/list/characters' to view character list

# Documentation of the SQL schema

As it is not considered a good practice nor a good idea to have a list of foreign key in a row of a table, I decided to put my data files (episodes and characters) in three tables.
The first two ones, 'episodes' and 'characters' respectively contain all data concerning episodes and characters except for the list of recurring characters or the list of episode.
The third database joinEpisodesCharacters has for each row, an episode_id representing the episode where a character appears, and a character_id, representing the character.
As such, if the episode which id is '1' has that list [2,5,12] in the json file, it will be filled in this table as:
  episode_id  |  character_id
       1      |      2
       1      |      5
       1      |      12
Both ids are foreign key of their respective table.

# How it went

Comme ce paragraphe correspond à mon retour sur l'exercice, je passe en français, avec lequel j'exprimerai plus clairement mon ressenti.

L'exercice a tout d'abord été long, je n'ai pu réaliser que la première partie en entier, et me pencher un peu sur la deuxième feature (notamment la mise en place de la table comment, et le début d'une implémentation du POST des comments).
Je n'avais pas anticipé la longueur du projet, car je n'avais jamais réalisé d'API REST 'from scratch' avant, ni n'avais travaillé sur un code pré-existant d'API REST avant. J'ai dû donc apprendre depuis mes connaissances de Python à réaliser une API REST avec les frameworks disponibles, ce qui m'a pris du temps. J'ai pu travailler environ 25h sur le projet, d'après mes estimations.
L'exercice m'a aussi été complexe, pour la même raison que je n'avais jamais réalisé ce travail avant.
Ainsi, j'avais commencé mon travail avec FastAPI, mais au fur et à mesure que j'avançais dans le tutoriel pour m'aider à réaliser l'exercice, j'ai trouvé le framework trop lourd (notamment au niveau UI) pour le projet, ce qui m'a mené à faire le choix de recommencer le projet avec Flask, que j'ai considéré comme plus léger et donc plus facile à manipuler pour une API de cette taille, au bout de plusieurs heures de travail.

Au fur et à mesure du projet, j'ai réalisé la première feature assez rapidement, mais je n'étais pas satisfait de mon travail, car je ne prennais tout d'abord pas les données depuis la base de données pour les deux GETs, mais depuis les json, ce qui n'était pas la consigne concrètement voulue. Je n'avais aussi pas affiché les listes d'épisodes d'apparition/ de personnages récurrents car je réalisais un simple 'SELECT *' sur les tables 'characters' et 'episodes'. Au vu du temps que j'avais déjà passé sur le sujet, j'ai préféré peaufiner la première feature plutôt que d'essayer de compléter la deuxième.
J'ai donc réussi à réaliser le code manquant pour afficher les listes (de nom des épisodes/personnages au lieu des ids, puisque ceux-ci ne représentent concrètement rien pour l'utilisateur). Une amélioration serait d'avoir chaque élément comme un lien vers l'emplacement correspondant du personnage/épisode dans la page de liste.

J'ai aussi pu me pencher un peu sur la feature des commentaires. J'imaginais ici une route '/list/comments' listant tous les commentaires, avec un bouton 'delete' à chaque commentaire amenant à une route correspondant au DELETE (avec comme input l'id du commentaire à supprimer dans la route) (on peut imaginer que le lien delete aurait automatiquement ramené au GET, montrant ainsi la liste actualisée, sans le commentaire supprimée).
Une autre route aurait permis de créer un commentaire sous la forme d'un formulaire à compléter, avec un bouton 'poster' à la fin; il aurait fallu vérifier les inputs de ce genre de formulaire pour éviter des attaques du type injection SQL.

Enfin, une rapide réflexion sur la feature 3 me fait conclure que les filtres seraient probablement un input à traduire en la bonne requête SQL pour ne sélectionner que les données nécessaires.

Mon code n'a aucun test, par manque de temps, mais il faudrait tester entre autres que les bases de données sont bien remplies à l'initialisation, et que les requêtes vers les tables ne sont pas vides si elles ne doivent pas l'être. Il faudrait implémenter des pratiques comme une page d'erreur plus explicite pour les routes qui n'existent pas, par exemple.

Je suis bien sûr prêt à discuter de ça avec vous si vous en voyez le besoin.
