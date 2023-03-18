def add_numbers(a, b):
    return a+b

def multiply_numbers(a, b):
    return a*b

def divide_numbers(a, b):
    return a/b

add_result = add_numbers(10, 4)
multiply_result = multiply_numbers(add_result, 7)
final_result = divide_numbers(multiply_result, 300)

print(f"The final result is: {final_result}")