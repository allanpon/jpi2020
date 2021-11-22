#!/usr/bin/python3
import math
print ("Calcul")
print ("1 : Rayon")
print ("2 : Hauteur")
print ("3 : Volume")
choix = int(input("choix :"))
if choix == 1 or choix == 2 or choix == 3:
	if choix == 1:
		v = int(input("Entrer un nombre :"))
		h = int(input("Entrer un nombre :"))
		r = math.sqrt(v/(3.14*h))
		print("Le rayon est",r)
	if choix == 2:
		v = int(input("Entrer un nombre :"))
		r = int(input("Entrer un nombre :"))
		h = v/(3.14*r*r)
		print("La hauteur est",h)
	if choix == 3:
		r = int(input("Entrer un nombre :"))
		h = int(input("Entrer un nombre :"))
		v = 3.14*r*r*h
		print("Le volume est",v)
