
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    decimal_integer = int(binary_string, 2)
    fibonacci_number = fibonacci(115)
    
    return decimal_integer % fibonacci_number == 0
