
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    dec = int(binary_str, 2)
    fib_24 = fibonacci(24)
    
    return dec % fib_24 == 0
