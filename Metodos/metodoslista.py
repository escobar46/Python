#crea una lista
lista=list(["hola","como estas",12 ])
lista2=[12,2,3,4,6,1,2]
#devuelve cantidad de elememtos de una lista
cantidad_elementos=len(lista)

#agregando un elemento a la lista
lista.append("brandon")

#Agrega un elemento a la lista en un indice en especifico
lista.insert(2,"VAL")

#agregando varios elementos a la lista 
lista.extend([False,2020])

#elimina un elemento de la  lista
#si le pongo -1 me eliminaria el ultimo, si me voy a -2 elimina el penultimo
#y asi sucecivamente 
lista.pop(0)

#remove remueve un elemento por su valor 
lista.remove(2020)


#Elimina todos los elementos de la lista 
#lista.clear()

#ordena la lista de forma ascendente, si usamos reverse=True lo ordena en reversa
lista2.sort()
#lista2.sort(reverse=True)

#Invierte los elementos de una lista 
lista.reverse()

#verifica si un elemento esta en la lista
elemento_encontrado=lista.index(12)

print(elemento_encontrado)
print(lista)
print(lista2)




