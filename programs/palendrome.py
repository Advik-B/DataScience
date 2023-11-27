s = input("Enter a string: ")

# Initialize the reversed string
reversed_str = s[::-1]
if s == reversed_str:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

