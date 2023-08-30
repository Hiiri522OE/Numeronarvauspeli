import random
print("Numeronarvauspeli")

numero = random.randint(1,9)
arvaus = int(input("Arvaa numeroa väliltä 1-9:"))
  
while True:
    
    if arvaus < numero:
      print("Valitsit liian pienen numeron.")
      arvaus = int(input("Arvaa uudestaan: "))
      
    elif arvaus > numero:
      print("Valitsit liian suuren numeron.")
      arvaus = int(input("Arvaa uudestaan: "))
      
    else:
      print("KYLLÄ, NUMERO ON ")
      print(numero)
      break
