cadena1 = "haga la salsa salada"
cadena2 = "Coming soon!"

#devuelve el indice del caracter que encuentra. Si no encuentra nada -1
cadena_find = cadena1.find("soy")

#devuelve el indice del caracter que encuentra. Si no encuentra nada tira un ERROR
# cadena_index = cadena1.index("Hola")

#si es numerico devuelve true or false
isnumeric = cadena1.isnumeric()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")

# averiguar longitud de una cadena
longitud = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada:
empieza_con = cadena1.startswith("0")

# reemplazar cadena1 x cadena2 (si no lo encuentra devuelve valor actual)
cadena_nueva = cadena1.replace("moncho", "produzca")

#separar cadenas con la cadena que le pasemos
nueva_lista = cadena1.split(" ")

print(nueva_lista)