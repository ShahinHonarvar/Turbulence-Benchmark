
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n - 1]
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fibonacci(76) == 0
