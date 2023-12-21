
def if_decimal_is_divisible(bin_string):
    def fibonacci(n):
        if n<=0:
            return 0
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]

    fib_118 = fibonacci(118)
    decimal_integer = int(bin_string, 2)
    return decimal_integer % fib_118 == 0
