
def fib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_174th = fib(174)
    return decimal_number % fibonacci_174th == 0
