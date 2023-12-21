
def if_decimal_is_divisible(bin_string):
    dec_int = int(bin_string, 2)
    fib_nums = [0, 1]

    for i in range(2, 90):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])

    if dec_int % fib_nums[-1] == 0:
        return True
    else:
        return False
