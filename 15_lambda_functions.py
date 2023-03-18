add_numbers = lambda a, b: a+b
multiply_numbers = lambda a, b: a*b
divide_numbers = lambda a, b: a/b

add_result = add_numbers(100, 41)
multiply_result = multiply_numbers(add_result, 20)
final_result = divide_numbers(multiply_result, 300)
print(final_result)