
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [fibonacci(i) for i in range(20)]
    return decimal_integer % fibonacci_sequence[18] == 0
