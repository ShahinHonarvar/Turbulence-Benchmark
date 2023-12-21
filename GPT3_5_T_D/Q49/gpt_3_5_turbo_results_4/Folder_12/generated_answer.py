
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal = int(binary, 2)
    fibonacci_66 = fibonacci(66)
    
    return decimal % fibonacci_66 == 0
