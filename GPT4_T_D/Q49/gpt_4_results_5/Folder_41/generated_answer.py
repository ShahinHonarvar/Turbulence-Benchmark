
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[len(fib_sequence) - 1] + fib_sequence[len(fib_sequence) - 2])
        return fib_sequence[n]

    decimal_integer = int(binary_string, 2)
    fib_num = fibonacci(67)
    return decimal_integer % fib_num == 0
