# Contador de Energia
# Librerias
import math
import datetime as dt

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

#funcion para el nombre del usuario
def Name():
    name=input("Ingresa tu nombre ")
    while name=="":
        #Este le preguntara al usuario su nombre y en caso de no ingresar ninguno repetira la pregunta
        name=input("Ingresa tu nombre ")
    return name

#funcion para saber el peso del usuario
def Weight():
    w=""
    w=int(input("Ingresa tu peso en kilogramos "))
    while w=="":
        w=int(input("Ingresa tu peso en kilogramos "))   
    return w

#funcion para saber la altura del usuario
def Height():
    h=""
    h=float(input("Ingresa tu altura en metros "))
    while h=="":
        h=float(input("Ingresa tu altura en metros "))   
    return h

#funcion para saber que alimento quiere comer el usuario
def Producto():
    producto=""
    producto=input("Que alimento quieres comer ")
    while producto=="":
        producto=input("Que alimento quieres comer ")
    return producto

#funcion para imprimir la matriz donde se encuentra la rutina
def imprimirRutina(rutina):
    for n in range(0, len(rutina)):
        print(rutina[n])

#funcion para saber si el usuario hace ejercicio y decide que clase de rutina quiere el usuario
def hacesEjercicio(intensidad):
    rutina=[[" L  "," M  "," M  "," J  "," V  "],[" EJ "," DE "," EJ "," DE "," EJ "],["EJ = Ejercicio","DE = Descanso"]]
    if intensidad == "1":
        print("Una buena rutina seria:")
        rutina=[[" L  "," M  "," M  "," J  "," V  "],[" EJ "," EJ "," EJ "," EJ "," EJ "],["EJ = Ejercicio"]]
        imprimirRutina(rutina)
        
    elif intensidad=="2":
        print("Te recomiendo practicar al menos 3 horas de ejercicio a la semana")
        print("Una buena rutina seria:")
        imprimirRutina(rutina)
    else:
        print("Selecciona una opcion valida")
        hacesEjercicio(intensidad)

#funcion que contiene el menu
def Menu(name):
    print("Hola" ,name, "Bienvenido a la apliccion que cuida tu salud")
    print("1. Calcular tu IMC")
    print("2. Calcular la cantidad de calorias que absorbe tu cuerpo al comer cierto alimento")
    print("3. Sugiereme una rutina para realizar ejercicio")
    print("4. Dime el historial de mi IMC")
    print("5. Salir")
    print("7. Prueba de Funcionamiento")

#funcion para calcular el IMC del usuario
def calcularIMC(h, w):
    IMC= w/(h*h)
    condicion=""
    if IMC >= 30:
        condicion="Obesidad"
    elif 25 <= IMC and IMC <= 29.9:
        condicion="Sobrepeso"
    elif 18.5 <= IMC and IMC <= 24.9:
        condicion="Normal"
    else:
        condicion="Desnutrido"

    return IMC, condicion

#funcion para calcular la cantidad de energia que gana el usuario al ingerir cierto alimento
def EnergiaGananda(name, w, producto, kC, resultadoXGenero,):
    caloriasPorEscalon=w*9.81*.15
    result=resultadoXGenero/caloriasPorEscalon
    print(name ," tu ",producto," hara que almacenes ", resultadoXGenero , " Kilocalorias por lo que tendras que subir ", math.ceil(result)," escalones para quemar tu alimento " )

def main():
    name=Name()
    
    historialImc=[]
    date=dt.date.today()
    while True:
        Menu(name)
        menu=input("Selecciona el indice de la actividad que quieras realizar. 1-5 ")
        if menu == "1":
            h=Height()
            w=Weight()
            IMC, condicion=calcularIMC(h, w)
            print("Tu IMC es de", round(IMC,2) ,"lo que significa que tu condicion es de ",condicion )
            historialImc.append(name)
            historialImc.append(IMC)
            historialImc.append(date.year)
        
        elif menu=="2":
            w=Weight()
            producto=Producto()
            kC=int(input("Cuantas kiloCalorias tiene tu alimento "))
            resultadoXGenero=Genero(kC)
            EnergiaGananda(name, w, producto,kC, resultadoXGenero)
        
        elif menu=="3":
            intensidad=input("¿Prefieres una rutina de ejercicio intensa o relajada? 1=Intensa, 2=Relajada")
            hacesEjercicio(intensidad)

        elif menu=="4":
            if len(historialImc) == 0:
                print("No tienes historial de IMC")
                print("")
            else:
                print(name, "tu IMC de manera cronologica ha sido de (IMC, año)")
                print(historialImc)
                print("")

        else:
            break

main()

def prueba():
    name="DUMMY"
    historialImc=["John Doe", "27.8","2010"]
    date=dt.date.today()

    #Menu
    Menu(name)
    print(" ")

    
    #Calcula Tu IMC
    
    #Entrada
    h=1.80
    w=90
    
    #Salida Esperada
    #tu IMC es de 27.78 lo que significa que tu condicion es de sobrepeso
    IMC, condicion=calcularIMC(h,w)
    print("tu IMC es de", round(IMC, 2), "lo que significa que tu condicion es de ", condicion)
    historialImc.append(name)
    historialImc.append(round(IMC, 2))
    historialImc.append(date.year)
    print("")

    #Valores Ingresados/Calculados
    w=90
    producto="Manzana +"
    kC=90

    #resultadoXGenero se calcula de la siguiente formula en este caso se asume que el usuario es Hombre
    #((kC*1000)*.80)-8300
    resultadoXGenero=63700
    
    #resultado esperado 
    #DUMMY tu Manzana + hara que almacenes  63700  Kilocalorias por lo que tendras que subir  481  escalones para quemar tu alimento
    EnergiaGananda(name, w, producto,kC, resultadoXGenero)
    print("")


    #Creador de Rutina de Ejercicio
    intensidad="1"

    #Resultado Esperado 
    #Una buena rutina seria:
        #[' L  ', ' M  ', ' M  ', ' J  ', ' V  ']
        #[' EJ ', ' EJ ', ' EJ ', ' EJ ', ' EJ ']
        #['EJ = Ejercicio']
    #Este utiiza una matriz para  crear una estadistica 2D
    hacesEjercicio(intensidad)
    print("")

    #Checar historial de IMC
    print(name, "tu IMC de manera cronologica ha sido de (IMC, año)")
    
    #Resultado Esperado
    #DUMMY tu IMC de manera cronologica ha sido de (IMC, año)
    #['John Doe', '27.8', '2010', 'DUMMY', 27.78, 2022]
    print(historialImc)
    print("")



prueba()
