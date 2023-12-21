
def if_decimal_is_divisible(bin_repr):
    fib_seq = [0, 1]
    while len(fib_seq) < 105:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal = int(bin_repr, 2)
    return decimal % fib_seq[103] == 0
