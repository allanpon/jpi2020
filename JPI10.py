#!/usr/bin/python
n = int(input("Entrer un nombre :"))
def ret(n):
	inverse = 0
	while(n>0):
		a=n%10
		inverse = inverse * 10 + a
		n = n//10
	return(inverse)
print(ret(n))

