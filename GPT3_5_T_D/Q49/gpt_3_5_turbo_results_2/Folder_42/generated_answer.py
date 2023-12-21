
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal = int(binary, 2)
    fib_146 = fibonacci(146)
    
    return decimal % fib_146 == 0
