
def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib_198 = fib(198)
    if decimal % fib_198 == 0:
        return True
    else:
        return False
