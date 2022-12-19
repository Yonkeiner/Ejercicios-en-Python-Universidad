"""Ejercicio 4 Construir un programa que simule el funcionamiento de una calculadora que puede realizar 
las cuatro operaciones aritmeticas basicas (suma, resta, multiplicacion y division). El usuario debe
especificar la operacion con el primer caracter del nombre de la operacion"""

"""S, s - Suma
   R, r - Resta
   P, p, M, m - Multiplicacion
   D, d - Division"""


numUno = float(input("digite un numero"))
numDos = float(input("digite un numero"))

operacion = input("digite la operacion (S)uma, (R)esta, (P)roducto o (M)ultiplicacion y (D)ivision").upper()

if operacion == "S":
    suma = numUno + numDos
    print (f"\La suma es: {suma}")
elif operacion == "R":
    resta = numUno - numDos
    print(f"\La resta es: {resta}")
elif operacion == "P" or operacion == "M":
     multi = numUno * numDos
     print(f"\El producto es: {multi}")
elif operacion == "D":
    division = numUno / numDos
    print(f"\La division es: {division} ")
else:
    print("Usted se equivoco de operacion")