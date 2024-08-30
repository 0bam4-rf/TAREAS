"""
utiliza un diccionario para gestionar el inventario de una tienda de frutas
implementaremos las funciones para agregar nuevas frutas
al invetario, actulizar cantidades, eliminar frutas y mostrar el inventario
"""

# frutas = {"mango": 10,
#           "manzanas": 15,
#           "pera": 8
#           }

# print (frutas)
# #---------

# nuevaFrutas = {"naranja" : 15,
#                "banano": 12
#                } 
# frutas.update(nuevaFrutas)
# print(frutas)

# #----------
# cantidad =input("ingrese la cantidad: ")
# frutas ["pera"]=cantidad

# print (frutas)

# #-------
# frutasEliminadas =["mango", "banano"]
# for fruta in frutasEliminadas:
#     if fruta in frutas:
#         del frutas[fruta]
#         print(f"{fruta} se elimino")
#     else:
#         print(f"{fruta} no se encontro en la lista")    

# print("**********inventario final**********")
# for fruta,cantidad in frutas.items():
#     print(f"{frutas}: {cantidad} unidades")

# print (f"inventario final{frutas}")   
# 
# ---------------------------------------------------------------
"""gestion de calificcacion de estudiantes
supongamos que tenemos un grupo de estudiantes y quieres 
almacenar sus calificaciones en un dicciionario. luego puedes 
agregar nuevas calificaciones, actulizar las existentes y eliminar
estudiantes del registro
"""
# estudianes = {"juan": [4,2.5,4],
#               "luis": [5,3,3.9],
#               "sara": [4,4,4]
#               }
# #------
# estudianes["juan"].append(4.5) 
# estudianes["luis"].append(3.8)
# estudianes["sara"].append(5)
# #-----
# estudianes["juan"][1]=3.5
# #----
# del estudianes ["luis"]

# for lista, nota in estudianes.items():
#     print(f"{lista}: {nota}")
#-----------------------------------------------------------
"""
gestion de inventario de productos
el usuario podra

agreagar un nuevo producto o actulizar la cantida
eliminar un producto
mostrar el invetario actual
solicitar los datos al usuario
"""
invetario = {}
print("¿QUE OPCION DESEA REALIZA?")
print("AÑADIR PRODUCTO (1)")
print("ELIMINAR PRODUCTO (2)")
print("MOSTRAR INVENTARIO (3)")
opcion = str(input("INGRESE UNA OPCION: "))
while True:
   if opcion == "1":
    dato = input("ingrese el producto:  ")
    cantidad = input("ingrese la cantidad:  ")
    invetario[dato] = cantidad
    print(invetario)
   elif opcion == "2":
     print(f"{invetario} ELIGA LO QUE VA A ELIMINAR")
     
           

