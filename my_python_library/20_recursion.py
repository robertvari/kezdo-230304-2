def call_myself(n):
    print(f"The value of n: {n}")

    if n >= 10:
        return  # early return
    
    call_myself(n+1)  # recursion call

call_myself(0)