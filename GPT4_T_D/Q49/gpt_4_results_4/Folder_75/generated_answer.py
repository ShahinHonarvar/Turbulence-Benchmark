
def fib(n): 
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib_189th = fib(189)
    return decimal % fib_189th == 0
