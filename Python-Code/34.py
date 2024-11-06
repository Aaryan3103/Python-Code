## Write a python program to check and display all the armstrong numbers in a given range

def is_armstrong(number):
    # Convert number to string to easily iterate over each digit
    digits = str(number)
    # Calculate the length of the number
    power = len(digits)
    # Sum each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** power for digit in digits)
    # Check if the sum is equal to the original number
    return armstrong_sum == number

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for number in range(start, end + 1):
        if is_armstrong(number):
            armstrong_numbers.append(number)
    return armstrong_numbers

# Example usage
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

armstrong_numbers = find_armstrong_numbers(start_range, end_range)
print(f"Armstrong numbers between {start_range} and {end_range} are: {armstrong_numbers}")
print("THIS PROGRAM IS WRITTEN BY Aaryan :- 0221BCA163")