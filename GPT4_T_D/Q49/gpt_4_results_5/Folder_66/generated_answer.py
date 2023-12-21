
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib_120 = fibonacci(120)
    return decimal % fib_120 == 0
