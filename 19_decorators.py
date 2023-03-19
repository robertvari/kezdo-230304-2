import time, random
from my_python_library.decorators import my_timer, check_temperature


@my_timer
def add_numbers(a, b):
    print(f"add_numbers started. a: {a} b:{b}")
    time.sleep(random.randint(1, 5))
    print("add_numbers finished.")

    return a+b

@my_timer
def say_hello(name, email, addres, phone):
    time.sleep(random.randint(1, 5))
    print(name, email, addres, phone)

@check_temperature
def set_temperature(a):
    return a**a

