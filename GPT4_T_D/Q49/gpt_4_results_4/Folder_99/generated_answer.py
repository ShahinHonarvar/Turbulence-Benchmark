
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib_109 = fibonacci(109)
    return decimal % fib_109 == 0
