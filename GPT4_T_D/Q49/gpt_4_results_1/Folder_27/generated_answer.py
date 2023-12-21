
def if_decimal_is_divisible(bin_string):
    def fib(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) <= n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]

    decimal = int(bin_string, 2)
    eighty_seventh_fib = fib(87)
    return decimal % eighty_seventh_fib == 0
