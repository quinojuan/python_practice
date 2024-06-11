def read_odd_number():
  while True:
    try:
      number = int(input("Introduce an odd number please: "))
      # print(type(number)) si no le pusiera el int obtendria una cadena
      if number % 2 != 0:
        print(f"Thanks! You have just introduced the number: {number}.")
        break
      else:
        print("The number isn't odd. Try again.")
    except ValueError:
      print("That's not a valid entry. Introduce an integer.")
      

# Call function readOddNumber
read_odd_number()