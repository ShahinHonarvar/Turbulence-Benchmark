
def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n+1):
                a, b = b, a + b
            return b
    
    fibonacci_90th = fibonacci(90)
    
    return decimal % fibonacci_90th == 0
