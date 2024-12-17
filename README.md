# Projet de Prédiction d'Images avec TensorFlow Lite et Flask

Ce projet permet d'utiliser un modèle TensorFlow Lite pour prédire la classe d'une image téléchargée par un utilisateur à travers une interface web intuitive.

## Table des Matières
- [Description du Projet](#description-du-projet)
- [Technologies Utilisées](#technologies-utilisées)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Exécution](#exécution)
- [Structure du Projet](#structure-du-projet)
- [Utilisation](#utilisation)
- [Exemple de Fonctionnement](#exemple-de-fonctionnement)
- [Auteurs](#auteurs)

---

## Description du Projet

L'application utilise **Flask** comme serveur backend pour charger un modèle TensorFlow Lite et prédire la classe d'une image fournie par l'utilisateur. Une interface web simple permet à l'utilisateur de télécharger une image, de la prévisualiser, et de recevoir le résultat de la prédiction.

Les classes prédites incluent différentes maladies des plantes et des statuts sains pour :
- **Poivron**
- **Pomme de terre**
- **Tomate**

---

## Technologies Utilisées
- **Python 3.x**
- **Flask** : Pour le serveur web
- **TensorFlow Lite** : Modèle d'apprentissage automatique pour la prédiction
- **HTML/CSS/JavaScript** : Interface utilisateur
- **Pillow (PIL)** : Manipulation des images
- **NumPy** : Traitement des données

---

## Prérequis
Avant d'exécuter le projet, assurez-vous d'avoir :
- Python 3.x installé
- **pip** pour gérer les dépendances
- TensorFlow Lite (fichier `model.tflite`)

---

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/AyoubDammaq/PlantDiseasePredictorApp.git
   cd PlantDiseasePredictorApp
   ```

2. Créez un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate   # Pour Linux/Mac
   venv\Scripts\activate      # Pour Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Placez votre modèle TensorFlow Lite dans le répertoire racine avec le nom `model.tflite`.

---

## Exécution

1. Lancez l'application Flask :
   ```bash
   python app.py
   ```

2. Ouvrez votre navigateur à l'adresse suivante :
   ```
   http://127.0.0.1:5000
   ```

---

## Structure du Projet

```
projet-prediction-images/
|-- templates/
|   |-- index.html          # Interface utilisateur HTML
|
|-- app.py                  # Backend Flask
|-- model.tflite            # Modèle TensorFlow Lite
|-- requirements.txt        # Dépendances
|-- README.md               # Documentation
```

---

## Utilisation

1. **Télécharger une image** :
   - Cliquez sur le bouton pour choisir une image depuis votre appareil.
   - L'image est prévisualisée sur l'interface.

2. **Faire la prédiction** :
   - Cliquez sur le bouton "Faire la Prédiction".
   - L'application envoie l'image au backend Flask.
   - Le modèle TensorFlow Lite prédit la classe de l'image.

3. **Voir le résultat** :
   - La classe prédite s'affiche à l'écran.

---

## Exemple de Fonctionnement

### 1. Page d'accueil
![Page d'accueil](https://github.com/user-attachments/assets/b2683fb5-b7b2-4c99-a790-a332247b9a3a)

### 2. Image téléchargée
![Image téléchargée](https://github.com/user-attachments/assets/2ebfa4fc-f415-4e9f-b7db-63a4a474c3d3)

### 3. Résultat de la prédiction
![Résultat prédiction](https://github.com/user-attachments/assets/770f703e-71f7-4695-9066-2d08e59c715f)

- **Image Téléchargée** : Photo de feuille de tomate malade.
- **Prédiction** : `Tomato_Leaf_Mold`

---

## Auteurs
- **Ayoub Dammak** : Développement et conception

---

**Merci d'utiliser ce projet ! N'hésitez pas à contribuer ou poser des questions.**

---
