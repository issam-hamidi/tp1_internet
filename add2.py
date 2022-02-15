import csv
import os


def command(commande): os.system(commande)


ping = ""
with open("fichier.csv") as fichier:
  data = csv.reader(fichier)
  for ligne in data:
    if len(ligne[0]) > 4:
     if ("/16" in ligne[2]): ligne[2] = ligne[2][:-3]
     print("ip route add dst-address={} gateway={}".format(ligne[1], ligne[2]))
     if ("/16" in ligne[3] or "/24" in ligne[3]): ligne[3] = ligne[3][:-3]
     ping += "ping -c 1 "+ligne[3]+os.linesep

print(ping)
