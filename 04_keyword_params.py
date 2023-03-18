def say_hello(email, name, address):
    print("-"*50)
    print(f"Hello {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print("-"*50)

say_hello(
    address="Pécs",  # keyword parameter
    name="Csaba",
    email="csaba@gmail.com"
)