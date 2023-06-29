import time

def time_taken(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time}")
        return result
    return wrapper

@time_taken
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)