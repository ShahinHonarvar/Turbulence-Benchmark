
def if_decimal_is_divisible(binary_rep):
    fib_sequence = [0, 1]
    idx = 1
    while idx < 134:
        fib_sequence.append(fib_sequence[idx] + fib_sequence[idx - 1])
        idx += 1
    decimal_int = int(binary_rep, 2)
    if decimal_int % fib_sequence[134] == 0:
        return True
    else:
        return False
