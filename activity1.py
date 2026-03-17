def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# First tuple
numbers_tuple1 = (4, 3, 2, 2, -1, 18)
print(numbers_tuple1)
result1 = calculate_product(numbers_tuple1)
print("The product of the numbers in the tuple is:", result1)

# Second tuple
numbers_tuple2 = (2, 4, 8, 8, 3, 2, 9)
print(numbers_tuple2)
result2 = calculate_product(numbers_tuple2)
print("The product of the numbers in the tuple is:", result2)
