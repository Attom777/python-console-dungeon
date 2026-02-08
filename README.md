# Jeu textuel en Python : "DONJON" #

## Installation

Aucune installation nécessaire ! Le jeu utilise uniquement des bibliothèques Python standard.

> [!Important]
> Ce jeu fonctionne uniquement sur un système d'exploitation Linux !

## Lancement

Depuis le répertoire, lancez :

```bash
python3 main.py
```

ou

```bash
python main.py
```

## Règles du jeu

### Menu principal
- Propose au moins un choix au joueur : celui d'explorer un donjon.
- Option : Quitter le programme.

### Le joueur
- Un niveau : l'expérience qu'il gagne au cours du jeu.
- De la vie : une valeur représentant sa santé.
- Un inventaire : le(s) objet(s) qu'il transporte.

### Initiation
- Le personnage est de niveau 0.
- Le personnage est de vie max (10 pv).
- Le personnage ne possède rien.

### Les donjons
- Un donjon est composé de plusieurs salles dans lesquelles se trouvent soit un ou plusieurs ennemis à combattre, soit des récompenses à prendre.
- Un donjon a au moins une salle contenant une récompense et une salle contenant un ou plusieurs ennemis.
- Au fur et à mesure des donjons explorés, le personnage gagne des niveaux d'expérience et des objets lui donnant des avantages pour mieux réussir les combats des donjons suivants.

### Fin de jeu
- Le jeu se termine lorsque le personnage a atteint le niveau 10.
- Un résumé de la partie s'affiche (ex. nombre de donjons explorés, nombre d'ennemis vaincus, etc.).

## Crédits

Projet 2022 - Neo Faroux (Développeur)
