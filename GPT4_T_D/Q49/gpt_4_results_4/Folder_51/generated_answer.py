
def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fib_nums = [0, 1]
    for i in range(2, 17):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
    if n % fib_nums[16] == 0:
        return True
    else:
        return False
