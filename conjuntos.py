from collections import deque

col = deque([1,2,3,4,5])
lista = [3,2,2,1,3,4,1,5,5,5,5]
tupla = (6,7,8,9,10)
conjunto = {11,12,13,14,15}

print (lista)

temporal = set (lista) # Convertimos a lista en un conjunto <- La ordena y elimina los duplicados

lista = list(temporal) # Convertimos el conjunto en un objeto Lista Iterable

print (lista)

for i, x in enumerate(lista):
    del lista[i]

print (lista)

for i, x in enumerate(lista):
    print(lista[i])

i=0

while i != 50:
    i = int (input ("ingrese un numero a consultar (si desea salir ingrese 50) : " ))

    if i in lista:
        print (str(i) + " se encuentra en la lista")
    elif i in tupla:
        print (str(i) + " se encuentra en la tupla")
    elif i in conjunto:
        print (str(i) + " se encuentra en el conjunto")
    else:
        print (str(i) + " no se encuentra en ninguna colección de datos") 