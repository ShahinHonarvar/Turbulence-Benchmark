
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal_integer = int(binary_representation, 2)
    fibonacci_128th = fibonacci(128)
    
    if decimal_integer % fibonacci_128th == 0:
        return True
    else:
        return False
