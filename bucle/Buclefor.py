
nums=[1,2,3,4,5]
animales=["perro","gato","loro","cocodrilo"]

#recorriendo la lista animales
for animal in animales:
    print(f'ahora la variable a animal es , {animal}')

#recorre la lista nums y los multiplica por
for multipli in nums:
    resultado = multipli *10
    print(f'los resultados son {resultado}')
    

#recorrer dos listas al mismo tiempo 
for numero, animale in zip(nums, animales): 
    print(f'recorriendo lsita 1 {numero}')
    print(f'recorriendo lista 2 {animale}')

#recorrer una lista de con la funcion range   
for num in range (5,10):
    print(num)


#Esta es la funcion que vamos a utilizar para desarrollar el primer ejercicio en leet

#for numer in range (len (nums)):
 #   print(nums(numer))
    
    
#Forma diferente de recorrer una lista 

for numss in enumerate(nums):
    #Como enumerate nos entrega una tupla lo que hacemos es separarlos para ver el valor
    indice= numss[0]
    #El valor estaria en la segunda posicion
    valor=numss[1] 
    print(f'el indice es: {indice} y el valor es {valor}')
    
