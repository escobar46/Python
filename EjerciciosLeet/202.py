# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.



def happy_number(n):
    #Variable que introduce el codigo
    #n=2
    #Variable para guardar los datos, con el set() me da para que nunca se repita un numero
    #nos hace que el while quiebre si hay un numero repetido que tiene un ciclo infinito y nunca da 1 
    vistos=set()

    #con este ciclo lo que hacemos es que se repita mientras el codigo arroje diferente de 1 
    while n!=1: 
        
        #aca, lo que hace es que como estamos en un ciclo, todos los valores (que arroje) los vamos a ir guardando en vistos 
        #si llegase a haber uno repetido lo que hace el ciclo es  romperse
        if n in vistos: 
            return False

        #aca ponemos lo que hace es agregar n(los numersos que vayan saliendo en vistos)
        vistos.add(n)
        
        #no estan entegrando un entero que para compararlo y desglozarlo debemos de mandarlo en string(texto) y de ahi a int(entero)
        #para que haga las sumas, los exponentes etc
        digitos = [int(d) for d in str(n)]
        
        
        #aca, hago un variable para ir sumando los resultados y luego volver a repetir los pasos hasta tener 1 o que se rompa el ciclo (False)
        sumado=0
        #con este ciclo lo que hago es separar uno por uno los enteros 
        for e in digitos :
            #elevo los digitos uno por uno 
            elevado=e**2 
            #sumo luego los digitos elevados 
            sumado += elevado
        #actualizo n para que haga el while de nuevo 
        n=sumado
    #si el ciclo se cancela o se quiebra, lo que hace esta linea es comparar para dar 1 

    if n == 1: 
        return True      


n=101
print(happy_number(n))