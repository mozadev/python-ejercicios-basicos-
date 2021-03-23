'''
5.	Comisión sobre ventas
Una empresa desea conocer el monto de comisión correspondiente
a una venta realizada por un vendedor bajo las siguientes condiciones.
 Si la venta es menor a $1,000.00, se le otorga el 3% de comisión.
 Si la venta es de $1,000.00 o más, el vendedor recibe el 5% de comisión

'''


def run():
    #comision sobre ventas
    monto=float(input("Digite el monto: "))
    if(monto<1000):
        comision= monto * (3 / 100)
    else:
        comision= monto * (5 / 100)

    print("El monto de comision es: " + str(comision))

if __name__ == '__main__':
    run()