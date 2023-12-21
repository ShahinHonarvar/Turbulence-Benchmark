
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    decimal = int(binary_string, 2)
    fibonacci_13 = fibonacci(13)
    
    return decimal % fibonacci_13 == 0
