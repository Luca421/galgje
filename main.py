import os
import time
import random
fout = 0
doorgaan = True
woorden = ["vader", "moeder", "ernaar", "boomhut", "theekopje", "school", "computer", "hoeveelheid", "pasta", "weeg", "diamandslijper", "insect", "kronkelpaden", "protestant", "probleemkind", "deo", "onbedrevenheid", "snapte", "snaaks", "terras", "sukkel"]
woord = random.choice(woorden)
geraden_woord = ""
geraden_letters = ""

def begin_text():
  print("welkom bij galgje")

def vraag_letter():
  letter = input("geef een letter: ")
  return letter
  
  
def print_galg(fout):
  if fout == 0:
    print("______________")
    print("|            ")
    print("|           ")
    print("|           ")
    print("|            ")
    print("|           ")
    print("|            ")
    print("|           ")
    print("___")
  elif fout == 1:
    print("______________")
    print("|            |")
    print("|           / \\")
    print("|           \ /")
    print("|            ")
    print("|           ")
    print("|            ")
    print("|           ")
    print("___")
  elif fout == 2:
    print("______________")
    print("|            |")
    print("|           / \\")
    print("|           \ /")
    print("|            |")
    print("|           ")
    print("|            ")
    print("|           ")
    print("___")
  elif fout == 3:
    print("______________")
    print("|            |")
    print("|           / \\")
    print("|           \ /")
    print("|            |")
    print("|            |")
    print("|            ")
    print("|           ")
    print("___")
  elif fout == 4:
    print("______________")
    print("|            |")
    print("|           / \\")
    print("|           \ /")
    print("|            |")
    print("|            |")
    print("|            |")
    print("|           ")
    print("___")
  elif fout == 5:
    print("______________")
    print("|            |")
    print("|           / \\")
    print("|           \ /")
    print("|            |")
    print("|           \|/")
    print("|            |")
    print("|           ")
    print("___")
  elif fout == 6:
    print("______________")
    print("|            |")
    print("|           / \\")
    print("|           \ /")
    print("|            |")
    print("|           \|/")
    print("|            |")
    print("|           / \\")
    print("___")

def verander_geraden_woord(geraden_woord, geraden_letters):
  geraden_woord = ""
  for letter in woord:
    if letter in geraden_letters:
      geraden_woord += letter
    else:
      geraden_woord += "_"
  return geraden_woord, geraden_letters

def fout_check(fout):
  if fout == 6:
    return False
  return True

def check_letter_geraden(letter, geraden_letters):
  if letter in geraden_letters:
    print("je hebt die letter al geraden...")
    return False
  else:
    return True

def letter_valid(letter):
  if len(letter) > 1:
    print("je mag maar 1 letter invoeren.")
    return False
  if not letter.isalpha():
    print("je mag alleen letters invoeren.")
    return False
  return True

begin_text()
while doorgaan:
  time.sleep(1)
  os.system("clear")
  print_galg(fout)
  print(geraden_woord)
  letter = vraag_letter()
  if not letter_valid(letter):
    continue
  if not check_letter_geraden(letter, geraden_letters):
    continue
  geraden_letters += letter
  if letter not in woord:
    fout += 1
  else:
    geraden_woord, geraden_letters = verander_geraden_woord(geraden_woord, geraden_letters)
  fout_vraagteken = fout_check(fout)
  if fout_vraagteken == False:
    print("dat was je laatste poging je hebt gefaald.")
    doorgaan = False
  elif geraden_woord == woord:
    if fout == 0:
      print("JE BENT HACKER")
      doorgaan = False
    print("je hebt het woord geraden! het woord was: " + woord)
    doorgaan = False