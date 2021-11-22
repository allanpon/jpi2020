#!/usr/bin/pyhton3
import random
n = random.randint(1,100)
while True :
	a = int(input("Entrer un nombre :"))
	if a < n:
		print("C'est trop petit !")
	else:
		print("C'est trop grand!")
	if a == n:
		print("Félicitations, vous avez trouvé le nombre mystère !!!")
		
