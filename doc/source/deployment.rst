Déploiement
===========

L'application est déployée à l'aide d'un pipeline CI/CD reposant sur GitHub Actions, Docker Hub et Render.

Le pipeline automatise les étapes de validation, de conteneurisation et de mise en production afin de garantir que seules les versions validées de l'application sont déployées.

Architecture de déploiement
---------------------------

Le processus de déploiement implique les services suivants :

- GitHub pour l'hébergement du code source
- GitHub Actions pour l'intégration et le déploiement continus
- Docker Hub pour le stockage des images Docker
- Render pour l'hébergement de l'application

Fonctionnement du pipeline
--------------------------

Lorsqu'une modification est poussée sur n'importe quelle branche autre que ``master`` :

- exécution du linting avec Flake8
- exécution des tests automatisés
- vérification que la couverture de tests reste supérieure à 80 %

Lorsqu'une modification est poussée dans la branche ``master`` :

- exécution du linting
- exécution des tests
- vérification de la couverture
- construction de l'image Docker
- création des tags ``latest`` et ``<commit_sha>``
- publication de l'image sur Docker Hub
- déclenchement du hook de déploiement Render
- déploiement automatique de la nouvelle version

Configuration requise
---------------------

Les éléments suivants doivent être configurés :

- un dépôt GitHub
- GitHub Actions
- un compte Docker Hub
- un dépôt Docker Hub nommé ``oc-p13_oc-lettings``
- un service Web Render utilisant l'image Docker du projet
- un compte Sentry

Configuration de Sentry
-----------------------

L'application utilise Sentry pour la surveillance des erreurs en production.

Pour activer le monitoring :

- Créer un projet dans Sentry.
- Récupérer la valeur DSN fournie par Sentry pour la configuration des variables d'environnement dans Render.

Une fois configuré, les erreurs applicatives seront automatiquement remontées vers Sentry.

Secrets GitHub
--------------

Les secrets suivants doivent être configurés dans le dépôt GitHub :

- ``DOCKERHUB_USERNAME``
- ``DOCKERHUB_TOKEN``
- ``RENDER_DEPLOY_HOOK``

Variables d'environnement
-------------------------

Les variables suivantes doivent être configurées dans Render :

- ``SECRET_KEY``
- ``DEBUG=False``
- ``SENTRY_DSN``

Déploiement initial
-------------------

Pour mettre en place l'infrastructure de déploiement :

- Créer un dépôt Docker Hub
- Créer un service Web sur Render
- Configurer Render pour utiliser l'image Docker du projet
- Configurer les variables d'environnement nécessaires dans Render
- Ajouter les secrets GitHub au dépôt
- Pousser le projet sur GitHub

Déploiement d'une nouvelle version
----------------------------------

- Créer une branche de travail
- Développer et tester les modifications localement
- Pousser la branche sur GitHub
- Ouvrir puis fusionner une Pull Request vers ``master``

Maintenance
-----------

En cas d'échec du pipeline :

- consulter les journaux GitHub Actions
- corriger les erreurs détectées
- effectuer un nouveau commit afin de relancer le pipeline

Les erreurs applicatives en production peuvent être consultées depuis l'interface Sentry.
