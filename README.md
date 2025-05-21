# 📦 Chargement Optimisé de Boîtes sur Palette

Ce projet Python permet de calculer et de visualiser de manière optimale le chargement de boîtes sur une palette. Il prend en compte les dimensions de la palette, les dimensions des boîtes, les contraintes de poids et de hauteur, et propose la meilleure orientation pour maximiser l'utilisation de l'espace.

---

## ✅ Fonctionnalités

- 💡 Choix automatique de l’orientation optimale des boîtes.
- 📊 Calcul du nombre de boîtes chargeables selon les contraintes.
- 📏 Prise en compte de la hauteur maximale et de la charge maximale de la palette.
- 🧊 Visualisation 3D du chargement à l’aide de `matplotlib`.

---

## 📁 Structure du Projet

- `calculer_chargement()` : Calcule les configurations possibles et sélectionne la plus optimisée.
- `draw_box()` : Dessine une boîte sur une scène 3D.
- `afficher_chargement_3d()` : Génère la visualisation 3D.
- `main()` : Interface interactive en ligne de commande.

---

## 🛠️ Prérequis

Installez les bibliothèques nécessaires avant d’exécuter le script :

`bash`
pip install matplotlib



Exécution
Lancez le script via la ligne de commande :

`bash`
python script.py
Puis entrez les informations demandées :

Longueur palette (cm) : 120
Largeur palette (cm) : 80
Hauteur max palette (cm) : 150
Charge max palette (kg) : 500
Longueur boîte (cm) : 30
Largeur boîte (cm) : 20
Hauteur boîte (cm) : 15
Poids boîte (kg) : 5
Nombre max de couches souhaité : 4
Souhaitez-vous choisir une orientation ? (o/n) : n
Le programme retournera :

✅ Nombre total de boîtes

📐 Orientation choisie (optimale ou imposée)

🧱 Nombre de boîtes par couche

📦 Nombre de couches utilisées

📉 Chargement 3D affiché à l’écran

Exemple d’Entrée
yaml

Palette : 120 x 80 x 150 cm
Boîte : 30 x 20 x 15 cm
Poids boîte : 5 kg
Charge max : 500 kg
Nombre max de couches : 4
Sortie :

yaml

Orientation optimale : (30, 20, 15)
Boîtes par couche : 16
Couches : 4
Total : 64 boîtes
📸 Visualisation 3D
Une fenêtre s'ouvre avec la visualisation 3D du chargement :

Palette représentée en bleu clair.

Boîtes affichées en rouge (une par une).

Dimensions et orientation visibles par projection.

`Licence`
Ce projet est distribué sous la licence MIT. Vous pouvez l’utiliser, le modifier ou le partager librement à des fins personnelles, académiques ou professionnelles.

`Auteur`
Projet développé par Hocine – Étudiant en Master Génie Logistique.
Contact : elma.hocine@gmail.com

Contributions
Les contributions sont les bienvenues !
Vous pouvez ouvrir une issue ou proposer une pull request pour :

Ajouter de nouvelles visualisations (2D, interactive, etc.)

Intégrer la gestion de palettes multiples

Améliorer l’interface utilisateur
