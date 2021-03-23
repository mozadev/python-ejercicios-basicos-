
'''
9.	Alquiler de automóviles
Una compañía dedicada al alquiler de automóviles cobra un monto fijo de S/. 300 para los primeros 300 Km. de recorrido.
Para más de 300 Km. y hasta 800 Km., cobra un monto adicional de S/.  1.5 por cada kilómetro en exceso sobre 300.
Para más de 800 Km. cobra un monto adicional de  S/. 0.5 por cada kilómetro en exceso sobre 800.
Los precios ya incluyen el 18% del IGV. Diseñe un algoritmo que determine el monto a pagar por el alquiler de un vehículo y el monto incluido del impuesto.

'''
def run():

    km = float(input("Ingresar KM recorridos: "))
    if (km <= 300):
        precio_venta = 300
    elif (km > 300 and km <= 800):
        precio_venta = round(300 + (km - 300) * 1.5, 2)
    else:
        precio_venta = round(300 + 500 * 1.5 + (km - 800) * 0.5, 2)

    igv = round((precio_venta - (precio_venta / 1.18)), 2)
    print("El monto a pagar es de: " + str(precio_venta) + " El IGV es: " + str(igv))

if __name__ == '__main__':
    run()