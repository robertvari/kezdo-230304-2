import random, time, threading

def add_numbers(a, b):
    print(f"add_numbers started: a: {a} b: {b}")
    time.sleep(random.randint(1, 10))
    print("add_numbers finished.")

    return a+b

def multiply_numbers(a, b):
    print(f"multiply_numbers started: a: {a} b: {b}")
    time.sleep(random.randint(1, 10))
    print("multiply_numbers finished.")

    return a*b



t1 = threading.Thread(target=add_numbers, args=[10, 4])
t2 = threading.Thread(target=multiply_numbers, args=[3, 6])

t1.start()
t2.start()