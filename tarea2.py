#Escribe un programa en Python que 
# use un bucle while para calcular 
# el factorial de un número ingresado
#  por el usuario. El factorial de un
#  número n es el producto de todos los
#  números enteros positivos menores o 
# iguales a n (es decir, n! = n * (n-1) * (n-2) * ... * 1).
factorial = 1
i = 1
numero = int (input("ingrese un numero "))
while i <= numero:
    factorial = factorial * i
    i = i + 1

print(f"el factorial de{numero} es, ",str (factorial))
