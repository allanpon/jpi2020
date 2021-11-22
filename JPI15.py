#!/usr/bin/python3
n = 1000
def ret(n):
    i = 0
    while(n>0):
        x=n%10
        i  = i * 10 + x
        n = n//10
    return(i)
print(ret(n))
while n < 3000:
    if  (n*4)==(ret(n)):
        print(n)
    else:
        n += 1

