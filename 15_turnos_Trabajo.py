#turnos de trabajo
'''
6.	Turnos de trabajo
Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno.
  El jornal diario se paga según:   a) tarifa hora diurna $5.000, b) tarifa hora nocturna $8.000.
   Leído el número de horas diurnas y nocturnas que trabajó un empleado durante el día cuánto
   deberá pagársele si se le debe descontar un 1% si gana más de $30.000 diarios?

'''

def run():
    horas_diurna=float(input("Digite la hora diurna: "))
    horas_nocturnas=float(input("Digite la hora nocturna: "))
    pago_diurno=horas_diurna*5.00
    pago_nocturno=horas_nocturnas*8.00
    total_sin_descuento=pago_diurno+pago_nocturno
    if(total_sin_descuento>30):
        descuento=0.01*total_sin_descuento
        pago_con_descuento=total_sin_descuento-descuento
        print("La cantidad q recibe es: ",pago_con_descuento)
    else:
        print("La cantidad q recibe es: ",total_sin_descuento)


if __name__ == '__main__':
    run()