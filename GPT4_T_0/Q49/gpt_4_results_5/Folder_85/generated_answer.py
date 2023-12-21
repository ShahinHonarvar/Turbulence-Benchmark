
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_number = int(binary_string, 2)
    fibonacci_45th = fibonacci(45)

    if decimal_number % fibonacci_45th == 0:
        return True
    else:
        return False
