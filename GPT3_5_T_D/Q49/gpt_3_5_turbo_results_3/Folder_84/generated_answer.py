
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal_integer = int(binary_representation, 2)
    fibonacci_196th = fibonacci(196)
    
    return decimal_integer % fibonacci_196th == 0
