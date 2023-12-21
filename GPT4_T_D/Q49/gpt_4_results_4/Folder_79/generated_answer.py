
def if_decimal_is_divisible(binary_string):
    def generate_fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n-1]

    decimal_int = int(binary_string, 2)
    thirteenth_fibonacci = generate_fibonacci(13)

    if decimal_int % thirteenth_fibonacci == 0:
        return True
    else:
        return False
