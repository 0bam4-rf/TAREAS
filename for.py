#sistanxis bucle for
#for variable in.secuencia:
    #bloque de codigo

# for i in range(2,10,5):
#      print(i)
# print("FIN") 
# -----------------------   
# frutas = ["manzana","pera","sadia","banano","piña","fresa","uva"]
# for i in frutas:
#     if i == "pera":
#         print(f"la fruta es {i}")
#         break
# ------------------- 
# numeros = [2,4,6,8,10]
# suma = 0
# for i in numeros:
#     suma += i
# print("la suma total de los elemtos de la lista es: {suma}")
# ------------------------
# Dada una lista de números, escribe un programa 
# en Python que imprima solo los números pares de esa lista.
# numeros = [1,2,3,4,5,6,7,8,9,10]
# for i in numeros:
#     if i % 2 == 0:
#         print(f"numeros pares {i}")
# ---------------        
#programa en pyton para contar la cadena de texto y cuente las vocales
# vocales = ["a", "e", "i", "o", "u"]
# cadena = "bienvenidos a pyton, estamamos aprendiendo a programar"
# contador = 0
# for letra in cadena:
#     if letra in vocales:
#         contador += 1
# print(f"el numero de vocales en el texto son {contador}")
# -----------------------
#Crea un programa en Python que solicite al usuario
#  un número entero y luego genere la tabla de 
# multiplicar de ese número del 1 al 10.
# numero = int (input("escriba un numero"))
# for tabla in range (1,11):
#     print(numero, " x ", tabla, "=", numero * tabla)
#------------------------------------
#for anidado
# for i in range(1,11):
#     for a in range(1,11):
#         print(f"{i} * {a} = {i*a}")
#     print("-" * 20)
# print("salir")    
#---------------------------
#dibujar un  triangulo con ateriscos segun las filas dadas por el usuario

# f = int(input("numero de filas "))
# for i in range (1,f+1):
#     for a in range (i):
#         print("*", end= "")
#     print()    #linea nueva