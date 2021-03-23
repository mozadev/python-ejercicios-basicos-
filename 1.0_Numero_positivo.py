
# Algoritmo que indica si un número ingresado es positivo, negativo o cero
def run():
    numero = int(input("Ingresar numero: "))
    if (numero > 0):
        print("Positivo")
    elif (numero < 0):
        print("Negativo")
    else:
        print("Es cero")

if __name__ == '__main__':
    run()