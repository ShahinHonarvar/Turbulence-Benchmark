
def if_decimal_is_divisible(bin_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    decimal = int(bin_string, 2)
    fib_59 = fibonacci(59)
    
    if decimal % fib_59 == 0:
        return True
    else:
        return False
