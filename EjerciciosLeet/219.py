def containsNearbyDuplicate(nums, k):
#El dicionario lo utilizo para guardar los numeros que vea en la lista y los guardo por indice con (i)
    vistos = {}

#Ejemplo range(len([1,2,3,1])) es range(4) → i = 0, 1, 2, 3
#Si pusiera a imprimir esta linea lo que nos daria es que (i) es el indice y (nums [i]) es el valor, 
#ya que colocando nums[i] busca el indice en nums y el diccionario le da el valor 
    for i in range(len(nums)):

#Aqui guardamos el valor de nums dependiendo del indice que salga en este caso i
        num = nums[i]

#Aca busca en vistos, si hay un numero igual dos veces.
#si lo hay hace la ejecucion 
        if num in vistos:

#Lo que hace abs es darme la resta de los indices, pero siempre me la dara en positivo
#abs no importa la posicion de los numero siempre entrega positivo 

            if abs(i - vistos[num]) <= k:
                return True
            
            
#aca lo que hace es poner la variable num en el diccionario, lo almacena y a la vez con (i) ponemos el indice
#la primera iteracion de esta lista [1,2,3,1] seria seria algo asi vistos[num]=i > vistos[1]=0
#siendo 1 el valor y 0 el indice y los guardaria en el diccionario vistos 
        vistos[num] = i

    return False