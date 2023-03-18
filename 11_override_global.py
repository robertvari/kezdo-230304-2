NAME = "Csaba"

def say_hello():
    print(f"Hello {NAME}")

def change_name(new_name):
    global NAME
    NAME = new_name

change_name("Kriszta")
say_hello()