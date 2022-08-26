# ContadorDeEnergia
Con este proyecto podrás calcular la cantidad de energía en Joules  que tu cuerpo almacena y cuantos escalones deberías subir para que hayas eliminado esa energía sobrante de tu organismo este resultado sera personalizado ya que se le preguntara su peso al usuario.

Este proyecto se me hace interesante ya que se me hace maravilloso como el cuerpo humano siempre busca regularse a si mismo ya que por ejemplo una persona con infrapeso tendra que hacer mucho ejercicio para poder quemar enegia acumulada en cambio lo opuesto pasa con una persona con sobrepeso ya que mientras mas masa mueva mas energia quema y tambien para crear conciencia de lo dañinos que son los alimentos chatarra

El algoritmo fluctuaria de la siguiente manera
Entrada
  peso
  kiloJoulesDelAlimento

Proceso
  Pedir peso
  Pedir kiloJoulesDelAlimento
  
  g=9.81
  e=15
  
  #Esto nos dira la cantidad de energia se gasta al subir un escalon
  Epotencial=peso*g*e
  
  #Esto nos dira la cantidad de energia que el cuerpo almacena de un alimento
  kiloJoulesAlmacenados=(kiloJoulesDelAlimento*0.8)-8300
  
  cuantosEscalones = kiloJoulesAlmacenados/Epotencial
  
  imprimir "Tienes que subir" cuantosEscalones "para quemar el alimento que comiste"

Salida
  "Tienes que subir" cuantosEscalones "para quemar el alimento que comiste"
