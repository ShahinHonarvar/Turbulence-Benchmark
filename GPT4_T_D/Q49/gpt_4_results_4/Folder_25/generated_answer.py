
def if_decimal_is_divisible(bin_string):
    def fibonacci_series(n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            fib_sequence = [0, 1]
            while len(fib_sequence) < n:
                fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            return fib_sequence[-1]

    num = int(bin_string, 2)
    if num % fibonacci_series(19) == 0:
        return True
    else:
        return False
