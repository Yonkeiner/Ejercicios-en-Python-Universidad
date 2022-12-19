#determine cual es el mayor de tres numeros

numUno = int(input("digite un numero: "))
numDos = int(input("digite un numero: "))
numTres = int(input("digite un numero: "))

if numUno >= numDos and numUno >= numTres:
    print(f"el mayor es (numUno)") 
elif numDos >= numUno and numDos >= numTres:
    print(f"el mayor es (numDos)") 
elif numTres >= numDos and numTres >= numUno:
    print(f"el mayor es (numTres)") 

