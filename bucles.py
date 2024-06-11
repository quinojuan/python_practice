animals = ["dog", "cat", "parrot", "cocodrile"]

for animal in animals:
  print(f"La variable animal vale: {animal}")
  

numbers = [100,15,45,85]

# for number in numbers:
#   result = number * 5
#   print(f"the {number} number * 5 is equal to: {result}")
  
# iterando dos listas al mismo tiempo.
for number, animal in zip(numbers, animals):
  print(f"lista 1:{number}")
  print(f"lista 2:{animal}")
  
# forma no optima de recorrer una lista
for num in range(len(numbers)):
  print(numbers[num])
  
# forma correcta de recorrer una lista con su indice
for num in enumerate(numbers):
  index = num[0]
  value = num[1]
  print(f"the index is: {index} and the value is: {value}")