Base de données
===============

L'application utilise l'ORM Django pour gérer les données persistées en base de données.

La structure de données est répartie entre deux applications :

lettings : gestion des annonces de location et des adresses ;
profiles : gestion des profils utilisateurs.

Modèles de l'application Lettings
---------------------------------

Address
^^^^^^^

Le modèle ``Address`` représente l'adresse complète d'un bien immobilier.

+------------------+----------------------+------------------------+
| Champ            | Type                 | Description            |
+==================+======================+========================+
| number           | PositiveIntegerField | Numéro de rue          |
+------------------+----------------------+------------------------+
| street           | CharField(64)        | Nom de la rue          |
+------------------+----------------------+------------------------+
| city             | CharField(64)        | Ville                  |
+------------------+----------------------+------------------------+
| state            | CharField(2)         | État ou région         |
+------------------+----------------------+------------------------+
| zip_code         | PositiveIntegerField | Code postal            |
+------------------+----------------------+------------------------+
| country_iso_code | CharField(3)         | Code ISO du pays       |
+------------------+----------------------+------------------------+

Contraintes :

- ``number`` est limité à 9999 ;
- ``zip_code`` est limité à 99999 ;
- ``state`` doit contenir exactement 2 caractères ;
- ``country_iso_code`` doit contenir exactement 3 caractères.

Relations :

- une adresse peut être associée à une unique annonce de location ;
- la suppression d'une annonce entraîne la suppression de l'adresse associée (``CASCADE``).

Letting
^^^^^^^

Le modèle Letting représente une annonce de location.

+---------+----------------+------------------------------+
| Champ   | Type           | Description                  |
+=========+================+==============================+
| title   | CharField(256) | Titre de l'annonce           |
+---------+----------------+------------------------------+
| address | OneToOneField  | Adresse associée à l'annonce |
+---------+----------------+------------------------------+

Contraintes :

- une annonce doit obligatoirement être associée à une adresse.

Relations :

- une annonce possède une adresse unique ;
- une adresse est associée à une seule annonce.

Modèles de l'application Profiles
---------------------------------

Profile
^^^^^^^

Le modèle ``Profile`` stocke des informations complémentaires liées à un utilisateur Django.

+---------------+---------------+---------------------------------+
| Champ         | Type          | Description                     |
+===============+===============+=================================+
| user          | OneToOneField | Utilisateur Django associé      |
+---------------+---------------+---------------------------------+
| favorite_city | CharField(64) | Ville favorite de l'utilisateur |
+---------------+---------------+---------------------------------+

Contraintes :

- ``favorite_city`` peut être vide (``blank=True``).

Relations :

- chaque profil est associé à un utilisateur Django unique ;
- chaque utilisateur possède un seul profil ;
- la suppression d'un utilisateur entraîne la suppression du profil associé (``CASCADE``).