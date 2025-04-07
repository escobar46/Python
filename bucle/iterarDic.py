diccionario={
    'nombre':'brandon',
    'apellido':'escobar',
    'altura':1.70
}
#Recorriendo el diccionario para obtener las claves 
for key in diccionario:
    key
    print(f'la clave es: {key}')
    

#Recorriendo el diccionario con items() para obtener las claves y los valores 

for datos in diccionario.items(): 
    key= datos[0]
    value=datos[1]
    print(f'la clave es: {key} y el valor es: {value}')
    
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #I me sirve para el indice, que me lo da range(lem(nums))
        for i in range(len(nums)):
            #i+1 me serviria para que no compare el mismo numero dos veces
            for j in range(i + 1, len(nums)):
                #Aca lo que hago es encontrar el numero necesario para igualar el target 
                if nums[j] == target - nums[i]:
                    return [i, j]
    #Si no hay target que coincida me devolveria esto 
        return []
    
romanos={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    
}

numero_romano="XII"
total=0

for letra in numero_romano:
    total+=romanos[letra]
    
print(total)