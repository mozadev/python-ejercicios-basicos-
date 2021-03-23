
'''
2.	Estacionamiento
En una playa de estacionamiento cobran
 $5 la primera hora y $10 a partir de la segunda hora.
 Diseñe un algoritmo que determine cuánto debe pagar un
 cliente por el estacionamiento de su vehículo, conociendo
 el tiempo de estacionamiento en horas.

'''
def run():

    horas_estacionado=int(input("Digite la cantidad de horas q estara estacionado: "))
    if(horas_estacionado==1):
        cobro=5
    else:
        cobro=5+10*(horas_estacionado-1)

    print("El costo por el tiempo estacionado seria: "+str(cobro))

if __name__ == '__main__':
    run()