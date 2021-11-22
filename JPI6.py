#!/usr/bin/python3
n = int(input("Entrer un nombre :"))
a = "*"
for i in range (1,n*2+1,2):
	étoile = i * a
	print(étoile.center(n*10))
	

