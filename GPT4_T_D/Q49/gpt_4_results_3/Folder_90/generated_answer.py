
def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a+b
    return a

def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_177th = fibonacci(177)
    return decimal_value % fibonacci_177th == 0
