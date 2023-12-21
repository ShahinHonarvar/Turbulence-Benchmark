
def if_decimal_is_divisible(bin_str):
    fib_list = [0, 1]
    while len(fib_list) < 97:
        fib_list.append(fib_list[-1] + fib_list[-2])
    dec_num = int(bin_str, 2)
    return dec_num % fib_list[96] == 0
