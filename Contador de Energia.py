#Contador de Energia
import math 

print("Hola Bienvenido a la calculadora de energia ")
w=int(input("Ingresa tu peso en kilogramos "))
producto=input("Que alimento quieres comer ")
kC=int(input("Cuantas kiloCalorias tiene tu alimento "))

energiAlmacenada=((kC*1000)*.80)-8300
caloriasPorEscalon=w*9.81*.15

result=energiAlmacenada/caloriasPorEscalon

print("Tu ",producto," hara que almacenes ", energiAlmacenada , " Kilocalorias por lo que tendras que subir ", math.ceil(result)," escalones para quemar tu alimento " )
