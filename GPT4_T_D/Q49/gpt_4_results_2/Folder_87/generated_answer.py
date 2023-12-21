
def if_decimal_is_divisible(binary_repr):
    fib_seq = [0, 1]
    for _ in range(178):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
    decimal = int(binary_repr, 2)
    if decimal % fib_seq[180] == 0:
        return True
    else:
        return False
