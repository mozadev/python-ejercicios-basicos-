#------------------------determina si es  capicua para mas de dos cifras--------------------

'''
1.	Diseñe un algoritmo que lea un número de tres cifras y determine
 si es o no capicúa. Un número es capicúa si es igual al derecho y
 al revés del número
'''
def run():

    n = int(input("Digite el numero: "))

    if n>=0:
        if str(n)==str(n)[::-1]:
            print('%i es capicua.'% n)
        else:
            print('%i no es capicua.' % n)

    else:
        print('el numero debe ser positivo')

if __name__ == '__main__':
    run()

# # Numero capicua
# n = int(input("Digite el numero: "))
# cn = n;
# d3 = cn % 10
# cn = cn // 10
# d2 = cn % 10
# cn = cn // 10
# d1 = cn % 10
# resul = d1 + d2 * 10 + d3 * (10 ** 2)
# if (resul == n):
#     print("El numero si es capicua")
# else:
#     print("No es capicua")



# Numero capicua

