
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = fib(108)
    return decimal % fibonacci == 0
