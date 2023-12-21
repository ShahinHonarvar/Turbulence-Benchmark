
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal_integer = int(binary_representation, 2)
    fibonacci_154th = fibonacci(154)
    
    if decimal_integer % fibonacci_154th == 0:
        return True
    else:
        return False
