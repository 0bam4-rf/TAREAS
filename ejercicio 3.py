# palabra1 = "hola"
# palabra2 = "mundo"
# palabra3 = "python"
# frase = palabra1 + " " + palabra2 + " " + palabra3
# print("la frase completa es ", frase)
#--------------------------------------------------------
#convertir de celsius a farengeis

# celsius = float(input("INGRESE LOS GRADOS CELSIUS"))
# #(0 °C × 9/5) + 32 = 32 °F
# fahrenheit = celsius * 9/5 + 32
# print("la temperatura en grados farenheit", fahrenheit)
#---------------------------------------------------------------
# hallar el area de un rectagunlo
# base = float(input("ingrese el ancho del rectangulo: "))
# altura = float(input("ingrese la altura del rectangulo: "))
# area = base * altura
# print("el area del rectandulo es: ", area)
# import math
#d = (x2 - x1)>2 + (y2 - y1)>2
# x1 = float(input("INGRESE LA CORDENADA X DEL PRIMER PUNTO: "))
# y1 = float(input("INGRESE LA CORDENADA y DEL PRIMER PUNTO: "))

# x2 = float(input("INGRESE LA CORDENADA X DEL SEGUNDO PUNTO: "))
# y2 = float(input("INGRESE LA CORDENADA y DEL SEGUNDO PUNTO: "))

# distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print("la distancia es: ",distancia)
#______________________________________________________
#crea un programa que calcule el monto total despues de aplicar interes compuesto
#el usuario debe ingresr el capital inicial, la tasa de interees anual y el numero de años
#la formula del interes compesto es:
# M = p(1 + r/100)t
# M es monto final
# p capital inicial
# r tasa de interes
# t numero de años

# p = float(input("ingrese el capital inicial: "))
# r = float(input("ingrese la tasa de interes anual: "))
# t = float(input("ingrese los años: "))
# M = p * (1 + r/100)**(t)
# print("EL MONTO AHORRADO ES DE: ",M)
#-----------------------------------------
# texto =input("ingrese su nombre: ")
# mayuscula = texto.upper()#en mayuscula
# minuscula = texto.lower()#en miniscula
# titulo = texto.title()#primera en mayuscula
# print("el texto en mayusculaes: ",mayuscula)
# print("el texto en minuscula: ",minuscula)
# print("el texto en titulo: ",titulo)
#-----------------------------------------------------
#crear un programa que muestre la e+fecha y hora actual en formato
# legible utilizadondo el modulo datatime
# import datetime
# fechaHoraActual = datetime.datetime.now()
# #formato fecha y hora
# fechaFormato = fechaHoraActual.strftime("%d/%m/%Y, %H:%M:%S")
# print("la fecha y hora actual es: ",fechaHoraActual)
#----------------------------------
#escribe un programa en python que genere un numero aleatorio del 1 al 100 utilizando el modulo random
# import random
# numeroAleatorio = random.randint(1, 100)
# print("el numero aleatorio es: ",numeroAleatorio)
#--------------------------------------------

# numero = 5
# if numero >1 :
#     print("es mayor que 1 (uno)")
#------------------
# edad = 16
# altura = 182
# if (edad > 19 and altura > 150): # or es dar una segunda opcion y and es obligatorio cumplir las dos
#     print("puede salir")
# else:
#     print("no pude salir")
#-------------------------------
numero  = 6
if numero < 3 :
    print("es menor que 3 ")
elif numero < 6 :
    print("el numero esta entre 3 y 6")
else:
    print("el numero es mayor o igual a 6")
#---------------------------------
#crear un programa solicitando su edad y decir si es mato de edad

# edad = int(input("ingrese su edad"))
# if edad >= 18:
#     print("USTED ES MAYO DE EDAD")
# else:
#     print("USTED NO ES MAYOR DE EDAD")
#     ------------------------
