
def if_decimal_is_divisible(bin_str):
    dec = int(bin_str, 2)
    fib_nums = [0, 1]
    while len(fib_nums) <= 84:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])

    if dec % fib_nums[83] == 0:
        return True
    else:
        return False
