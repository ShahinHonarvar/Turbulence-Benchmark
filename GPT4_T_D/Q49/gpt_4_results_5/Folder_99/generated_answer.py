
def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_109 = fibonacci(109)
    return decimal_number % fib_109 == 0
