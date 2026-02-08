# --------------------------------------  IMPORT  --------------------------------------
import os

import Lib.Donjon.donjon_map as donjMap

#from pick import pick

# --------------------------------------  FONCTIONS  --------------------------------------


# COMBAT ---------------------
def battleDisplay(R_numb, P_level, P_life):

  os.system('clear')

  print(
    "+--------------------------------------------------------------------------------------------+"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "|                                 INTERFACE : COMBAT ENNEMIE                                 |"
  )
  print(
    "|                                                                                            |"
  )
  print(
    "+----------------------------------------------+---------------------------------------------+"
  )
  print(
    "|                                              |                                             |"
  )
  print(
    "|                 INFO : PLAYER                |                INFO : ENNEMIE               |"
  )
  print(
    "|                                              |                                             |"
  )
  print(
    "|       ---------------------------------      |       ---------------------------------     |"
  )
  print(
    "|                                              |                                             |"
  )
  print(
    "|  Donjon visitée      : 1                     |                                             |"
  )
  print(
    "|  Salle(s) traversée  : 1                     |                                             |"
  )
  print(
    "|  Dernière salle      : 1                     |                                             |"
  )
  print(
    "|                                              |                                             |"
  )
  print(
    "|                                              |                                             |"
  )
  print(
    "+------------------------------+------------------------------+------------------------------+"
  )
  print(
    "|                                     TRÉSOR                              |"
  )
  print(
    "|               -              |               -              |               -              |"
  )
  print(
    "|  Donjon visitée      : 1     |                              |  Ennemie(s) vaincue  : 0    |"
  )
  print(
    "|  Salle(s) traversée  : 1    |  Trésor(s) trouvé  : 0       |  Boss vaincue        : 0     |"
  )
  print(
    "|  Dernière salle      : 1     |                              |                              |"
  )
  print(
    "|               -              |               -              |               -              |"
  )
  print(
    "+------------------------------+------------------------------+------------------------------+"
  )
  input("")


# FIN ---------------------
def endAndDisplay(D_viseted, R_viseted, R_last, T_found, E_kill, B_kill):

  os.system('clear')

  print(
    "+-----------------------------------------------------------------------------------------------------------+"
  )
  print(
    "|                                                                                                           |"
  )
  print(
    "|                                       FIN DE PARTIE : RÉCAPITULATIF                                       |"
  )
  print(
    "|                                                                                                           |"
  )
  print(
    "+-----------------------------------+-----------------------------------+-----------------------------------+"
  )
  print(
    "|              DONJONS              |               TRÉSOR              |               ENNEMIE             |"
  )
  print(
    "|                 -                 |                 -                 |                  -                |"
  )
  print("|  Donjon visitée (fini)  :", D_viseted,
        "      |                                   |  Ennemies vaincue  :",
        E_kill, "           |")
  print("|  Salles traversées      :", R_viseted,
        "      |  Trésor(s) trouvé  :", T_found,
        "           |                                   |")
  print("|  Dernière salle         :", R_last,
        "      |                                   |  Boss vaincue        :",
        B_kill, "         |")
  print(
    "|                 -                 |                 -                 |                  -                |"
  )
  print(
    "+-----------------------------------+-----------------------------------+-----------------------------------+"
  )

  input("")


# DEBUT DE SALLE ---------------------
def startOfRoom(D_viseted, D_state, R_viseted, R_last, T_found, E_kill, B_kill,
                D_numb, R_numb, R_init, R_new, P_level, P_life):

  os.system('clear')

  return (D_viseted, donjMap.Game[D_numb - 1]["way"][R_numb - 1], R_viseted,
          R_last, T_found, E_kill, B_kill, D_numb, R_numb, 1, R_new, P_level,
          P_life)


# OTHER ---------------------
