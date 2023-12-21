
def if_decimal_is_divisible(decimal):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return (fibonacci(n-1) + fibonacci(n-2))

    fibonacci_80 = fibonacci(80)
    decimal_integer = int(decimal, 2)

    if decimal_integer % fibonacci_80 == 0:
        return True
    else:
        return False
