
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number % fib(186) == 0
