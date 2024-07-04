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

### Dossier "media"
- **Objectif :** Contient les fichiers médias téléchargés par les utilisateurs.

### Dossier "static"
- **Objectif :** Contient les fichiers statiques utilisés dans le projet (CSS, JavaScript, images).
- **Sous-dossiers :**
  - `admin/` : Contient les fichiers statiques spécifiques à l'administration Django.
  - `css/` : Contient les fichiers CSS pour le style de l'application.
  - `img/` : Contient les images utilisées dans l'application.
  - `js/` : Contient les fichiers JavaScript pour l'interactivité de l'application.

## 🖼️ Templates
Les templates HTML se trouvent dans les répertoires `templates` respectifs de chaque application. Ils définissent l'interface utilisateur pour les différentes fonctionnalités du site.

## 🛠️ Instructions pour le Déploiement

### 🐍 Configuration de l'Environnement
- Installez Python (version 3.x).
- Installez Django : `pip install django`.

### 🗃️ Configuration de la Base de Données
- Configurez la base de données dans le fichier `settings.py`.
- Appliquez les migrations : `python manage.py migrate`.

### 🔐 Création de Superutilisateur et gérer les comptes sur l'interface administrateur
- Créez un superutilisateur pour accéder à l'interface d'administration : `python manage.py createsuperuser`.
- Pour créer une classe avec des accès sur Django il faut créer utilisateur puis dans django admin lui attribuer des accès. 
  
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

## 🔑 Points Clés des Modèles et Vues

### 🏗️ Modèles (models.py)
- **Product (icamapps/models.py)** : Modèle pour les produits disponibles à la cafétéria.
- **Event (icamapps/models.py)** : Modèle pour les événements organisés par la cafétéria.
- **MenuItem (icamapps/models.py)** : Modèle pour les éléments du menu de la cafétéria.
- **Contact (icamapps/models.py)** : Modèle pour les informations de contact de la cafétéria.
- **Order (icamapps/models.py)** : Modèle pour les commandes passées par les utilisateurs.
- **Panier (icamapps/models.py)** : Modèle pour gérer le panier des utilisateurs.
- **Confirmation (icamapps/models.py)** : Modèle pour gérer les confirmations de commande.

### 👁️ Vues (views.py)
- **signup (accounts/views.py)** : Vue pour la page d'inscription des utilisateurs, permettant de créer un nouveau compte utilisateur.
- **logout_user (accounts/views.py)** : Vue pour déconnecter l'utilisateur actuel.
- **login_user (accounts/views.py)** : Vue pour la page de connexion des utilisateurs, permettant de s'authentifier et de se connecter.
- **home (icamapps/views.py)** : Vue pour la page d'accueil affichant les événements, les éléments du menu et les informations de contact.
- **menu (icamapps/views.py)** : Vue pour la page du menu affichant tous les produits disponibles.
- **event (icamapps/views.py)** : Vue pour la page des événements affichant tous les événements.
- **panier (icamapps/views.py)** : Vue pour la page du panier permettant de gérer les articles ajoutés par l'utilisateur.
- **index (icamapps/views.py)** : Vue pour la page d'index.
- **add_to_cart (icamapps/views.py)** : Vue pour ajouter un produit au panier de l'utilisateur.
- **remove_from_cart (icamapps/views.py)** : Vue pour supprimer un article du panier de l'utilisateur.
- **confirmation (icamapps/views.py)** : Vue pour confirmer une commande d'un produit spécifique.
  
# ⚙️ Administration (admin.py)

Le fichier `admin.py` configure l'interface d'administration de Django pour gérer les modèles de l'application `icamapps`. Cela permet aux administrateurs de visualiser, ajouter, modifier et supprimer des enregistrements de modèles directement depuis l'interface d'administration.

## Modèles enregistrés

- **Product**
  - Enregistrement du modèle `Product` dans l'administration Django. Les administrateurs peuvent gérer les produits disponibles à la cafétéria.

- **Event**
  - Enregistrement du modèle `Event` dans l'administration Django. Les administrateurs peuvent gérer les événements organisés par la cafétéria.

- **Panier**
  - Enregistrement du modèle `Panier` dans l'administration Django. Les administrateurs peuvent gérer les paniers des utilisateurs.

## Configuration personnalisée de l'administration pour le modèle `Order`

L'administration du modèle `Order` est personnalisée à l'aide de la classe `OrderAdmin`. Cette personnalisation permet de contrôler l'affichage et les fonctionnalités de gestion des commandes dans l'interface d'administration.

- **OrderAdmin**
  - **list_display** : Affiche les champs `order_number`, `user`, `product`, `quantity`, et `ordered` dans la liste des commandes.
  - **search_fields** : Permet de rechercher des commandes en utilisant `order_number`, `user__username`, et `product__name`.
  - **list_filter** : Ajoute des filtres pour les champs `ordered` et `product`, facilitant la recherche de commandes spécifiques.
  - **ordering** : Définit l'ordre de tri par défaut des commandes, avec les commandes les plus récentes en premier (`-ordered`).

# 📝 Formulaires (`forms.py`)

Le fichier `forms.py` contient les définitions des formulaires utilisés pour la saisie et la validation des données dans l'application `icamapps`.

## Formulaires disponibles

### `CreateNewlist`

Le formulaire `CreateNewlist` est utilisé pour collecter des informations lorsqu'un nouvel utilisateur souhaite s'inscrire à un service spécifique de l'application.

- **Champs :**
  - `Prenom` : Champ de texte pour le prénom de l'utilisateur.
  - `Nom` : Champ de texte pour le nom de l'utilisateur.
  - `Email` : Champ de texte pour l'adresse email de l'utilisateur, avec validation automatique de format.

#### Utilisation typique :

Ce formulaire est utilisé lors du processus d'inscription ou de création de compte utilisateur dans l'application. Il garantit que les informations essentielles comme le prénom, le nom et l'email sont saisies correctement.

## 🧪 Tests
Les tests sont définis dans les fichiers `tests.py` de chaque application. Ils permettent de vérifier le bon fonctionnement des différentes fonctionnalités de l'application.

## 🏁 Finalité
Le document fournit une vue d'ensemble de la structure et de la configuration du projet ICAMIAM. Pour une documentation plus détaillée, veuillez vous référer aux fichiers de code et aux commentaires inclus dans chaque fichier.








