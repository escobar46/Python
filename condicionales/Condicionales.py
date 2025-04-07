edad=14

if edad >=18:
    print("podes pasar") 
else :
    print("vuelve cuando seas mayor")
    
Ingreso_mensual = 100000
Gasto_mensual=7000

# If anidados y else if (elif)

if Ingreso_mensual > 1000:
    
    if Ingreso_mensual-Gasto_mensual <0:
        print("Estas en deficit")
    
    elif Ingreso_mensual- Gasto_mensual >3000:
        print("Para ahorrar")
    
    else: 
        print("Hay que mirar que hay si te alcanza para fin de mes") 

elif Ingreso_mensual > 10000:
     print("estas bien en el mundo")

else: 
    print("estas pobre") 