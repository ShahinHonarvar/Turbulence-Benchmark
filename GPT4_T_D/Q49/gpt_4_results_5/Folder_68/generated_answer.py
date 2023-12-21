
def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if decimal_integer % fibonacci_sequence(38) == 0:
        return True
    else:
        return False
