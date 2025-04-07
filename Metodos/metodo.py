cadena1= "Hola  soy Brandon"
cadena2="Bienvenido12maquina"
cadena3= "hola, soy, brando"
#convierte a mayusculas 
Mayus = cadena1.upper()

#Convierte a minuscula
Minus = cadena1.upper()

#convierte la primera en mayuscula 
PrimMayu= cadena1.capitalize()

#busca una de cadena de otra cadena, en este caso nos daria indice 3
#sino hay concidencia devuelve -1 
Busqueda= cadena1.find("a")
print(Busqueda)

#Buscamos una cadena de otra cadena, si no hay concidencias lanza una exepcion 
Busqueda_index= cadena1.find("H")

#Si es numerico devuelve True 
Numerico = cadena1.isnumeric()
print(Numerico)

#Si alfanumerico devuelve True 
Alphanumerico= cadena2.isalpha()
print(Alphanumerico)

#Buscamos una cadena de otra caddena, devuelve la cantidad de veces coincidad 
Contar= cadena1.count("a")
print(Contar)

#Contamos cuantos caracteres hay en una cadena tiene una cadena 
contar_cadena= len(cadena1)
print(contar_cadena)

#verifica si una cadena empieza con otra cadena dada, si es asi devuelve true
empienza_con= cadena1.startswith("H")
print(empienza_con)

#verifica si una cadena empieza con otra cadena dada, si es asi devuelve true
termina_con= cadena1.endswith("H")
print(termina_con)

#Reemplaza un pedazo de la cadena dada por otro 
cadena_nueva=cadena1.replace("la","lu")
print(cadena_nueva)

#Split nos va a separar con la cadena que la pasemos, nos mostraria una lista 
cadena_split=cadena3.split(",")
print(cadena_split)