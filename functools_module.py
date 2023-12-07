from functools import partial
def power(x, y):
    return x ** y
power_of_2 = partial(power, 2)
print(power_of_2(3))  
print(power_of_2(1))

from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Calculate the product of all numbers using reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1 * 2 * 3 * 4 * 5)

from functools import cache
@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output: 55
print("________________")
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling decorated function")
        return func(*args, **kwargs)
    return wrapper
@my_decorator
def example_function():
    """This is an example function"""
    pass
print(example_function.__name__)  # Output: example_function
print(example_function.__doc__)   # Output: This is an example function


