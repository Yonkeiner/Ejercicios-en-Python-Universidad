# Hacer un programa que simule un cajero automatico con un saldo inicial de $1000 y tendras 
# el siguiente menu de opciones:

"""1. Depositar dinero en la cuenta 
   2. Retirar dinero de la cuenta 
   3. Consultar saldo disponible
   4. Salir"""

SaldoInicial = 1000

print("\t :: MENU ::")
print("1. Depositar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Saldo disponible")
print("4.Salir")

opcion = int(input("Digite un numero: "))

if opcion == 1:
    DepositoCuenta = float(input("Cuanto dinero va a depositar: "))
    SaldoInicial += DepositoCuenta
    print (f"Usted tiene un saldo de : {SaldoInicial}")
elif opcion == 2:
    RetirarFondos = float(input("Monto a retirar: "))
    if RetirarFondos > SaldoInicial:
        print("Saldo insuficiente")
    else:
        SaldoInicial -= RetirarFondos
        print(f"Saldo en Cuenta {SaldoInicial}")
elif opcion == 3:
    print(f"Monto disponible: {SaldoInicial}")
elif opcion == 4:
    print("Gracias por usar nuestros servicios")
else:
    print("Usted se equivoco de opcion")
