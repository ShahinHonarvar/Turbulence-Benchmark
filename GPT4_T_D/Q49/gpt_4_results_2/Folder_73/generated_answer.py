
def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fib_nums = [0, 1]
    while len(fib_nums) < 165:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    return decimal % fib_nums[164] == 0
