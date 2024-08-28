#--------------------EJERCICIO 2-----------------------------------------------
"""Escribe un programa en Python que solicite al usuario ingresar una lista de números enteros.
Luego, el programa debe calcular e imprimir la suma de todos los números ingresados. 
El programa debe continuar solicitando números hasta que el usuario decida dejar de ingresar más.
Requisitos:
El programa debe permitir al usuario ingresar números uno por uno.
Después de ingresar cada número, el usuario debe ser preguntado si desea agregar otro número.
Si el usuario decide que no quiere agregar más números, el programa debe calcular y mostrar 
la suma total de los números ingresados."""
# lista = []
# while True:
#     n = int (input("ingrese un numero "))
#     lista.append(n)
#     si = input("desea seguir agregando numeros? (si / no)")
#     if si == "no":
#         break
# suma = sum(lista)    
# print(f"f los numeros a sumar son {lista}") 
 
# print(f"la suma es {suma}") 



#-----------------------------EJERCICIO 3--------------------------------------------------
"""Escribe un programa en Python para gestionar una lista de contactos. 
El programa debe permitir al usuario realizar las siguientes operaciones:

Agregar un contacto a la lista, incluyendo un nombre y un número de teléfono.
Eliminar un contacto de la lista especificando el nombre del contacto.
Mostrar todos los contactos en la lista, con el formato "Nombre: Número de teléfono".
El programa debe mostrar un menú con las opciones disponibles y seguir funcionando hasta 
que el usuario elija salir. Asegúrate de manejar situaciones en las que el usuario intente
eliminar un contacto que no está en la lista y que el programa informe adecuadamente al usuario.

Requisitos:
El programa debe permitir al usuario ingresar contactos con un nombre y un número de teléfono.
Debe ser posible eliminar un contacto buscando por el nombre.
Debe mostrar todos los contactos en la lista en un formato claro.
El programa debe seguir ejecutándose hasta que el usuario decida salir."""

contatos = []
contato = []

print(f"sus contactos son {contatos}")

while True:
   print("¿QUE OPCION DESEA REALIZA?")
   print("AÑADIR CONTACTO (1)")
   print("ELIMINAR CONTACTO  (2)")
   print("MOSTRAR LISTA DE CONTACTOS (3)")
   print("SALIR (4)")
   opcion = str(input("INGRESE UNA OPCION: "))

   if opcion == "1":

      nombre = str (input("ingrese el nombre: "))
      telefono = str (input("ingrese el numero de telefono: "))
      contato = nombre + ":"  + telefono
      contatos.append(contato)
      print("CONTACTO AGREGADO")
      print(f"{contatos}")      
   elif opcion == "2":
        nombre = (input("ingrese el nombre: "))  
        contatos.remove(nombre)
        print("CONTACTO ELIMINADO")
        print(f"SU LISTA DE CONTACTOS ES: {contatos}")
   elif opcion == "3":
       #print (contatos) 
       for i in (contatos):
           print(i)  
   elif opcion == "4":
       break
   else:
    print("INGRESE UNA OPCION CORRECTA")

for i in (contatos):
    print(i)



#---------------------------EJERCICIO 4------------------------------------------------------------------
"""Escribe un programa en Python que permita al usuario crear una lista de sus películas favoritas.
El programa debe permitir al usuario realizar las siguientes acciones:

Agregar una película a la lista.
Eliminar una película especificando su nombre.
Mostrar todas las películas en la lista.
Buscar si una película específica está en la lista.
El programa debe ofrecer estas opciones en un menú y continuar funcionando hasta que el usuario decida salir."""

#---------------------------EJERCICIO 5------------------------------------------------------------------
