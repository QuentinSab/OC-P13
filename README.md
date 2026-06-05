## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau profils `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table profils `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Vue d'ensemble

L'application est déployée à l'aide d'un pipeline CI/CD reposant sur GitHub Actions, Docker Hub et Render.

Lorsqu'un code est poussé sur n'importe quelle branche, GitHub Actions exécute les vérifications de qualité du code :

- linting avec Flake8 ;
- exécution des tests ;
- vérification que la couverture de tests reste supérieure à 80 %.

Lorsqu'une modification est appliquée dans la branche master :

- GitHub Actions exécute le linting, les tests et la vérification de la couverture.
- Une image Docker est construite à partir du Dockerfile du projet.
- L'image est taguée avec le hash du commit ainsi qu'avec le tag latest.
- L'image est publiée sur Docker Hub.
- Un hook est déclenché et Render récupère la dernière image Docker puis déploie automatiquement l'application.

#### Configuration requise

Les services suivants doivent être configurés :

- un dépôt GitHub ;
- GitHub Actions ;
- un compte Docker Hub et un dépôt Docker Hub ;
- un service Web Render configuré pour utiliser l'image Docker du projet.

#### Secrets GitHub

Les secrets suivants doivent être configurés dans le dépôt GitHub :

    DOCKERHUB_USERNAME
    DOCKERHUB_TOKEN
    RENDER_DEPLOY_HOOK

#### Variables d'environnement

Les variables d'environnement suivantes doivent être configurées sur Render :

    SECRET_KEY
    DEBUG=False
    SENTRY_DSN

### Procédure de déploiement

#### Déploiement initial

- Créer un dépôt Docker Hub.
- Créer un service Web sur Render utilisant l'image Docker hébergée sur Docker Hub.
- Configurer les variables d'environnement nécessaires sur Render.
- Ajouter les secrets GitHub requis.
- Pousser le projet sur GitHub.

Une fois le pipeline configuré, aucune intervention manuelle n'est nécessaire pour déployer une nouvelle version de l'application.