import json
import requests

from random import randint
from consumo_api import get_all_sw_characters, get_charter_by_id, get_all_sw_characters_names



""" lista = []

nombre1 = input("Ingresar el nombre del personaje numero 1")
nombre2 = input("Ingresar el nombre del personaje numero 2")
altura1 = int(input("Ingresar la altura del personaje 1"))
altura2 = int(input("Ingresar la altura del personaje 2"))
peso1 =int(input("Ingresar el peso del personaje 1"))
peso2 =int(input("Ingresar el peso del personaje 2"))
planeta_origen1 =input("Ingresar de que planeta es originario el personaje 1")
planeta_origen2 =input("Ingresar de que planeta es originario el personaje 2")
peliculas1 =int(input("Ingresar el numero de peliculas en las q participo"))
peliculas2 =int(input("Ingresar el numero de peloculas en las q participo"))

personaje1 = [nombre1,altura1,planeta_origen1,peliculas1,peso1]
personaje2 = [nombre2,altura2,planeta_origen2,peliculas1,peso2]

if(altura2 < altura1):
    print(nombre2, "es mas bajo que", nombre1)
else:
    print(nombre1,"es mas bajo que", nombre2)
    
if(peso1 < peso2):
    print(nombre2, "es mas pesado que", nombre1)
else:
    print(nombre1,"es mas pesado que", nombre2)

if(peliculas1 < peliculas2):
    print(nombre2, "participo en mas peliculas que", nombre1)
elif(peliculas1 == peliculas2):
    print("Ambos participaron en la misma cantidad de peliculas")
else:
    print(nombre1,"participo en mas peliculas que", nombre2) """


#Actividad "2"#
""" def ordenar(item):
   return item['name']


from consumo_api import get_all_sw_characters

sw_data = get_all_sw_characters()
sw_data.sort(key=ordenar)
for index, character in enumerate(sw_data):
    print( character['name'], character['height'],len(character['films']))
 """


#ACT 3#
""" from random import randint
lista = []

for i in range(50):
     lista.append(randint(1, 100))
print("El rango de valores es de 0 a 100")
print("La diferencia entre el mayor y el menor es", lista[0] - lista[-1])
lista.sort()

print('menor', lista[0])
print('mayor', lista[-1])



print('listado de menor a mayor')

for num in lista:
     print(num)

lista.sort(reverse=1)

print('menor', lista[-1])
print('mayor', lista[0])



print('listado de mayor a menor')

for num in lista:
     print(num)

print("El promedio de los numeros generados es")
print(sum(lista) / 100)

print('Lista de impares multiplos de 3')
for num in lista:
    if(num % 2 == 0 and num % 3 > 0):
        print(num) """