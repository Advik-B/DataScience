
n = int(input("Enter a number: "))
num = n
sum_ = 0

# calculate the sum of the cubes of each digit
while num > 0:
    digit = num % 10
    sum_ += digit ** 3
    num //= 10

# check if the sum is equal to the original number
if n == sum_:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
