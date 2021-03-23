#Ejemplo 2 baterial durasol
'''
4.	Bateria “Durasol”
En la empresa de Batería “Durasol” se ha establecido una promoción de las baterías” para los negocios que se dedican a la venta de batería, dicha promoción consiste en lo siguiente:
	Si se compran menos de cinco baterias el precio es de S/. 300 cada una, de S/. 260 si se compran de cinco a 10 y de S/. 210 si se compran más de 10.

	Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las baterías que compra y la que tiene que pagar por el total de la compra.

'''
def run():

    cantida_baterias=int(input("Ingrese numero de baterias: "))
    if(cantida_baterias<5):
        total=300*cantida_baterias
    elif(cantida_baterias<=10):
        total=260*cantida_baterias
    else:
        total=210*cantida_baterias
    print("Total a pagar: "+str(total))

if __name__ == '__main__':
    run()