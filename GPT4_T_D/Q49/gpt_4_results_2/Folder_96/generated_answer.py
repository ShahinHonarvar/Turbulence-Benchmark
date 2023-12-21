
def if_decimal_is_divisible(bin_str):
    fib_seq = [0, 1]
    index = 1
    while len(fib_seq) < 47:
        fib_seq.append(fib_seq[index] + fib_seq[index-1])
        index += 1
    decimal_num = int(bin_str, 2)
    if decimal_num % fib_seq[46] == 0:
        return True
    else:
        return False
