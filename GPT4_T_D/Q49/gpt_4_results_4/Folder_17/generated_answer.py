
def if_decimal_is_divisible(bin_string):
    def fib_154():
        fib_sequence = [0, 1]
        while len(fib_sequence) < 154:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]

    num = int(bin_string, 2)
    return num % fib_154() == 0
