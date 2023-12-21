
def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fib_seq = fibonacci_sequence(74)
    if decimal % fib_seq[-1] == 0:
        return True
    else:
        return False

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
