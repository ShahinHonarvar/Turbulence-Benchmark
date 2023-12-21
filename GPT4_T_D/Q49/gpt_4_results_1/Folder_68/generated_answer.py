
def if_decimal_is_divisible(binary_string):
    dec_num = int(binary_string, 2)
    fib_nums = [0, 1]

    for i in range(2, 38):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])

    if dec_num % fib_nums[37] == 0:
        return True
    else:
        return False
