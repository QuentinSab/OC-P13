Technologies
============

Le projet OC Lettings Site est une application web développée en Python à l'aide du framework Django.

Plusieurs outils complémentaires sont utilisés afin de faciliter le développement, les tests, la conteneurisation, l'intégration continue et le déploiement de l'application.

Langages de programmation
-------------------------

* Python
* HTML
* CSS

Frameworks et bibliothèques
---------------------------

Django
^^^^^^

Le framework Django constitue le cœur de l'application. Il fournit notamment :

- le système de routage ;
- l'ORM ;
- le moteur de templates ;
- l'interface d'administration.

Gunicorn
^^^^^^^^

Gunicorn est utilisé comme serveur WSGI pour exécuter l'application en production.

WhiteNoise
^^^^^^^^^^

WhiteNoise permet de servir les fichiers statiques directement depuis l'application Django.

Sentry SDK
^^^^^^^^^^

Sentry est utilisé pour la surveillance de l'application et le suivi des erreurs en production.

Base de données
---------------

SQLite est utilisée comme base de données relationnelle du projet.

Conteneurisation
----------------

Docker
^^^^^^

Docker permet de construire une image contenant l'ensemble de l'application et de ses dépendances.

Docker Compose
^^^^^^^^^^^^^^

Docker Compose simplifie l'exécution locale de l'application grâce à une configuration centralisée des services et des variables d'environnement.

Intégration et déploiement continus
-----------------------------------

GitHub
^^^^^^

GitHub est utilisé pour l'hébergement du code source et la gestion des versions.

GitHub Actions
^^^^^^^^^^^^^^

GitHub Actions exécute automatiquement le pipeline CI/CD du projet :

- vérification du style de code ;
- exécution des tests ;
- contrôle de la couverture de tests ;
- construction et publication des images Docker ;
- déclenchement du déploiement.

Docker Hub
^^^^^^^^^^

Docker Hub est utilisé comme registre de conteneurs pour stocker les images Docker générées par le pipeline.

Render
^^^^^^

Render est utilisé pour l'hébergement et le déploiement de l'application en production.

Qualité logicielle
------------------

Pytest
^^^^^^

Pytest est utilisé pour l'exécution de la suite de tests automatisés.

Pytest-Cov et Coverage
^^^^^^^^^^^^^^^^^^^^^^

Ces outils permettent de mesurer la couverture des tests et de vérifier qu'elle reste supérieure à 80 %.

Flake8
^^^^^^

Flake8 est utilisé pour l'analyse statique du code et la vérification du respect des conventions de style Python.

Documentation
-------------

Sphinx
^^^^^^

Sphinx est utilisé pour générer la documentation technique du projet.

Read the Docs
^^^^^^^^^^^^^

Read the Docs héberge et publie automatiquement la documentation générée par Sphinx.
