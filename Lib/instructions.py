import os


# INSTRUCTIONS ---------------------
def instructionsDisplay():

  tab = ["Vous allez explorer un donjon comportant 4 sous donjon.", "Vous commencez niveau 0 et avec une vie pleine (10 pv).", "Vous rencontrerez, soit une salle : Vide ; Avec des ennemis ; Avec des trésors.", "Un tableau vous présenteras vos stats finaux."]
  gen = iter(tab)

  os.system('clear')

  print(
    "+--------------------------------------------------------------------------------------------+"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|                                    TABLEAU - INSTRUCTIONS                                  |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "+--------------------------------------------------------------------------------------------+"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|  - Bienvenue ! Dans mon projet 2022 - Donjon infernal !                                    |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|  -", next(gen), "                                |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|  -", next(gen), "                                |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|  -", next(gen), "        |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|  -", next(gen), "                                          |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|  - Bonne chance, jeune explorateur !                                                       |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|                        Crédit (2022) : Neo Faroux (Dévellopeur)                            |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "+--------------------------------------------------------------------------------------------+"
  )

  input("")
