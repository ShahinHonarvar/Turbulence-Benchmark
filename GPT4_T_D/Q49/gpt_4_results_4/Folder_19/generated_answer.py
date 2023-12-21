
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_sequence = [0, 1]
    for i in range(2, 29):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    if decimal_integer % fib_sequence[28] == 0:
        return True
    else:
        return False
