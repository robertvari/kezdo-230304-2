def calculate_result(a, b):
    def add_numbers():
        return a+b

    def multipy_numbers(value):
        return value * b

    def divide_numbers(value):
        return value / b

    add_result = add_numbers()
    multiply_result = multipy_numbers(add_result)
    final_result = divide_numbers(multiply_result)

    return final_result


final_result = calculate_result(10, 301)
print(final_result)