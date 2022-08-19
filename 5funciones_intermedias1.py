print("Ejercicio 1")
x = [ [5,2,3], [10,8,9] ] 
x[1] = [15, 8, 9]
print(x)

print("Ejercicio 2")
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]['last_name'] = 'bryan'
print(estudiantes)

print("Ejercicio 3")

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'][0]= 'Andres'
print(directorio_deportes)

print("Ejercicio 4")
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)




estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(estudiantes):
    for p in estudiantes:
        print('first_name - ', p['first_name'], 'last_name - ', p['last_name'])

iterateDictionary(estudiantes)

name ='first_name'
name2 = 'last_name'

def iterateDictionary2():
       
       
        print(estudiantes[0][name])
        print(estudiantes[1][name])
        print(estudiantes[2][name])
        print(estudiantes[3][name])
          
iterateDictionary2()

def iterateDictionary2():
        print(estudiantes[0][name2])
        print(estudiantes[1][name2])
        print(estudiantes[2][name2])
        print(estudiantes[3][name2])
          
iterateDictionary2()

print("-------------------------------------------------")
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo():
        numu= len(dojo['ubicaciones'])
        print(numu, "", 'UBICACIONES')
        for ubic in dojo['ubicaciones']:
                print(ubic)
        print("  ")

        num = len(dojo['instructores'])
        print(num, "", 'INSTRUCTORES')
        for inst in dojo['instructores']:
                print(inst)
printInfo()

