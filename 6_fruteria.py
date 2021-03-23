
'''
6.	La frutería “La Jugosa” ofrece las naranjas con descuento según la siguiente tabla:
NUM. DE KILOS COMPRADOS      % DESCUENTO
0 – 2                                                0%
2.01 – 5                                           10%
5.01 – 10                                         15%
10.01 en adelante                           20%
Determinar cuánto pagara una persona que compre naranjas en la frutería “La Jugosa”
'''

def run():

    cantidad=float(input("Digite la cantidad: "))
    precio=float(input("Digite el precio: "))
    if(cantidad<=5):
        total=cantidad*precio*0.90
    elif(cantidad<=10):
        total=cantidad*precio*0.85
    else:
        total=cantidad*precio*0.80
    print("el precio total es: "+str(total))

if __name__ == '__main__':
    run()