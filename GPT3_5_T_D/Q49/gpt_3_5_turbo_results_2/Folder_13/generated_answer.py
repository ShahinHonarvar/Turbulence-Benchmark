
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = fibonacci(174)
    return decimal_integer % fibonacci_number == 0
