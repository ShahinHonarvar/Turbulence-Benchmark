
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal_int = int(binary_str, 2)
    fibonacci_69 = fibonacci(69)
    
    if decimal_int % fibonacci_69 == 0:
        return True
    else:
        return False
