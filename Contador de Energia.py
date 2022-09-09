#Contador de Energia
import math 

print("Hola Bienvenido a la calculadora de energia ")
name=input("Ingresa tu nombre")

#Este le preguntara al usuario su nombre y en caso de no ingresar ninguno repetira la pregunta
while name=="":
    name=input("Ingresa tu nombre ")

#Introduce los valores
w=int(input("Ingresa tu peso en kilogramos "))
producto=input("Que alimento quieres comer ")
kC=int(input("Cuantas kiloCalorias tiene tu alimento "))

#funcion para saber si el sujeto es de sexo femenino o masculino
def Genero(kC):
    genero=input("Es usted hombre o mujer H/M ")

    if genero == 'H':
        energiaAlmacenada=((kC*1000)*.80)-8300
        return energiaAlmacenada
    elif genero == 'M':
        energiaAlmacenada=((kC*1000)*.80)-7100
        return energiaAlmacenada
    else:
        print("Favor de Ingresar H si usted es hombre o M si usted es mujer ")
        Genero(kC)

caloriasPorEscalon=w*9.81*.15
resultadoXGenero=Genero(kC)
result=resultadoXGenero/caloriasPorEscalon

print(name ," tu ",producto," hara que almacenes ", resultadoXGenero , " Kilocalorias por lo que tendras que subir ", math.ceil(result)," escalones para quemar tu alimento " )
