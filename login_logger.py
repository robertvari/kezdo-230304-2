from my_python_library.decorators import login_check

@login_check
def login(username, password):
    local_username = "robert"
    local_password = "testpas123"

    if local_username == username and local_password == password:
        print(f"You are logged in {username}. Wellcome back.")
        return True
    else:
        print("Invalid username or password")
        return False

login("robert", "testpas123")