Démarrage rapide
================

Cette section décrit les étapes minimales nécessaires pour lancer l'application localement après son installation.

Activation de l'environnement virtuel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sous Linux ou macOS :

``source venv/bin/activate``

Sous Windows (PowerShell) :

``.\venv\Scripts\Activate.ps1``

Lancement de l'application
^^^^^^^^^^^^^^^^^^^^^^^^^^

Démarrer le serveur de développement Django :

``python manage.py runserver``

Par défaut, l'application est accessible à l'adresse :

``http://127.0.0.1:8000``

Vérification du fonctionnement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Après le démarrage du serveur :

- accéder à la page d'accueil
- vérifier que la page des annonces est accessible via `/lettings/`
- vérifier que la page des profils est accessible via `/profiles/`

Arrêt du serveur
^^^^^^^^^^^^^^^^

Pour arrêter le serveur de développement, utiliser le raccourci clavier :

*Ctrl + C*
