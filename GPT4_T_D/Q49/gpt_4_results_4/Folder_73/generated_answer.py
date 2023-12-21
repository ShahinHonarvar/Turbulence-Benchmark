
def if_decimal_is_divisible(binary_string):
    def fibonacci_sequence(n):
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[n - 1]

    decimal_int = int(binary_string, 2)
    fib_number = fibonacci_sequence(164)
    return decimal_int % fib_number == 0
