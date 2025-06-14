
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    decimal = int(binary, 2)
    fibonacci_39 = fibonacci(39)
    
    return decimal % fibonacci_39 == 0
