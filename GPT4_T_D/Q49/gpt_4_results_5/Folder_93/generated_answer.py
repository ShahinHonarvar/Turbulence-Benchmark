
def if_decimal_is_divisible(bin_string):
    def fibonacci_n(n):
        fib_seq = [0, 1]
        while len(fib_seq) <= n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]

    decimal_num = int(bin_string, 2)
    return decimal_num % fibonacci_n(59) == 0
