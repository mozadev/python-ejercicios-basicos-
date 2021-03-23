#Factura de venta
'''
3.	Factura de venta
Hacer un algoritmo que permita emitir la factura correspondiente
 a una compra de un artículo del cual se adquieren una o varias
  unidades y se conoce su precio antes de  IGV. El IGV es del 18%
   y si el precio bruto (precio venta mas IGV) es mayor de $50.00
    se debe realizar un descuento del 5%.

'''
def run():

    cant=int(input("Digite la cantidad: "))
    pv=float(input("Digite el precio de venta: "))
    igv=round((18/100)*pv,2)
    pb=pv+igv
    precio_sin_descuento=round(cant*pb,2)
    print("El igv es: "+str(igv))
    if(pb>50):
        precio_con_descuento=precio_sin_descuento*(95/100)
        print("El precio bruto es "+str(precio_con_descuento))
    else:
        print("El precio bruto es "+str(precio_sin_descuento))

if __name__ == '__main__':
    run()