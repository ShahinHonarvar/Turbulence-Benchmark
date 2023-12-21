
def if_decimal_is_divisible(bin_str):
    fib_seq = [0, 1]
    while len(fib_seq) < 195:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    decimal = int(bin_str, 2)

    if decimal % fib_seq[194] == 0:
        return True
    else:
        return False
