
def if_decimal_is_divisible(bin_str):
    def fibonacci_numbers(n):
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < n:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        return fibonacci_sequence

    decimal_repr = int(bin_str, 2)
    fib_138 = fibonacci_numbers(139)[-1]

    if decimal_repr % fib_138 == 0:
        return True
    else:
        return False
