"""un dicionario es una estrutura de datos y un tipo de dato 
en pyton con caracteristicas especiales que nnos permite almacenar
cualquier tipo de valor como enteros,cadenas, listas e incluso otras funciones
estos diccionarios nos permiten ademas identificar cada elemento por una clave (key)"""

#lista
lista = ["juan","maria","carlos"]
diccionario ={
    "nombre": "diego",
    "edad" : 25, 
    "profesion": "profesor"}
          
productos = {
    "televisor": 15.000,
    "celular":30.000,
    "portatil":160.000
}

nombres ={"nombre":"carlos","edad":20,"cursos":["python","javascript","nodejs"]}
# print (nombres)
# print (nombres ["nombre"])
# print (nombres["edad"])
# print (nombres["cursos"])
# print (nombres["cursos"][1])

notas_estudiantes ={
    "juan":[2.5,3,4.6],
    "ana": [3.5,4.6,4.9],
    "luis": [4,2.5,3.9]
}
#print(notas_estudiantes["juan"])
#--------------------AGREGARAR DATOS A UN DICCIONARIO------------------------------
"""miDiccionario = {
    "nombre": "sara",
    "edad":30
    }
miDiccionario["profesion"]= "instrutora"
print(miDiccionario)"""

#--------------editar datos de un diccionario---------------
"""miDiccionario["edad"]=31
print(miDiccionario)"""

#--------------eliminar datos de un diccionario-------------

"""miDiccionario = {
    "nombre": "sara",
    "edad":30,
    "profesion": "instrutora"
    }
print(miDiccionario)
prof = miDiccionario.pop("profesion")

print(prof)
print(miDiccionario)"""

#--------------agregar nultiples valores-------------------
miDiccionario = {
    "nombre": "sara",
    "edad":30,
    "profesion": "instrutora"
    }
print(miDiccionario)


nuevosDatos = {
    "cuidad":"cali",
    "documento": 123456,
    "telefono": 2222222
}
print(nuevosDatos)


for clave , valor in nuevosDatos.items():
    miDiccionario[clave]=valor

print(miDiccionario)