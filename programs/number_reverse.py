num = int(input("Enter a number to reverse: "))

"""
1. The `reversed_num` variable is initialized to 0. This will hold the reversed number.

2. The `while` loop continues as long as `num` is not equal to 0.
   This means it will keep running until all the digits of the number have been processed.

3. Inside the loop, the `remainder` variable is calculated as the remainder of `num` divided
   by 10. This effectively gives the last digit of `num`.

4. The `reversed_num` is then updated by multiplying it by 10 and adding the `remainder.
   This effectively shifts the digits of `reversed_num` to the left and adds the last digit
   of `num` to the right end of `reversed_num`.

5. Finally, `num` is updated by performing integer division by 10.
   This effectively removes the last digit from `num`.

The loop then continues with the next digit of `num`, and so on, until `num` is 0.
At this point, `reversed_num` will hold the reversed number.
"""
reversed_num = 0
while num != 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num = num // 10

print("The reversed number is:", reversed_num)
