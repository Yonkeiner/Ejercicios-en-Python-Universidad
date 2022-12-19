# Determine si un caracter es una vocal

LetraEsVocal = input ("Digite un caracter: ").lower()

if LetraEsVocal == "a" or LetraEsVocal == "e" or LetraEsVocal == "i" or LetraEsVocal == "o" or LetraEsVocal =="u":
    print(f'{LetraEsVocal} es vocal')
else:
    print(f"{LetraEsVocal} no es vocal")