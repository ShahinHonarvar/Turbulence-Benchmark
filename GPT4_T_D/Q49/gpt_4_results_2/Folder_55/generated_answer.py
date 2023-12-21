
def if_decimal_is_divisible(bin_str):
    dec_num = int(bin_str, 2)
    fib_39 = fib(39)
    return dec_num % fib_39 == 0

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
