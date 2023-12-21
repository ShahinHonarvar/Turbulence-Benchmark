
def if_decimal_is_divisible(bin_str):
    fib_seq = [0, 1]
    for i in range(2, 107 + 1):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    decimal_num = int(bin_str, 2)
    return decimal_num % fib_seq[107] == 0
