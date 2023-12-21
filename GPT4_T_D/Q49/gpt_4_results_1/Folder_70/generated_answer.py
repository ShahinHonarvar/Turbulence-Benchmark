
def if_decimal_is_divisible(binary_string):
    fib_seq = [0, 1]
    while len(fib_seq) < 138:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal = int(binary_string, 2)
    if decimal % fib_seq[137] == 0:
        return True
    else:
        return False
