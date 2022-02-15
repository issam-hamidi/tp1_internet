##### FAUT ENREGISTRER LE FICHIER EN CSV


import csv
import os


def command(commande): os.system(commande)

with open("fichier.csv") as fichier:
  data = csv.reader(fichier)
  for ligne in data:
    if len(ligne[0]) > 4:
     if ("/16" in ligne[2]): ligne[2] = ligne[2][:-3]
     print("ip route add dst-address={} gateway={}".format(ligne[1], ligne[2]))

