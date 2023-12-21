
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    dec_int = int(binary_str, 2)
    fib_195th = fibonacci(195)
    
    return dec_int % fib_195th == 0
