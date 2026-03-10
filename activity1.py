def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
numbers_tuple = (4,3,2,2,-1,18)
print(numbers_tuple)
result = calculate_product(numbers_tuple)
print("The product of the numbers in the tuple is:", result)

def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
numbers_tuple2 = (2,4,8,8,3,2,9)
print(numbers_tuple)
result = calculate_product(numbers_tuple)
print("The product of the numbers in the tuple is:", result)
