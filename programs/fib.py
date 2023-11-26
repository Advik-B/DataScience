
# Define the number of terms in the series
num_terms = int(input("Enter the number of terms of the series you want: "))

# Initialize the first two terms
a, b = 0, 1

# Print the first two terms
print(a)
print(b)

# Generate and print the remaining terms
for _ in range(num_terms - 2):
    a, b = b, a + b
    print(b)
