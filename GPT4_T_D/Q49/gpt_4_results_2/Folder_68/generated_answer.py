
def if_decimal_is_divisible(bin_string):
    dec_int = int(bin_string, 2)
    fibonacci_38th = fib(38)
    return dec_int % fibonacci_38th == 0

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
