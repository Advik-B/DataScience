s = input("Enter a string: ")

# Split the string into a list of characters
# "hello" -> ["h", "e", "l", "l", "o"]
# "pratibha" -> ["p", "r", "a", "t", "i", "b", "h", "a"]
L_s = list(s)

new_string = ""

for element in L_s:
    if element.isupper():
        new_string += element.lower()

    elif element.islower():
        new_string += element.upper()

    elif element.isdigit():
        new_string += '@'

    else:
        new_string += '0'

print(new_string)
