
def if_decimal_is_divisible(bin_string):
    fib_nums = [0, 1]
    for _ in range(45):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    dec_num = int(bin_string, 2)
    if dec_num % fib_nums[-1] == 0:
        return True
    else:
        return False
