 
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        a, b = 0, 1 
        for _ in range(n-1):
            a, b = b, a + b
        return b
    decimal = int(binary_str, 2)
    fibonacci_number = fibonacci(87)
    return decimal % fibonacci_number == 0
