# Accept three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Create a list with the three integers
numbers = [num1, num2, num3]

# Sort the list in ascending order
numbers.sort()

# Display the integers in ascending order
print("Integers in ascending order:", numbers)
