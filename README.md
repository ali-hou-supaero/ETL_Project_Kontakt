# ETL_Project_Kontakt

Voici la marche à suivre pour que l'on puisse collaborer efficacement **en utilisant des branches Git**.  

---

## Pourquoi utiliser des branches ?

Lorsque plusieurs personnes travaillent sur le même projet, modifier directement la branche principale (`main`) peut créer des conflits ou écraser le travail des autres.  
Les **branches** permettent à chacun de développer ou tester de nouvelles fonctionnalités sans perturber le code principal.  

En résumé :  
- Chaque personne travaille sur **sa propre branche**.  
- Une fois le travail terminé et validé, on **fusionne la branche** dans `main`.

---

## 1. Récupérer le repository

Clonez le repository sur votre ordinateur :

```bash
git clone https://github.com/ali-hou-supaero/stat_project_weather.git
```
ou via SSH
```bash
git@github.com:ali-hou-supaero/ETL_Project_Kontakt.git
```

## 2. Créer et passer sur votre propre branche

Avant de commencer à travailler, créez une nouvelle branche à votre nom ou au nom de la fonctionnalité que vous développez.
```bash
git checkout -b prenom-nom
```
Exemple :
```bash
git checkout -b ali-analyse-temp
```
Explication :

checkout -b : crée une nouvelle branche et vous place directement dessus.

Le nom de la branche doit être court, explicite et sans espaces.

Métaphore : vous partez avec une copie de travail personnelle du projet, indépendante de celle des autres.

3. Travailler sur votre branche

Modifiez, ajoutez ou supprimez des fichiers dans votre environnement local (par exemple, dans Jupyter Notebook).

4. Sauvegarder vos modifications en local
4.1 Préparer les fichiers à sauvegarder
```bash
git add nom_du_fichier.ipynb
```

Cette commande prépare le fichier pour être sauvegardé.
C’est comme mettre vos feuilles dans un classeur.


4.2 Sauvegarder localement avec un message
```bash
git commit -m "Ajout de la question 3"
```

Cette commande enregistre définitivement les fichiers préparés avec git add.
Vous pouvez ainsi garder une trace des modifications dans le temps.

Métaphore : vous rangez votre classeur dans votre armoire avec une étiquette (“Ajout de la question 3”).

5. Mettre à jour votre branche avec les dernières modifications de main

Avant d’envoyer votre travail, il faut vous assurer que votre branche est à jour avec la branche principale (main) :
```bash
git pull origin main
```

Cela récupère les dernières modifications faites sur main et les intègre dans votre branche.

S’il y a des conflits :

Git vous les signalera et vous guidera pour les résoudre.
Une fois réglés, validez avec :
```bash
git add nom_du_fichier_conflit.ipynb
git commit -m "Résolution de conflit"
```
6. Envoyer votre travail sur GitHub

Une fois vos modifications terminées et testées, envoyez votre branche sur GitHub :
```bash
git push origin prenom-nom
```
Avec l'exemple précédent :
```bash
git push origin ali-analyse-temp
```

Explication :

push : envoie vos modifications locales sur GitHub.

origin : correspond au dépôt distant (le repository en ligne).

prenom-nom : correspond à votre branche personnelle.

7. Créer une Pull Request (PR)

Allez sur la page GitHub du projet.
Vous verrez une proposition pour “Compare & pull request” : cliquez dessus.

Ajoutez un titre et une courte description de votre travail.

Cliquez sur Create pull request.

Cela permet à l’équipe (ou au responsable du projet) de vérifier et fusionner votre travail dans la branche principale main.

8. Fusion et nettoyage

Une fois votre PR validée et fusionnée dans main :

Supprimez la branche sur GitHub (GitHub propose souvent un bouton “Delete branch”).

Supprimez aussi la branche en local :
```bash
git branch -d prenom-nom
```

Puis repassez sur la branche principale :
```bash
git checkout main
git pull origin main
```

Vous êtes maintenant à jour pour la suite du projet !

## Résumé des commandes utiles

| 🧩 Action | 💻 Commande | 🧠 Explication |
|------------|-------------|----------------|
| **Cloner le projet** | `git clone <url>` | Récupère le projet depuis GitHub |
| **Créer une branche** | `git checkout -b ma-branche` | Crée et passe sur une nouvelle branche |
| **Ajouter un fichier** | `git add mon_fichier.ipynb` | Prépare le fichier à être sauvegardé |
| **Sauvegarder localement** | `git commit -m "message"` | Enregistre les modifications en local |
| **Mettre à jour sa branche** | `git pull origin main` | Récupère les nouveautés de la branche principale |
| **Envoyer sa branche** | `git push origin ma-branche` | Envoie votre travail sur GitHub |
| **Supprimer une branche locale** | `git branch -d ma-branche` | Supprime la branche de votre ordinateur |
