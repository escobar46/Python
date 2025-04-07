diccionario={
    "nombre":"brandon",
    "apellido":"escobar",
    "altura":1.70
}

#nos devuelve un objeto dict_item (tipo de objeto que se puede iterar)
claves= diccionario.keys()

#Obtenemos un elemento get() si este no encuentra nada, el programa continua
valor=diccionario.get("nombre")

#elimina todos los elementos del diccionario 
eliminar=diccionario#.clear()

#elimina un elemento del diccionario 
diccionario.pop("altura")

#obteniendo un elemento dic_items iterable 
diccionario_iterable=diccionario.items()

print(diccionario_iterable)