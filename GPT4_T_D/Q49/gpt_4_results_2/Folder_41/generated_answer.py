
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_number = int(binary_string, 2)
    fibonacci_67th = fibonacci(67)
    
    if decimal_number % fibonacci_67th == 0:
        return True
    else:
        return False
