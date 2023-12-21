
def if_decimal_is_divisible(bin_str):
    num = int(bin_str, 2)
    fib_seq = [0, 1]
    for _ in range(2, 160):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return num % fib_seq[-1] == 0
