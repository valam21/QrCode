# AI4CKD - Système Intelligent de Gestion des Patients atteints de MRC

![Banner AI4CKD](https://via.placeholder.com/1200x300?text=AI4CKD+Solution+for+CKD+Patients)

## Table des Matières

1.  [Introduction](#1-introduction)
2.  [Fonctionnalités Clés](#2-fonctionnalités-clés)
    * [Système d'Alertes Intelligentes (Alerting dynamique)](#système-dalertes-intelligentes-alerting-dynamique)
    * [Module de Génération de Synthèse PDF](#module-de-génération-de-synthèse-pdf)
    * [Authentification Utilisateur](#authentification-utilisateur)
3.  [Technologies Utilisées](#3-technologies-utilisées)
4.  [Architecture du Projet](#4-architecture-du-projet)
5.  [Pré-requis](#5-pré-requis)
6.  [Installation et Démarrage](#6-installation-et-démarrage)
    * [Cloner le Dépôt](#cloner-le-dépôt)
    * [Configuration de la Base de Données (PostgreSQL)](#configuration-de-la-base-de-données-postgresql)
    * [Configuration du Backend](#configuration-du-backend)
    * [Configuration du Frontend](#configuration-du-frontend)
    * [Lancer l'Application](#lancer-lapplication)
7.  [Utilisation de l'Application](#7-utilisation-de-lapplication)
8.  [Déploiement](#8-déploiement)
9.  [Structure du Dépôt](#9-structure-du-dépôt)
10. [Livrables (Hackathon)](#10-livrables-hackathon)
11. [Défis et Apprentissages](#11-défis-et-apprentissages)
12. [Contribution](#12-contribution)
13. [Auteurs](#13-auteurs)
14. [Licence](#14-licence)

---

## 1. Introduction

Ce projet a été développé dans le cadre du hackathon "AI4CKD". L'objectif est de créer un prototype d'application web pour la gestion des patients atteints de Maladie Rénale Chronique (MRC). Le prototype se concentre sur deux modules critiques : un **système intelligent de détection et d'alerte automatique** des situations cliniques critiques et un **module de génération de synthèse PDF** des données patients. Une fonctionnalité d'**authentification utilisateur** a également été intégrée pour sécuriser l'accès aux données patient.

## 2. Fonctionnalités Clés

### Système d'Alertes Intelligentes (Alerting dynamique)

Cette fonctionnalité permet la détection automatique de situations à risque à partir des données cliniques saisies par les professionnels de santé lors des consultations.

* **Déclenchement des alertes** : Les alertes sont déclenchées en fonction de seuils et de règles prédéfinies basées sur les paramètres cliniques (ex: créatinine, tension artérielle, poids).
    * **Alertes MRC** : Seuil de créatinine élevé, tension artérielle anormale, etc.
    * **Alertes Dynamiques** : Détection de l'aggravation rapide de la fonction rénale (ex: augmentation significative de la créatinine entre deux consultations successives).
* **Notifications** : Les alertes sont affichées de manière claire et visuelle sur la page de détail du patient, permettant une intervention rapide.

### Module de Génération de Synthèse PDF

Ce module permet de générer un rapport PDF complet du dossier patient, incluant toutes les informations démographiques, les antécédents, l'historique des consultations et les alertes.

* **Exportation Facile** : Un bouton dédié sur la page de détail du patient permet de télécharger instantanément le PDF.
* **Contenu Complet** : Le PDF contient de manière structurée l'ensemble des données pertinentes du patient, facilitant le partage et l'archivage.

### Authentification Utilisateur

Pour sécuriser l'accès aux données sensibles des patients, un système d'authentification a été mis en place.

* **Inscription (Register)** : Les nouveaux utilisateurs peuvent créer un compte avec leur email et un mot de passe.
* **Connexion (Login)** : Les utilisateurs enregistrés peuvent se connecter pour accéder aux fonctionnalités de l'application.
* **Protection des Routes** : L'accès aux pages de gestion des patients (liste, détails, ajout) et aux API backend est restreint aux utilisateurs authentifiés via des JSON Web Tokens (JWT).
* **Déconnexion (Logout)** : Permet aux utilisateurs de se déconnecter de leur session.

## 3. Technologies Utilisées

Ce projet est une application web full-stack, utilisant les technologies suivantes :

* **Frontend**:
    * [Next.js](https://nextjs.org/) (Framework React pour le rendu côté serveur et client)
    * [React](https://react.dev/) (Bibliothèque JavaScript pour les interfaces utilisateur)
    * [TypeScript](https://www.typescriptlang.org/) (Superset de JavaScript typé)
    * [Tailwind CSS](https://tailwindcss.com/) (Framework CSS utilitaire pour un style rapide et réactif)
    * [`date-fns`](https://date-fns.org/) (Utilitaires pour la manipulation des dates)
    * `localStorage` (pour la gestion des tokens JWT côté client)
* **Backend**:
    * [Node.js](https://nodejs.org/) (Environnement d'exécution JavaScript côté serveur)
    * [Express.js](https://expressjs.com/) (Framework web pour Node.js)
    * [TypeScript](https://www.typescriptlang.org/)
    * [PostgreSQL](https://www.postgresql.org/) (Système de gestion de base de données relationnelle)
    * [`pg`](https://node-postgres.com/) (Client PostgreSQL pour Node.js)
    * [`dotenv`](https://github.com/motdotla/dotenv) (Pour la gestion des variables d'environnement)
    * [`cors`](https://github.com/expressjs/cors) (Middleware Express pour gérer les requêtes Cross-Origin)
    * [`pdfkit`](http://pdfkit.org/) (Génération de PDF en Node.js)
    * [`bcryptjs`](https://github.com/dcodeIO/bcrypt.js) (Pour le hachage des mots de passe)
    * [`jsonwebtoken`](https://github.com/auth0/node-jsonwebtoken) (Pour la génération et la vérification des JWT)

## 4. Architecture du Projet

L'application suit une architecture client-serveur standard :

* **Frontend (Next.js)** : Responsable de l'interface utilisateur et de l'interaction avec l'API backend. Il gère la navigation, l'affichage des données et les interactions utilisateur.
* **Backend (Node.js/Express)** : Fournit une API RESTful pour la gestion des données (patients, consultations, alertes, utilisateurs). Il interagit avec la base de données PostgreSQL, contient la logique métier (calcul d'alertes) et gère l'authentification.
* **Base de Données (PostgreSQL)** : Stocke toutes les données de l'application (informations patients, consultations, alertes et utilisateurs).