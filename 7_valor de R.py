
'''
7.	Elaborar un algoritmo que calcule el valor de R de acuerdo a la siguiente relación:
R = (A * B) / (C * D) Si X * Y > 0
R = (A + B) / (C + D) Si X * Y = 0
R = (A + B) – C + D Si X * Y < 0

'''
def run():

    a = float(input("Digite el valor de a: "))
    b = float(input("Digite el valor de b: "))
    c = float(input("Digite el valor de c: "))
    d = float(input("Digite el valor de d: "))
    x = float(input("Digite el valor de x: "))
    y = float(input("Digite el valor de y: "))
    if (x * y > 0):
        resultado = (a * b) / (c * d)
    elif (x * y == 0):
        resultado = (a + b) / (c + d)
    else:
        resultado = (a + b) - c + d

    print("El valor de R es: " + str(resultado))

if __name__ == '__main__':
    run()