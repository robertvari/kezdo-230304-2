def say_hello(name, email=None, address=None, phone=None):
    print("-"*50)
    print(f"Hello {name}")
    
    if email:
        print(f"Email: {email}")
    
    if address:
        print(f"Address: {address}")

    if phone:
        print(f"Phone: {phone}")

    print("-"*50)

say_hello(
    name="Csaba", 
    phone="0620 1234 567",
    email="csaba@gmail.com"
)