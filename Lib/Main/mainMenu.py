# --------------------------------------  IMPORT  --------------------------------------
import os

# --------------------------------------  FONCTIONS  --------------------------------------

def pickOption():

  os.system('clear')

  print("=" * 70)
  print(" " * 25 + "MENU PRINCIPAL")
  print("=" * 70)
  print()
  print("  Choisissez une option :")
  print()
  print("  1. 🌋 EXPLORER LES DONJONS")
  print("  2. 📜 LIRE LES INSTRUCTIONS")
  print("  3. ❌ QUITTER LE JEU")
  print()
  print("=" * 70)
  
  while True:
    try:
      choix = input("\nVotre choix (1-3) : ").strip()
      
      if choix == "1":
        return 1  # EXPLORER LES DONJONS (correspond à l'index original 1)
      elif choix == "2":
        return 3  # INSTRUCTIONS (correspond à l'index original 3)
      elif choix == "3":
        return 5  # QUITTER (correspond à l'index original 5)
      else:
        print("❌ Choix invalide ! Veuillez entrer 1, 2 ou 3.")
    except (EOFError, KeyboardInterrupt):
      print("\n\nAu revoir !")
      return 5  # Quitter

def switchChoose(data):

  if data == 1: # Si choix est : "Entrer dans le donjon"
    return [0, 1]
  elif data == 3: # Si choix est : "Instruction"
    return [0, -1]
  elif data == 0 or data == 2 or data == 4: # Si choix est : "EMPTY"
    return main()
  elif data == 5: # Si choix est : "Quitter"
    return [0, 0]

# --------------------------------------  MAIN MENUE  --------------------------------------

def main():

  chooseUser = pickOption() # Fonction pour récuperer le chox du joueur

  chooseVerifed = switchChoose(chooseUser) # Fonction pour décider quoi faire avec le choix du joueur

  return chooseVerifed # retour des valeurs en tab [a, b]
