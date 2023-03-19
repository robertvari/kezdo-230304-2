import time

def my_timer(decorated_function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = decorated_function(*args, **kwargs)
        print(f"Process time: {time.time() - start_time}")

        return result
    
    return wrapper