# frutas =["manzana","pera","uvas","banano"]#strn
# numeros = [89, 78, 65 ,78, 56]
# frutas.append("sandia")#agregar elementos a las listas al final
# frutas.insert(0,"piña")#agregar un elemento en una posicion especifica
# frutas.extend(["mango","kiwi","lulo"])#agregar multiples elementos
# frutas[5] = "limon" #editar un elemento de la lista
# frutas.remove("pera")#remover un elemento
# del frutas [7]# eliminar un elemento de la lista, con el numero del elemento
# del frutas [2:4]#eliminar por rango del 2 al 4
# frutas.clear() #eliminar todo de la lista
# # frutasEliminadas = frutas.pop(0)#saca de la lista al elemento seleccionado y lo agrega a una variable
# print(frutas)
# # print(frutasEliminadas)
#----------------------------------------------

#Escribe un programa en Python que permita al usuario crear una lista de compras. El programa debe solicitar al usuario que ingrese el nombre de los productos uno por uno y los agregue a la lista. Una vez que el usuario haya terminado de agregar productos, el programa debe imprimir la lista completa de compras en orden.

# Requisitos:

# El programa debe permitir al usuario ingresar 
# productos hasta que decida detenerse.
# Después de ingresar cada producto, el usuario
#  debe ser preguntado si desea agregar otro producto.
# Si el usuario decide que no quiere agregar más productos,
#  el programa debe mostrar la lista completa de compras.

# lista = []
# while True:
#     produtos = [input("ingrese los produto ")]
#     lista.append(produtos)
#     si = input("quiere eliminar otro producto? (si / no)")
#     if si == "no":
#      break
#     print("sus compras son ",lista)
# print(f"sus prductos son ", lista)

# eliminar = print("desea eliminar un producto? (si / no)")
# if eliminar == "si":
#     while True:
#         produtos = [input("ingrese los produto a eliminar ")]
#         lista.append(produtos)
#         si = input("quiere agregar otro producto? (si / no)")
#         if si == "no":
#             break
#         print("sus compras son ",lista)
#--------------------------------------
#Escribe un programa en Python que solicite
# al usuario ingresar una lista de números enteros. 
# Luego, el programa debe calcular e imprimir la
#  suma de todos los números ingresados. El programa debe
#  continuar solicitando números hasta que el usuario decida 
# dejar de ingresar más.

# Requisitos:

# El programa debe permitir al usuario ingresar números uno por uno.
# Después de ingresar cada número, el usuario debe ser preguntado 
# si desea agregar otro número.
# Si el usuario decide que no quiere agregar más números, 
# el programa debe calcular y mostrar la suma total de los
#  números ingresados.

lista = []
while True:
    n = int (input("ingrese un numero "))
    lista.append(n)
    si = input("desea seguir agregando numeros? (si / no)")
    if si == "no":
        break
suma = sum(lista)    
print(f"f los numeros a sumar son {lista}") 
 
print(f"la suma es {suma}") 

