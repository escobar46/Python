Num=(int(input("Ingresar grados: ")))
Grado=(input("Es fahrenheit(F) o Celsius (C): "))

if Grado==("F") :
    resul= (Num-32)*(5/9)
    print(f'Este es el resultaod en Celsius: {resul} C')
elif Grado==("C"):
    resul=(Num*(9/5))+32
    print(f'Este es el resultaod en Fahrenheit: {resul} F')
else: 
    print("escala incorrecta")