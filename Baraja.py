# Modulos necesarios
import itertools, random

# Creacion del mazo
mazo = list(itertools.product(range(1,12),['Espadas','Bastos','Copas','Oros']))
# Barajar las cartas
random.shuffle(mazo)

#Muestra tu mano para la proxima jugada
print("||Tu mano||")
print("----------------------")
for i in range(7):
   if i == 1 :
      print("As de",mazo[i][1])
   elif i == 10 :
      print("Sota de", mazo[i][1])
   elif i == 11:
      print("Caballo de", mazo[i][1])
   elif i == 12:
      print("Rey de", mazo[i][1])
   else:
      print(mazo[i][0], "de", mazo[i][1])
print("----------------------")