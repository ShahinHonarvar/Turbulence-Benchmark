
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a

    decimal_integer = int(binary_string, 2)
    fibonacci_number = fibonacci(143)
    
    return decimal_integer % fibonacci_number == 0
