Installation
============

Cette section décrit les étapes nécessaires pour installer le projet OC Lettings Site dans un environnement de développement local.

Prérequis
^^^^^^^^^

Les éléments suivants doivent être installés sur la machine :

- Git
- Python 3.11.9 ou supérieur
- Pip 24 ou supérieur

Récupération du projet
^^^^^^^^^^^^^^^^^^^^^^

Cloner le dépôt Git :

- ``git clone https://github.com/QuentinSab/OC-P13``
- ``cd OC-P13``

Création de l'environnement virtuel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Créer un environnement virtuel Python :

``python -m venv venv``

Activer l'environnement virtuel :

Sous Linux ou macOS :

``source venv/bin/activate``

Sous Windows (PowerShell) :

``.\venv\Scripts\Activate.ps1``

Installation des dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installer les dépendances du projet :

``pip install -r requirements.txt``

Collecte des fichiers statiques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avant d'exécuter les tests ou de lancer l'application, les fichiers statiques doivent être collectés :

``python manage.py collectstatic --noinput``

Une fois ces étapes terminées, l'application peut être démarrée en suivant le guide de démarrage rapide.