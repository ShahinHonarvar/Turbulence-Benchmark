
def if_decimal_is_divisible(decimal):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    fibonacci_126th = fibonacci(125)

    decimal_int = int(decimal, 2)

    return decimal_int % fibonacci_126th == 0
