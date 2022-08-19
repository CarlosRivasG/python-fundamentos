#ejercicio 1
for i in range(1, 151):
    print(i)

#Ejercicio 2
for i in range(1,1005):  
    if i%5==0:  
        print(i)  

#Ejercicio 3
i = 1
for i in range(1,101):
    if i%10==0:  
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)


#Ejercicio 4
sumimp = 0

for i in range(1, 500000):
    if i%2 !=0:
        print(i)
        sumimp = sumimp + i
    
print("La suma total es: ", sumimp)

#Ejercicio 5
i = 2018
while i > 0:
    print(i)
    i = i - 4

#Ejercicio 6

lowNum = 1
highNum = 100
mult = 4
i = 0
for i in range( lowNum, highNum):
    if i%mult ==0:
        print(i)




