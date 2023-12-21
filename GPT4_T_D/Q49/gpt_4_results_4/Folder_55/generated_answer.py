
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a
    
    if decimal_number % fibonacci(39) == 0:
        return True
    else:
        return False
