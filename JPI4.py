#!/usr/bin/python3
n = int(input("Entrer un nombre :"))
l = []
a = 1
for i in range (n):
	l.append(a)
print(l)
for j in range (n-1):
	for k in range (1+j,n):
		l[k] = l[k] + 1
		k+=1
	print(l)

	
	
	
