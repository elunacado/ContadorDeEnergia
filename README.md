# ContadorDeEnergia
Con este proyecto podrás calcular la cantidad de energía en Joules que tu cuerpo almacena y cuantos escalones deberías subir para que hayas eliminado esa energía sobrante de tu organismo , calcular tu IMC, obtener rutinas de ejercio para la semana y recibir el historial de tu IMC.

Este proyecto se me hace interesante ya que se me hace maravilloso como el cuerpo humano siempre busca regularse a si mismo ya que por ejemplo una persona con infrapeso tendra que hacer mucho ejercicio para poder quemar enegia acumulada en cambio lo opuesto pasa con una persona con sobrepeso ya que mientras mas masa mueva mas energia quema y tambien para crear conciencia de lo dañinos que son los alimentos chatarra ademas de que México esta en el 5to lugar de obesidad infantil por lo que el conocimiento del IMC de cada persona deberia ser de conocimiento de cada persona junto con el como esta deberia ejercitarse para mejorar su salud.

El algoritmo fluctuaria de la siguiente manera
Entrada
  Decision del Usuario
    -Calcular IMC
    -Calcular la cantidad de Joules que recibe tu cuerpo por cierto alimento
    -Producir a rutina de ejercicio
    -Pedir historial
Proceso
    -Calcular IMC
      -Pedir peso
      -Pedir altura
      -peso/altura^2
    -Calcular la cantidad de Joules
       -Pedir kJ del alimento
       -Pedir peso del usuario
       donde: 
       g=9.81
         e=15
    -Producir rutina
       -Pedir la intensidad de la rutina 
    -Pedir historial
       -Leer el historial del IMC
 
  
  #Esto nos dira la cantidad de energia se gasta al subir un escalon
  Epotencial=peso*g*e
  
  #Esto nos dira la cantidad de energia que el cuerpo almacena de un alimento
  kiloJoulesAlmacenados=(kiloJoulesDelAlimento*0.8)-8300
  
  cuantosEscalones = kiloJoulesAlmacenados/Epotencial
  
  imprimir "Tienes que subir" cuantosEscalones "para quemar el alimento que comiste"

Salida
  -"Tu IMC es de: "
  -"Tienes que subir" cuantosEscalones "para quemar el alimento que comiste"
  -Rutina de ejercicio
  -Historial
