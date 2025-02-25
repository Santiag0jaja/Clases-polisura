import pprint

""" Diccionarios en python y sus metodos """

dvacio: dict = {}
dinicializado = {"llave: ": "valor", "edad": 18.5}
print(type(dinicializado), dinicializado)

"""Forma permitida para acceder a un diccionario"""
print(dinicializado["edad"])

"""Forma no permitida"""
# print(dinicializado.edad)

"""Accediendo a un diccionario que no existe"""
#print(dinicializado["digame_el_futuro"])

"""Metodo Get: acceder a un diccionario de manera segura sin generar excepcion"""
print(dinicializado)
print(dinicializado.get("Digame_el_futuro", "muestra que no se encuentra la llave"))

"""Cuando si existe la llave"""
print(dinicializado.get("edad", True))

"""Metodo Keys: Nos permite conocer las llaves del diccionario (Solo las llaves de primer nivel)"""
print(dinicializado.keys())
print(list(dinicializado.keys()))

"""Metodo values: nos permite obtener los valores de cada unba de las llaves"""
print(dinicializado.values())
print(list(dinicializado.values()))

"""Metodo items: nos permite separar cada llave-valor en una lista de otros elementos"""
print(dinicializado.items())
items = list(dinicializado.items())
print(items)
print(items[0])
print(items[0][0])

elemento_1, elemento_2 = list(dinicializado.items())
print("Elemento 1:", elemento_1)
print("Elemento 2:", elemento_2)

"""Asignacion: asignamos valores a las llaves en el diccionario"""
dinicializado["python_nivel"] = 1
print(dinicializado)

dinicializado["python_nivel"] = 2
print(dinicializado)

"""Metodo pop: elimina el item de la llave especificada"""
print(dinicializado)
#dinicializado.pop('llave')

"""Metodo copy: nos entrega una copia exacta del diccionario al que se le aplico el metodo"""
copia_a = dinicializado.copy()
copia_b = dinicializado.copy()
print("Copia A: ", copia_a)
print("Copia B: ", copia_b)

"""Metodo update: nos permite concatenar diccionarios"""
a_concatenar: dict = {"nombre": "Joaquin"}
print(a_concatenar["nombre"])
print("antes", copia_a)
copia_a.update(a_concatenar)
print("despues", copia_a)

""" Metodos de concatenar utilizando metodos de ** o"""
"""KEY ARCS / KARGS:"""
"""ARGS:"""

dic_concat_kargt: dict = {**copia_b, **a_concatenar}
print(dic_concat_kargt)

"""Metodo Popitem: Nos devuelve el item que elimina"""

llave, valor = dic_concat_kargt.popitem()
print("Llave eliminada: ", llave, " Valor eliminado de la llave: ", valor)
print(dic_concat_kargt)

"""Metodo Clear: nos elimina todos los valores del dict"""
print("Antes: ", dic_concat_kargt)
dic_concat_kargt.clear()
print("Despues uwu: ", dic_concat_kargt)


dict_datos_per: dict = {}
dict_datos_per = {
    "nombre": "pepito",
    "apellidos": "perez",
    "estado_civil": "soltero",
    "fecha_nacimiento": "01/01/2000",
    "genero": "masculino",
    "tipo_sangre": {
        "rh": "+",
        "grupo_sanguineo": "AB"
    }

}

pprint.pprint(dict_datos_per)

datos_contacto = {
    "nombre": "Juan Pérez",
    "edad": 25,
    "email": "juan.perez@example.com",
    "teléfono": "+57 312 345 6789",
    "dirección": {
        "calle": "Calle 123",
        "ciudad": "Medellín",
        "país": "Colombia"
    },
    "redes_sociales": {
        "Instagram": "@juanperez",
        "Twitter": "@jperez"
    }
}

dict_datos_per["datos de contacto"] = datos_contacto
pprint.pprint(dict_datos_per)
print("LLegando a niveles: ", dict_datos_per["datos de contacto"]["dirección"]["calle"])

dict_cedula: dict = {}
dict_cedula["12345678"] = dict_datos_per
pprint.pprint(dict_cedula)


