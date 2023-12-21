
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def if_decimal_is_divisible(bin_str):
    dec_int = int(bin_str, 2)
    fib_num = fibonacci(134)
    return dec_int % fib_num == 0
