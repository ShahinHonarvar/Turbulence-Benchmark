
def if_decimal_is_divisible(bin_str):
    dec_num = int(bin_str, 2)
    fib_sequence = [0, 1]
    for i in range(2, 47):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return dec_num % fib_sequence[-1] == 0
