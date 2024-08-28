#bucles
# dia = 0
# semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

# while dia < 7:
#     print("Hoy es: ", semana[dia])
#     dia += 1
#-------
# contador = 1
# while contador <= 5:
#     print(contador)
#     contador += 1 #contador = contador + 1

# contador = 0
# while contador <= 5:
#     contador = contador +1
#     print("iteracion numero ",contador)
    #---------------------------------
# contador = 0
# while contador < 15:
#     contador += 1
#     print("iteracion ",contador)
#     if contador == 3:
#         break
# print("fin del programa")
#------------------------------------------
# Escribe un programa en Python que use un 
# bucle while para sumar números ingresados
#  por el usuario hasta que se ingrese un número negativo.
#  Luego, muestra la suma total.
# suma = 0
# while True:
#     numero = int(input("ingrese el numero (para salir ingrese un negativo) "))
#     if numero < 0:
#         break
#     suma += numero
#     print("la suma va en: ",suma)
# print("la suma total es: ",suma)    
#-----------------------------------------
# Escribe un programa en Python que utilice un bucle 
# while para encontrar y mostrar el primer número 
# divisible por 7 en el rango del 1 al 100.
# numero = 4
# while numero <= 100:
#     if numero % 7 == 0:
#         print("el numero divisible por 7 en el rango del 1 al 100 son: ",numero)
#         break
#     numero += 1
#----------------------------------------------
#'''Escribir un programa que solicite ingresar
#  10 notas de alumnos y nos informe
# cuántos tienen notas mayores o iguales a 7 y cuántos menores.

# notasMayores = 0
# notasBaja = 0
# i = 1
# while i <= 10:
#     nota = float(input(f"Ingrese la nota {i}: "))
#     if nota >= 7 and nota <=10:
#         notasMayores += 1
#     else:
#         notasBaja +=1
#     i += 1            

# print("la cantidad de notas altas son: ",notasMayores)
# print("la cantidad de notas bajas son: ",notasBaja)
#----------------------------------
# progrm de un contador donde se cuente de forma 
# desendente desde 10 segundos

# bomba = 10

# while bomba > 0:
#     print("falta ",bomba)
#     bomba -= 1
# print("BOMMMM")
#---------------------------
#Árbol de navidad en Python.
#  Imprime un árbol de navidad formado 
# con * haciendo uso del while y de la 
# multiplicación de un entero por una cadena,
#  cuyo resultado en Python es replicar la cadena.

# z = 7
# x = 1
# while z > 0:
#     print(" "* z + "*" * x + "" *z)
#     x +=2
#     z -=1
#----------------
import math

def factorizar(n):
    factores = []
    # Dividimos n por 2 mientras sea divisible por 2
    while n % 2 == 0:
        factores.append(2)
        n = n // 2

    # Probamos con los números impares desde 3 hasta la raíz cuadrada de n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factores.append(i)
            n = n // i

    # Si queda un factor primo mayor que la raíz cuadrada de n
    if n > 2:
        factores.append(n)
    
    return factores

# Ejemplo de uso
numero = 5
factores = factorizar(numero)
print(f"Los factores primos de {numero} son: {factores}")
