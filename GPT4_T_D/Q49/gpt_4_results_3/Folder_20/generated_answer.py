
def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)

    def fibonacci_sequence(n):
        a, b = 0, 1
        while n:
            yield a
            a, b = b, a + b
            n -= 1

    fibonacci_numbers = list(fibonacci_sequence(100))

    return decimal_num % fibonacci_numbers[-1] == 0
