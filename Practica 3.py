import math

radio_cono= float(input("ingrese el radio del cono: "))
altura_cono=  float(input("ingrese la altura del cono: "))
gerenatriz_cono=  float(input("ingrese la generatriz del cono: "))

area_base= math.pi*radio_cono**2
area_lateral= math.pi * radio_cono * gerenatriz_cono
area_total= area_base + area_lateral
volumen= (area_base * altura_cono)/3 

print ("")
print ("el area base es:",area_base)
print("el area lateral es:",area_lateral)
print("el area total es :",area_total)
print("el volumen es:",volumen)
