
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_94th = fib(94)
    return decimal % fibonacci_94th == 0
