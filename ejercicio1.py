#-Determinar-si-dos-numeros-son-pares

numUNO = int (input( "digite un numero: ="))
numDOS = int (input( "digite un numero: ="))

if numUNO %2 == 0 and numDOS %2 == 0:
    print ("Ambos numeros son pares")
elif numUNO %2 == 0 and numDOS %2 != 0:
    print(f"{numUNO} es par")
elif numUNO %2 != 0 and numDOS %2 == 0:
     print(f"{numDOS} es par")
else: 
    print ("Ambos numeros son impares")