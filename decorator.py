def log(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__} function...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__} function.")
        return result
    return wrapper

@log
def my_function(x, y):
    return x + y

result = my_function(2, 3)
print(result)
