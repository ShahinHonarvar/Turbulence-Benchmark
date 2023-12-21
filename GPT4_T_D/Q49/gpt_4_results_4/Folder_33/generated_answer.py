
def if_decimal_is_divisible(binary_string):
    def fibonacci_sequence(n):
        a = b = 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    fibonacci_numbers = list(fibonacci_sequence(134))
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_numbers[-1] == 0
