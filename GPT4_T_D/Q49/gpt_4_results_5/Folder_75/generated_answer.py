
def if_decimal_is_divisible(binary_string):
    decimal_repr = int(binary_string, 2)

    def get_nth_fibonacci(n):
        fib_seq = [0, 1]
        while len(fib_seq) < n + 1: 
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]

    if decimal_repr % get_nth_fibonacci(189) == 0:
        return True
    else:
        return False
