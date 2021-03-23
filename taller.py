# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:49:09 2021

@author: jorge
"""


# 1. De los n elementos de un vector dado calcule:
vector = []
i = 1
while True:
    numero = int(input(f'Digite el número {i} o digite 0 para salir: '))
    if numero == 0:
        break
    i += 1
    vector.append(numero)
def produc(vec):
    productoria = 1
    for i in vec:
        productoria = productoria * i
    return productoria
    
print(f'La sumatoria del vector es: {sum(vector)}')
print(f'La productoria del vector es: {produc(vector)}')
print(f'El número mayor del vetor es: {max(vector)}')
print(f'El número menor del vetor es: {min(vector)}')

# 2. De los n elementos de un vector dado calcule:
vector2 = []
x = 1
while True:
    numero2 = int(input(f'Digite el número {x} o digite 0 para salir: '))
    if numero2 == 0:
        break
    x += 1
    vector2.append(numero2)
vec1 = []
vec2 = []
def xx(vect):
    for i in vector2:
        if i % 2 == 0:
            vec1.append(i)
        else:
            vec2.append(i)
    respuesta = print(f'Los números pares son: {vec1}\nLos números imprares son: {vec2}')
    return respuesta
        
        
print(f'{xx(vector2)}')

#3. Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de las siguientes operaciones:

v = []
v1 = []
x = 1
while True:
    numero2 = int(input(f'Digite el número {x} o digite 0 para salir: '))
    if numero2 == 0:
        break
    x += 1
    v.append(numero2)
x = 1
while True:
    numero2 = int(input(f'Digite el número {x} o digite 0 para salir: '))
    if numero2 == 0:
        break
    x += 1
    v1.append(numero2)
resultado = []
def sum_vec(v,v1):
    for i in range(len(v)):
        resultado.append(v[i]+v1[i])
    return resultado

print(f'La suma de los vectores es: {sum_vec(v,v1)}')


#4. De los n elementos de un vector dado identifique el número que mas se repite e indique cual es.

vector = []
x = 1
while True:
    numero2 = int(input(f'Digite el número {x} o digite 0 para salir: '))
    if numero2 == 0:
        break
    x += 1
    vector.append(numero2)

def moda(datos):
    repeticiones = 0

    for i in datos:
        n = datos.count(i)
        if n > repeticiones:
            repeticiones = n
        return print(f'El número que mas se repite es: {i} y se repite {repeticiones} veces')

moda(vector)



#5. Dado un Vector v de longitud par, divida en 2 partes, en la primera parte
#realice la productoria y en la segunda la sumatoria. Entregue los valores
#resultantes.

v = []
x = 1
while True:
    numero2 = int(input(f'Digite el número {x} o digite 0 para salir: '))
    if numero2 == 0:
        break
    x += 1
    v.append(numero2)
B = v[:len(v)//2]
C = v[len(v)//2:]

print(f'La productoria de la primera parte es: {produc(B)}, la sumatoria de la segunda mitad es: {sum(C)}')
print(produc(C))


"""6. Dado un vector v, indique si es simétrico, un vector es simétrico si siendo
longitud par los números de la primera mitad son iguales al inverso de la
otra mitad por ejemplo: X=[1,2,3,3,2,1], en el ejemplo x es un vector
simétrico, en caso que la longitud del vector sea impar, se ignorará el
elemento central y se seguirá la misma lógica anterior, por ejemplo:
Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico."""

v = []
x = 1
while True:
    numero2 = int(input(f'Digite el número {x} o digite 0 para salir: '))
    if numero2 == 0:
        break
    x += 1
    v.append(numero2)

B = v[:len(v)//2]
C = v[len(v)//2:]
if B == C:
    print('El vector es simetrico')
else:
    print('El vector no es simetrico')

#7. Dado dos vectores númericos A y B debe realizar las siguiente operaciones con conjuntos:

import copy
    
v = []
v1 = []
g = []
x = 1
while True:
    numero2 = int(input(f'Digite el número {x} o digite 0 para salir: '))
    if numero2 == 0:
        break
    x += 1
    v.append(numero2)
x = 1
while True:
    numero2 = int(input(f'Digite el número {x} o digite 0 para salir: '))
    if numero2 == 0:
        break
    x += 1
    v1.append(numero2)
v2 = copy.copy(v)
v2.extend([element for element in v1 if element not in v])

def intersection(v,v1):
    v3 = []
    for i in v:
        for j in v1:
           if i == j:
               v3.append(i)
    v3 = list(tuple(v3))
    return v3
v4 = []
v4.append([element for element in v if element not in v1])
v5=[]
v5.append([element for element in v1 if element not in v2])
print(f'La union de las listas sin repetir es: {v2}')
print(f'La interseccion de las listas es: {intersection(v,v1)}')
print(f'La diferencia entre el primer vector y el segundo es: {v4}')
print(f'La diferencia entre el segundo vector y el primero es: {v5}')















