# 📄 Documentation Technique pour le Projet ICAMIAM

## 🎯 Objectif du Projet
Le projet ICAMIAM est une application web développée avec Django, dont le but est de permettre aux utilisateurs de commander et de réserver des produits à la cafétéria de l'école.

## 🌟 Fonctionnalités Principales
- 🛒 Commander des produits.
- 📅 Réserver des produits.
- 👀 Voir les éléments disponibles.
- 📱 Accessible sur téléphone.

## 🗂 Structure du Projet
Le projet est organisé en plusieurs applications Django comme suit :

### Application "accounts"
- **Objectif :** Gérer l'authentification et les utilisateurs.
- **Fichiers principaux :**
  - `__init__.py` : Initialise l'application.
  - `admin.py` : Enregistre les modèles dans l'interface d'administration de Django.
  - `apps.py` : Configuration de l'application.
  - `models.py` : Définit les modèles de base de données pour les utilisateurs.
  - `tests.py` : Contient les tests pour l'application.
  - `views.py` : Contient les vues de l'application.
  - `migrations/` : Contient les fichiers de migration de base de données.
  - `templates/` : Contient les templates HTML pour les vues.

### Application "icamapps"
- **Objectif :** Gérer les fonctionnalités principales de réservation et de commande.
- **Fichiers principaux :**
  - `__init__.py` : Initialise l'application.
  - `admin.py` : Enregistre les modèles dans l'interface d'administration de Django.
  - `apps.py` : Configuration de l'application.
  - `forms.py` : Définit les formulaires utilisés dans l'application.
  - `models.py` : Définit les modèles de base de données pour les réservations et les commandes.
  - `tests.py` : Contient les tests pour l'application.
  - `views.py` : Contient les vues de l'application.
  - `migrations/` : Contient les fichiers de migration de base de données.
  - `templates/` : Contient les templates HTML pour les vues.

### Application "icamiam" (application principale)
- **Objectif :** Contient les configurations et les fichiers de routage du projet Django.
- **Fichiers principaux :**
  - `__init__.py` : Initialise le projet.
  - `asgi.py` : Fichier de configuration pour le serveur ASGI.
  - `settings.py` : Contient les configurations du projet Django.
  - `urls.py` : Définit les routes URL pour l'application.
  - `wsgi.py` : Fichier de configuration pour le serveur WSGI.

## 🛠️ Instructions pour le Déploiement

### 🐍 Configuration de l'Environnement
- Installez Python (version 3.x).
- Installez Django : `pip install django`.

### 🗃️ Configuration de la Base de Données
- Configurez la base de données dans le fichier `settings.py`.
- Appliquez les migrations : `python manage.py migrate`.

### 🔐 Création de Superutilisateur
- Créez un superutilisateur pour accéder à l'interface d'administration : `python manage.py createsuperuser`.
  
## 🚀 Lancement du projet

Pour lancer le projet, exécutez la commande suivante dans votre terminal :

```
py manage.py runserver 127.0.0.1:80
```
Ensuite, ouvrez votre navigateur et entrez l'une des URL suivantes :

127.0.0.1
icamiam.fr
## 📱 Connexion via téléphone
Pour accéder au site depuis votre téléphone, suivez les étapes ci-dessous :

1. Ouvrez le fichier settings.py.
2. Ajoutez votre adresse IP actuelle à la liste des IP autorisées.
3. Dans le terminal, exécutez la commande :
```
py manage.py runserver "votre_ip":80
```
4. Entrez votre adresse IP dans la barre d'URL de votre navigateur mobile pour accéder au site.

### Configuration de la Base de Données
- Configurez la base de données dans le fichier `settings.py`.
- Appliquez les migrations : `python manage.py migrate`.

### Création de Superutilisateur
- Créez un superutilisateur pour accéder à l'interface d'administration : `python manage.py createsuperuser`.

### Démarrage du Serveur
- Démarrez le serveur de développement : `python manage.py runserver`.
- Accédez à l'application via `http://127.0.0.1:8000/`.

## 🔑 Points Clés des Modèles et Vues

### 🏗️ Modèles (models.py)
- **User (accounts/models.py)**
- Modèle pour gérer les informations des utilisateurs.
- **Product (icamapps/models.py)**
- Modèle pour les produits disponibles à la cafétéria.
- **Reservation (icamapps/models.py)**
- Modèle pour gérer les réservations des utilisateurs.

### 👁️ Vues (views.py)
- **Accounts Views (accounts/views.py)**
- Vues pour l'authentification et la gestion des profils utilisateurs.
- **Reservation Views (icamapps/views.py)**
- Vues pour la création, la gestion et la visualisation des réservations.

## 🖼️ Templates
Les templates HTML se trouvent dans les répertoires `templates` respectifs de chaque application. Ils définissent l'interface utilisateur pour les différentes fonctionnalités du site.

## 🧪 Tests
Les tests sont définis dans les fichiers `tests.py` de chaque application. Ils permettent de vérifier le bon fonctionnement des différentes fonctionnalités de l'application.

## 🏁 Conclusion
Ce document fournit une vue d'ensemble de la structure et de la configuration du projet ICAMIAM. Pour une documentation plus détaillée, veuillez vous référer aux fichiers de code et aux commentaires inclus dans chaque fichier.
