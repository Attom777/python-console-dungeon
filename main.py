# ----------------------------------------  IMPORT  ----------------------------------------------

import os
import platform
import sys

# Vérification que le système est Linux
if platform.system() != 'Linux':
    print("\n" + "=" * 70)
    print("  ERREUR : Ce jeu fonctionne uniquement sur Linux !")
    print("=" * 70)
    print(f"\nSystème détecté : {platform.system()}")
    print("\nVeuillez exécuter ce jeu sur un système Linux.")
    input("\nAppuyez sur Entrée pour quitter...")
    sys.exit(1)

try:
  import Lib.Main.mainMenu as main_f  # Main Menu Screen
  import Lib.instructions as instructions_f  # Game Instructions
  import Lib.Donjon.donjonMenu as donjon_menu_f  # Screen Displays
except ImportError as e:
  print(f"\n\nERREUR D'IMPORT : {e}", flush=True)
  print("\nVérifiez que tous les modules sont présents.", flush=True)
  print("Assurez-vous d'être dans le bon répertoire.", flush=True)
  input("\nAppuyez sur Entrée pour quitter...")
  sys.exit(1)
except Exception as e:
  print(f"\n\nERREUR : {e}", flush=True)
  import traceback
  traceback.print_exc()
  input("\nAppuyez sur Entrée pour quitter...")
  sys.exit(1)

# --------------------------------------  VARIABLES  ---------------------------------------------

# ------ [ PLAYER ] ------------------------------------------------------------------------------

player = {
  "caracter": {
    "lifeBarPlayer": 100,
    "levelBarPlayer": 0,
    "inventorPlayer": {}
  },
  "stats": {
    "currentDonjon": 0,
    "currentEnnemiesKilled": 0
  }
}

# ------ [ ENNEMIES ] ------------------------------------------------------------------------------

ennemy1 = {
  "caracter": {
    "lifeBarEnnemy": 10,
    "levelBarEnnemy": 0,
    "inventorEnnemy": {
      "Hache": 2
    }
  }
}

# ---------------------------------------  FONCTION  ---------------------------------------------


def switchValueMain(data):

  if data[0] == 0:  # Si choix est : Valide "Entrer dans le donjon"
    if data[1] == -1:  # Si choix est : "Instruction"
      instructions_f.instructionsDisplay()
      mainMain()
    elif data[1] == 0:  # Si choix est : "Quitter"
      print("AU REVOIR !")
      exit()
    elif data[1] == 1:  # Si choix est : "Entrer dans le donjon"
      recurcifMain()


# -----------------------------------------  MENU  -----------------------------------------------


def recurcifMain(D_viseted=0,
                 D_state=0,
                 R_viseted=1,
                 R_last=1,
                 T_found=0,
                 E_kill=0,
                 B_kill=0,
                 D_numb=1,
                 R_numb=1,
                 R_init=0,
                 R_new=0,
                 P_level=0,
                 P_life=10):

  if (D_viseted == 4) or (P_life <= 0) or (P_level >= 10):  # Conditon d'arret
    donjon_menu_f.endAndDisplay(D_viseted, R_viseted, R_last, T_found, E_kill,
                                B_kill)
    mainMain()

  if R_init == 0:

    recurcifMain(*donjon_menu_f.startOfRoom(
      D_viseted, D_state, R_viseted, R_last, T_found, E_kill, B_kill, D_numb,
      R_numb, 1, R_new, P_level, P_life))

  else:

    os.system('clear')

    print(
    "+------------------------------------------------------------------------------------------------+"
    )
    print(
    "|                                                                                                |"
    )
    print(
      "|                                        INTERFACE : DONJON                                      |"
    )
    print(
      "|                                                                                                |"
    )
    print(
      "+------------------------------------------------+-----------------------------------------------+"
    )
    print(
      "|                                                |                                               |"
    )
    print(
      "|                  INFO : PLAYER                 |                 INFO : DONJON                 |"
    )
    print(
      "|                                                |                                               |"
    )
    print(
      "|         ---------------------------------      |        ---------------------------------      |"
    )
    print(
      "|                                                |                                               |"
    )
    print(
      "|  VIE DU JOUEUR     :", P_life, "                       |  DONJON ACTUEL    :", D_numb, "                        |"
    )
    print(
      "|  NIVEAU DU JOUEUR  :", P_level, "/ 10                    |  SALLE ACTUEL     :", R_numb,"                        |"
    )
    print(
      "|                                                |                                               |"
    )
    print(
     "+------------------------------------------------+-----------------------------------------------+")

    print("\n")
    print("----------------------------------------------------------------------------------------------")
    print("\n")
    print("> Vous entrez dans une nouvelle pièce")
    input("Continuer...")
    
    if D_state == 0:
      print("\n> Ah ! Cette salle est vide...")
      
      input("\nAvancer dans la salle suivante (Enter) ")
      recurcifMain(D_viseted, D_state, R_viseted + 1, R_last + 1, T_found,
                   E_kill, B_kill, D_numb, R_numb + 1, 0, 1, P_level, P_life)
    elif D_state == 1:
      print("\n> Attention ! Un ennemi en vu, combat en cours...")
      #donjon_menu_f.battleDisplay(a+1,b+1)
      
      input("\nAvancer dans la salle suivante (Enter) ")
      recurcifMain(D_viseted, D_state, R_viseted + 1, R_last + 1, T_found,
                   E_kill + 2, B_kill, D_numb, R_numb + 1, 0, 1, P_level + 1,
                   P_life)
    elif D_state == 2:
      print("\n> Oh ! Un trésor !")
      input("Continuer...")
      print("\n> Trésor récupéré")
      
      input("\nAvancer dans la salle suivante (Enter) ")
      recurcifMain(D_viseted, D_state, R_viseted + 1, R_last, T_found + 1,
                   E_kill, B_kill, D_numb, R_numb + 1, 0, 1, P_level, P_life)
    else:
      os.system('clear')
      
      print("Changement de donjon")
      input("\nContinuer...")
      recurcifMain(*donjon_menu_f.startOfRoom(
        D_viseted + 1, D_state, R_viseted, 1, T_found, E_kill, B_kill, D_numb +
        1, 1, 0, 1, P_level, P_life))


# -----------------------------------------  MAIN  -----------------------------------------------


def mainMain():

  valueMain = main_f.main()
  switchValueMain(valueMain)


if __name__ == "__main__":
  try:
    mainMain()
  except KeyboardInterrupt:
    print("\n\nAu revoir !")
    input("\nAppuyez sur Entrée pour quitter...")
  except ImportError as e:
    print(f"\n\nERREUR D'IMPORT : {e}")
    print("\nVérifiez que la bibliothèque 'pick' est installée :")
    print("  pip install pick")
    input("\nAppuyez sur Entrée pour quitter...")
  except Exception as e:
    print(f"\n\nERREUR : {e}")
    import traceback
    print("\nDétails de l'erreur :")
    traceback.print_exc()
    print("\nVérifiez que la bibliothèque 'pick' est installée :")
    print("  pip install pick")
    input("\nAppuyez sur Entrée pour quitter...")
