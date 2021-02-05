def do(func):
    def wrapper_do(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper_do

@do
def greet(name):
    print(f"Hello {name}")

@do
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


greet("World")
print(return_greeting("Adam"))