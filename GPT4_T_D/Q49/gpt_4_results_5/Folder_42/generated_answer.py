
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_integer = int(binary_representation, 2)
    fibonacci_146th = fibonacci(146)
    
    if decimal_integer % fibonacci_146th == 0:
        return True
    return False
