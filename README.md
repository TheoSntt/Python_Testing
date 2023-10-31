
# GUDLIFT


## Description du projet

Ce projet, réalisé dans le cadre de ma formation OpenClassrooms était centré sur les notions de débugage et de tests. L'application Flask, très basique, a été fournie par OpenClassrooms comme base de travail. L'objectif du projet était de débuguer l'application, d'y ajouter quelques fonctionnalités, et de rédiger des tests unitaires, d'intégration, et de performance.  
Les différentes évolutions apportées à l'application ont été réalisées en TDD (test driven development).  
Ce projet m'a permis d'apprendre le développement de tests, notamment des tests unitaires avec Pytest. Il m'a aussi permis d'appréhender le TDD, et d'avoir une introduction aux applications Flask.

## Mise en place et exécution en local de l'application

1. Téléchargez le projet depuis Github. Soit directement (format zip), soit en clonant le projet en utilisant la commande suivante dans Git Bash :  
```
git clone https://github.com/TheoSntt/python-testing
```
2. Créez un environnement virtuel Python en exécutant la commande suivantes dans le Terminal de votre choix :
```
python -m venv env (env étant le nom de l'environnement, vous pouvez le changer)
```
Puis, toujours dans le terminal, activez votre environnement avec la commande suivante si vous êtes sous Linux :
```
source env/bin/activate
```
Ou bien celle-ci si vous êtes sous Windows
```
env/Scripts/activate.bat
```
3. Dans vorte environnement virtuel, téléchargez les packages Python nécessaires à la bonne exécution de l'application à l'aide de la commande suivante :
```
pip install -r requirements.txt
```
4. Vous pouvez maintenant exécuter l'application en local. Il vous suffit de lancer le serveur local, à l'aide de la commande suivante :
```		
python server.py
```
5. L'application est prête à être utilisée. Vous pouvez utiliser un mail présent dans le fichier db/clubs.json pour vous connecter. Vous avez désormais accès aux fonctionnalités de l'application : réserver des places dans différentes compétitions, places qui seront déduites des points dont dispose le club.

## Exécution des tests

Les tests ont été réalisés à l'aide de Pytest, pour les exécuter, lancer la commande suivante :
```		
pytest
```
Pour obtenir la couverture de test, celle-ci :
```		
pytest --cov=.
```
Pour générer un rapport HTML de la couverture de test, celle-ci :
```		
pytest --cov=. --cov-report html
```

