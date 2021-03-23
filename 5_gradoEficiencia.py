
#---------------grado de  ediciencia de un operario------------------------
'''
5.	Grado de eficiencia de un operario
Diseñe un algoritmo para obtener el grado de eficiencia de un operario de una fábrica de tornillos, de acuerdo a las siguientes condiciones, que se le imponen para un período de prueba:
Las condiciones son: Menos de 200 tornillos defectuosos y  más de 10000 tornillos producidos. El grado de eficiencia se determina de la siguiente manera:
•	Si no cumple ninguna de las condiciones, grado 5.
•	Si sólo cumple la primera condición, grado 6.
•	Si sólo cumple la segunda condición, grado 7.
•	Si cumple las dos condiciones, grado 8

'''
def run():

     contador5=0
     contador6=0
     contador7=0
     contador8=0

     for i in range(6):
          defi=int(input("Digite el numero de tornillos defectuosos: "))
          prod=int(input("Digite el numero de tornillos producidos: "))
          if((defi>200)and(prod<1000)):
               grado=5
               contador5=contador5+1
          elif((defi<200)and(prod<1000)):
               grado=6
               contador6 = contador6+ 1
          elif((defi>200)and(prod>1000)):
               grado=7
               contador7= contador7 + 1
          elif((defi<200)and(prod>1000)):
               grado=8
               contador8 = contador8 + 1


          print("El grado de eficiencia del operario es "+str(grado))


     print("el numero de operarios con eficiencia 5 es: "+str(contador5))
     print("el numero de operarios con eficiencia 6 es: "+str(contador6))
     print("el numero de operarios con eficiencia 7 es: "+str(contador7))
     print("el numero de operarios con eficiencia 8 es: "+str(contador8))

if __name__ == '__main__':
    run()