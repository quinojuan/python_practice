#creando tuplas con tuple()
# tupla = tuple(["dato1", "dato2"])

# print (tupla)

# monster = "mostro1", "mostro2"

# print(monster)

# Teoria de conjuntos

conjunto1 = {1,2,3,8,9}
conjunto2 = {1,8,9}

# verificando si es un subconjunto utilizando dos alternativas
# result = conjunto2.issubset(conjunto1)
result = conjunto2 <= conjunto1

print(result)
