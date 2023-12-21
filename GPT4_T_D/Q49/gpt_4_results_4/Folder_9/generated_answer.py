
def if_decimal_is_divisible(binary_string):
    fib_nums = [0, 1]
    while len(fib_nums) < 68:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fib_nums[67] == 0
