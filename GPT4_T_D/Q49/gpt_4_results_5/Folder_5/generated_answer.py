
def if_decimal_is_divisible(binary_string):
    
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    decimal_number = int(binary_string, 2)
    fib_85 = fibonacci(85)
    
    return decimal_number % fib_85 == 0
