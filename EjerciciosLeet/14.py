strs = ["flower","flow","flight"]

primer_palabra=strs[0]


#aca estoy comparando uno a uno cada palabra con la primera, si la primera no inicia igual a la siguiente no tenemos nada 
for palabra in strs[1:]:
    
#Lo que le estoy diciendo aca es que si una palabra no empieza con el prefijo (flor), elimina la ultima letra
#un ejemplos seria, el prefijo (flor) la siquiente palabra es flotar, entonces lo que hace es eliminar la "r" 
# esto para que mire cual es el prefijo mas comun 

    while not palabra.startswith(primer_palabra):
        primer_palabra = primer_palabra[:-1]
        if primer_palabra == "":
            print("") 
            
print(primer_palabra)


