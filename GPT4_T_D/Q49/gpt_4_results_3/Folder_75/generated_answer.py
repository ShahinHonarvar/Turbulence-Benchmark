
def fib(n):
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]


def if_decimal_is_divisible(bin_string):
    decimal_integer = int(bin_string, 2)
    fibonacci_number = fib(189)
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False
