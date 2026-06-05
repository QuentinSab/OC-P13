Interface de programmation
==========================

Les requêtes HTTP sont traitées par des vues Django qui génèrent des pages HTML à partir de templates.

Routes disponibles
------------------

Application principale
^^^^^^^^^^^^^^^^^^^^^^

- ``/`` : déclenche la vue ``oc_lettings_site.views.index`` et affiche la page d'accueil.
- ``/admin/`` : donne accès à l'interface d'administration Django.

Application lettings
^^^^^^^^^^^^^^^^^^^^

- ``/lettings/`` : déclenche la vue ``lettings.views.index`` et affiche la liste des annonces de location.
- ``/lettings/<letting_id>/`` : déclenche la vue ``lettings.views.letting`` et affiche les détails d'une annonce à partir de son identifiant.

Application profiles
^^^^^^^^^^^^^^^^^^^^

- ``/profiles/`` : déclenche la vue ``profiles.views.index`` et affiche la liste des profils utilisateurs.
- ``/profiles/<username>/`` : déclenche la vue ``profiles.views.profile`` et affiche les informations associées à un utilisateur.

Gestion des erreurs
-------------------

L'application utilise des vues personnalisées pour la gestion des erreurs :

- ``oc_lettings_site.views.error_404`` : affichée lorsqu'une ressource demandée n'existe pas.
- ``oc_lettings_site.views.error_500`` : affichée lorsqu'une erreur interne du serveur se produit.