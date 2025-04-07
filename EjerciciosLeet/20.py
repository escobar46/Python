brackets = {
    "(": ")",
    "{": "}",
    "[": "]"}

print(brackets.values())        # dict_values([')', '}', ']'])

#Lo que hace esto es que valida que si haya esto en el diccionario (valores)
print(")" in brackets.values())
