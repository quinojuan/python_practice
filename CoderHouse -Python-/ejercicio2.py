def leer_numeros_y_calcular_promedio():
  while True:
    try:
      cantidad = int(input("¿Cuántos numeros quieres introducir?"))
      if cantidad > 0:
        break
      else:
        print("Por favor, introduce un numero mayor que 0.")
    except ValueError:
      print("Eso no es un numero válido. Por favor, introduce un numero entero.")
    
  numeros = []
  for i in range(cantidad):
    while True:
      try:
        numero = float(input(f"Introduce el número {i+1}: "))
        numeros.append(numero)
        break
      except ValueError:
        print("Eso no es un numero válido. Por favor, introduce un numero entero.")
  
  promedio = sum(numeros) / cantidad
  print(f"El promedio de los {cantidad} numeros introducidos es: {promedio}")
  
# Llamar a la funcion para ejecutar el programa
leer_numeros_y_calcular_promedio()