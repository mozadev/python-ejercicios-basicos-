#Anemia
'''
8.	Laboratorio de análisis clínicos
Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos,
un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su resultado como positivo y en caso contrario como negativo. La tabla en la que el medico se basa para  obtener el resultado es la siguiente:
EDAD                                              NIVEL  HEMOGLOBINA
0 – 1 mes                                                 13 – 26 g%
> 1 y < = 6 meses                                 10 – 18 g%
> 6 y < = 12 meses                              11 – 15 g%
> 1 y < = 5  años                                   11.5 – 15 g%
> 5 y < = 10 años                                 12.6 – 15.5 g%
> 10 y < = 15 años                                13 – 15.5 g%

'''
def run():
    edad = int(input("Digite su edad(en meses): "))
    sexo = input("Digite el sexo: ")
    nivel = int(input("Digite su nivel de hemoglobina: "))
    if (edad > 0 and edad <= 1 and nivel < 13):
     r=1
    elif (edad > 1 and edad <= 6 and nivel < 10):
     r=1
    elif (edad > 6 and edad <= 12 and nivel < 11):
     r=1
    elif (edad > 12 and edad <= 60 and nivel < 11.5):
     r=1
    elif (edad > 60 and edad <= 120 and nivel < 12.6):
     r=1
    elif (edad > 120 and edad <= 180 and nivel < 13):
     r=1
    else:
     r=0

    if r==1:
     print("positivo: tiene anemia")
    if r==0:
     print("negativo: no tiene anemia")


if __name__ == '__main__':
 run()




