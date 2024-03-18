Projet Simplon Data Platform
Description

Ce projet, développé dans le cadre d'un programme de formation à Simplon, vise à créer une plateforme dynamique basée sur les données de la SBA (Small Business Administration). Il intègre une pile technologique moderne comprenant Django, FastAPI, Tailwind CSS, et Docker pour offrir une expérience utilisateur fluide et responsive. Le backend est construit avec Django et FastAPI pour une gestion efficace des données et des requêtes API, tandis que le frontend utilise Tailwind CSS pour un design épuré et moderne. Docker est employé pour faciliter le déploiement et l'isolation des environnements de développement et de production.
Démarrage rapide

Pour lancer le projet, assurez-vous d'avoir Docker installé sur votre machine. Clonez ensuite le dépôt du projet et naviguez dans le répertoire du projet. Utilisez le script start.sh pour démarrer l'ensemble de l'application en utilisant Docker Compose. Le script accepte un argument optionnel pour spécifier une configuration Docker Compose alternative.

bash

./start.sh [environment]

Si aucun argument n'est fourni, le script utilisera compose.yml par défaut. Pour des environnements spécifiques (par exemple, développement ou production), vous pouvez passer le nom de l'environnement comme argument (ex : ./start.sh dev pour utiliser compose.dev.yml).
Architecture

Le projet est structuré autour de trois services principaux définis dans le fichier docker-compose :

    Web : Le service web, construit sur Django et servant l'interface utilisateur conçue avec Tailwind CSS. Il est accessible sur le port 80.
    API : Un service API FastAPI pour la gestion des requêtes liées aux données. Accessible sur le port 8000.
    Postgres_db : Une base de données PostgreSQL servant de système de gestion de base de données pour le projet.

Docker Compose

Le fichier docker-compose version 3.8 définit la configuration des services, leurs dépendances, les ports exposés, les fichiers d'environnement, et les volumes pour la persistance des données.
Configuration

Le projet utilise des fichiers d'environnement (.env) situés dans le répertoire web/ pour gérer les variables d'environnement du service web et de la base de données.
Volumes

    postgres_data : Un volume Docker est utilisé pour persister les données de la base de données PostgreSQL au-delà de la durée de vie des conteneurs.

Contribution

Nous encourageons les contributions! Veuillez suivre les meilleures pratiques de développement et de collaboration. Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue ou un pull request.
Licence

Ce projet est distribué sous une licence qui sera définie par l'équipe de projet ou les directives de l'école Simplon.
