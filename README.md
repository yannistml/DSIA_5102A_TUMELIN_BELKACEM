# Catalogue de Musique 

Ce projet a pour but d'offrir aux utilisateurs la possibilité de naviguer dans un catalogue de musique, d'explorer différents artistes, albums et chansons. 
## Utilisation

Pour lancer notre projet, voici les démarches à suivre : 

1. Téléchargez le repo en local
2. Dans un terminal, placez-vous à la racine du projet
3. Exécutez les commandes suivantes :

```bash
docker compose build
docker compose up
```
Une fois les conteneurs créés dans Docker, ouvrez l'application dans votre navigateur à l'adresse http://localhost:8000. Vous pouvez alors utiliser l'application normalement.

## Construction du projet

### Packages
Ce projet a été réalisé en utilisant les frameworks FastAPI, SQLAlchemy, et Pydantic. Ces outils nous ont permis de créer un backend robuste et efficace.
### Arborescence du projet
L'arborescence de ce projet se base sur la séparation de toutes les parties de notre application dans des dossiers distincts. Ainsi, notre fichier main.py appelle simplement les routes permettant de naviguer à travers notre application.

### Fonctionnalités réalisées
Diverses fonctionnalités ont été réalisées dans le cadre du développement de ce projet :

1. L'authentification des utilisateurs : Elle se fait via la génération de tokens JWT, du hachage des mots de passe, et de l'insertion dans notre base de données PostgreSQL.
2. La gestion du catalogue de musique : Permet de naviguer à travers les artistes, ventes et chansons stockés dans la base de données.
3. La recherche avancée : Permet aux utilisateurs de rechercher des chansons, albums ou artistes selon divers critères.
4. L'intégration de Docker : Permet une portabilité de notre application et facilite son déploiement.


## Navigation sur le site

### Page d'accueil (non connecté)

Dans la page d'accueil, vous avez deux options :
1. Vous connecter si vous avez déjà un compte
2. Cliquer sur "Créer un compte" pour vous inscrire

### Page d'accueil (connecté)
Une fois connecté, vous avez accès au
catalogue pour explorer les artistes, ventes et chansons

## Difficultés rencontrées
Au cours du développement de ce projet, nous avons rencontré plusieurs défis :
1. La gestion des relations complexes dans la base de données entre les artistes, albums, chansons et playlists.
2. L'implémentation d'un système de recherche efficace capable de gérer de grandes quantités de données.
3. La mise en place d'un système d'authentification sécurisé avec gestion des tokens JWT.
4. L'optimisation des performances pour gérer un grand nombre de requêtes simultanées.

Malgré ces difficultés, nous avons réussi à les surmonter en utilisant des techniques d'optimisation de base de données, en implémentant un système de cache, et en structurant notre code de manière modulaire et efficace.
Ce projet nous a permis d'approfondir nos connaissances en développement backend avec FastAPI et de mettre en pratique des concepts avancés de gestion de bases de données et d'authentification.

Créé par Yannis TUMELIN et Zakary BELKACEM
