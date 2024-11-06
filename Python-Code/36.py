#wap in py to demonstrate try and except 
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
   print("Error: Invalid input. Please enter a valid number.")
print("THIS PROGRAM IS WRITTEN BY Aaryan :- 0221BCA163")