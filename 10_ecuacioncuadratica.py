
'''
1.	Ecuacion de segundo grado
Hacer un algoritmo para resolver una ecuación de segundo grado. La ecuación de segundo grado es  ax2 + bx + c = 0 y a ≠ 0. Las soluciones o raíces de la ecuación son:

'''
def run():

    a = float(input("Digite a: "))
    b = float(input("Digite b: "))
    c = float(input("Digite c: "))
    if (a != 0):
        x1 = round((-b) + ((b ** 2 - 4 * a * c) ** (1 / 2)), 2) / 2 * a
        x2 = round((-b) - ((b ** 2 - 4 * a * c) ** (1 / 2)), 2) / 2 * a
        print("La solucion de la ecuacion cuadrada es: " + str(x1) + " y " + str(x2))
    else:
        print("El coeficiente debe ser diferente de cero")

if __name__ == '__main__':
    run()