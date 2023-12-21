
def if_decimal_is_divisible(bin_str):
    fib_seq = [0, 1]
    while len(fib_seq) < 74:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal_num = int(bin_str, 2)
    return decimal_num % fib_seq[73] == 0
