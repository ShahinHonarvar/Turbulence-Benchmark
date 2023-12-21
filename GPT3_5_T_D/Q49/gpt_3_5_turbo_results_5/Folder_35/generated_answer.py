
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return (fibonacci(n-1) + fibonacci(n-2))

    decimal_num = int(binary_string, 2)
    fibonacci_num = fibonacci(187)

    if decimal_num % fibonacci_num == 0:
        return True
    else:
        return False
