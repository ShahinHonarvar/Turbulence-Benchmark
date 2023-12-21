
def if_decimal_is_divisible(binary_string):
    def fibonacci_sequence(n):
        if n <= 1:
            return n
        else:
            return (fibonacci_sequence(n-1) + fibonacci_sequence(n-2))

    fibonacci_28th = fibonacci_sequence(28)

    decimal_integer = int(binary_string, 2)

    if decimal_integer % fibonacci_28th == 0:
        return True
    else:
        return False
