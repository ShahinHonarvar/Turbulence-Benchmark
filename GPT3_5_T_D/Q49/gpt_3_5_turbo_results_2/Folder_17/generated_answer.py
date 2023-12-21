
def if_decimal_is_divisible(decimal):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal_value = int(decimal, 2)
    fibonacci_154 = fibonacci(154)
    return decimal_value % fibonacci_154 == 0
