#!/usr/bin/python3
liste1 = [4,8,7,12]
liste2 = [3,6]
x = 0 
y = 0
for i in range(0, len(liste1)):
	for j in range(0,len(liste2)):
		x += liste1[i]*liste2[j]
x = list(str(x))
for j in range(0,len(x)):
	y += int(x[j])
print(y)





