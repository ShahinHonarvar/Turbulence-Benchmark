
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_sequence = [0, 1]
    fib = 1
    while fib <= decimal:
        fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(fib)
    if decimal % fib_sequence[159] == 0:
        return True
    else:
        return False
