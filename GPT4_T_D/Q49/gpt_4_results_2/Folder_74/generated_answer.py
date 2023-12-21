
def if_decimal_is_divisible(binary_string):
    def fibonacci_index(n):
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < n:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        return fibonacci_sequence[n - 1]

    decimal_number = int(binary_string, 2)

    if decimal_number % fibonacci_index(166) == 0:
        return True
    else:
        return False
