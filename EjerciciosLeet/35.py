nums=int([])
target=int()

#me guarda el primer indice que tengo 
izq=0
#me guarde el ultimo indice que hay en la lista 
dere=len(nums)-1

#Hago un ciclo while con esta condicion que siempre se cumplira
while izq <= dere:

#debo calcular el punto medio para que ciclo sepa si esta a la izquierda o a la derecha de la lista
#con el doble // me da un numero entero y no float 

    medio= (izq+dere)//2

#comparo para ver si de pronto el target esta en el medio
    if nums[medio]==target:
       print (medio)

#comparo si el medio es menor al taget para saber donde buscar el numero 
    elif nums[medio]<target:
#Si esta condicion se cumple debo de sumarle un 1 al medio y que izq cambie su valor 
#de 0 a 1 en esta ocasion, entonces vuelve a hacer el ciclo while 
#asi sucesivamente hasta encontrar un numero <= a target
        izq = medio+1
#si la condicion anterior no se cumple lo que hace el ciclo es  restarle un 1 a dere 
#Lo que seria restarle un 1 al ultimo numero de la lista y asi encontrando donde esta target
#todo mientras se este cumpliendo la condicion del ciclo, sino tomaria que ya tenemos la solucion
    else:
       dere = medio-1

print(izq) 
 
    
