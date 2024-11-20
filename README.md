# Catalogue de Musique 

Ce projet a pour but d'offrir aux utilisateurs la possibilité de naviguer dans un catalogue de musique, d'explorer différents artistes et albums. 
## Utilisation

Pour lancer notre projet, voici les démarches à suivre : 

1. Téléchargez le repo en local
2. Dans un terminal, placez-vous à la racine du projet
3. Exécutez la commande suivante :

```bash
docker-compose up --build 

```
Une fois les conteneurs créés dans Docker, ouvrez l'application dans votre navigateur à l'adresse http://localhost:8000. Vous pouvez alors utiliser l'application normalement. Cela peut prendre un peu de temps avant d'être fonctionnel

## Construction du projet

### Packages
Ce projet a été réalisé en utilisant les frameworks FastAPI, SQLAlchemy, et Pydantic. Ces outils nous ont permis de créer un backend robuste et efficace.
### Arborescence du projet
L'arborescence de ce projet se base sur la séparation de toutes les parties de notre application dans des dossiers distincts. Ainsi, notre fichier main.py appelle simplement les routes permettant de naviguer à travers notre application.

### Fonctionnalités réalisées
Diverses fonctionnalités ont été réalisées dans le cadre du développement de ce projet :

1. L'authentification des utilisateurs : Elle se fait via la génération de tokens JWT, du hachage des mots de passe, et de l'insertion dans notre base de données PostgreSQL.
2. La gestion du catalogue de musique : Permet de naviguer à travers les artistes,les albums et les ventes stockés dans la base de données et de supprimer des albums du catalogue.
3. La recherche avancée : Permet aux utilisateurs de rechercher des albums par id.
4. L'intégration de Docker : Permet une portabilité de notre application et facilite son déploiement.


## Navigation sur le site

### Page d'accueil (non connecté)

Dans la page d'accueil, vous avez deux options :
1. "login" si vous avez déjà un compte 
2. Cliquer sur "register" pour vous inscrire

### Page d'accueil (connecté)
Une fois connecté, vous avez accès au catalogue 

## Difficultés rencontrées
Au cours du développement de ce projet, nous avons rencontré plusieurs défis :
1. La gestion des relations complexes dans la base de données.
2. L'implémentation d'un système de recherche efficace capable de gérer de grandes quantités de données.
3. La mise en place d'un système d'authentification sécurisé avec gestion des tokens JWT.


Ce projet nous a permis d'approfondir nos connaissances en développement backend avec FastAPI et de mettre en pratique des concepts avancés de gestion de bases de données et d'authentification.

Créé par Yannis TUMELIN et Zakary BELKACEM
