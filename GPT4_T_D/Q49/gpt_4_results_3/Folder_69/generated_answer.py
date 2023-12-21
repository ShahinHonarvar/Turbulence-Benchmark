
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) <= n:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        return fibonacci_sequence[n]

    number_in_decimal = int(binary_string, 2)
    return number_in_decimal % fibonacci(170) == 0
