numero_romano:str
total=0

romanos={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    
}


#comparo letra por letra, esto haciendo uso del zip, lo que haces es crear pares de letras consecutivas
#numero_romano: "XXVII"
#numero_romano[1:]: "XVII" (elimina el primer carácter)
# [('X', 'X'), ('X', 'V'), ('V', 'I'), ('I', 'I')]
for a,b in zip(numero_romano,numero_romano[1:]):
#Lo que hara el if es comparar los dos pares de letras pero yendose al diccionario (romanos)
  if romanos[a] < romanos[b]:
#Si la primera accion se cumple los resta, sino va a la siguiente accion 
     total-= romanos[a]
#Si no es menor lo suma 
  else:
    total += romanos[a]
#Como es un ciclo for, la iteracion se hacen hasta acabar los valores de la variable inicial (Numero_Romano)

#Esta ultima linea nos ayuda a sumar el utltimo caracter, Explicacion en la parte final
print(total + romanos[numero_romano[-1]])  

#Explicacion penultima linea y asi mismo me explica el porque en la sumas nunca hay un +romano[b]
#numero_romano = "XIV"
#list(zip(numero_romano, numero_romano[1:]))  
# [('X', 'I'), ('I', 'V')]
#Observa que 'V' no aparece como a en ninguna iteración.
#Para asegurarnos de incluirlo, lo sumamos al final.