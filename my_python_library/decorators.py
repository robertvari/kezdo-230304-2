import time
import logging
from datetime import datetime

def my_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Process time: {time.time() - start_time}")

        return result
    
    return wrapper

def check_temperature(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1000:
            print(f"<WARNING> Temperature is too high: {result}")

        return result
    
    return wrapper

def login_check(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            logging.basicConfig(filename="server_log.txt", level=logging.INFO)
            logging.info(f"Date:{datetime.now()} user logged in")
        else:
            logging.basicConfig(filename="server_log.txt", level=logging.WARNING)
            logging.warning(f"Date:{datetime.now()} invalid login attempt")

        return result
    
    return wrapper