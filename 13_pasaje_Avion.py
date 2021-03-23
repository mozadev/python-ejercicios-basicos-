
'''
4.	Valor de un pasaje de avión
Haga un algoritmo que permita determinar el precio de un
pasaje en avión sabiendo: la distancia a recorrer, valor
por kilómetro recorrido ($47), sobre los 1000 km de vuelo
el valor del kilómetro es de $25.

'''
def run():
    recorrido=float(input("Digite la distancia: "))
    valor_recorrido=47
    valor_recorrido_mayor1000=25
    if(recorrido>1000):
        adicional=(recorrido-1000)*25
        base=1000*valor_recorrido
        total=adicional+base
    else:
        total=recorrido*valor_recorrido


    print("El precio es: "+str(total))


if __name__ == '__main__':
    run()