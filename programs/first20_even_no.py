
# BEGIN: Display first 20 even numbers
count = 0
number = 2

while count < 20:
    print(number)
    number += 2
    count += 1

# Can also be done using a for loop

# Reset the count and number variables
number = 2
for count in range(20):
    print(number)
    number += 2
