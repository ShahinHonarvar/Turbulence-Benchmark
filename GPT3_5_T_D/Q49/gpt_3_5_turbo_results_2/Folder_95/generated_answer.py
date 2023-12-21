
def if_decimal_is_divisible(binary):
    fib_seq = [0, 1]
    while len(fib_seq) < 169:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal = int(binary, 2)
    return decimal % fib_seq[168] == 0
