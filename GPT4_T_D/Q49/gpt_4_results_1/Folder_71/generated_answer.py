
def if_decimal_is_divisible(binary_str):
    fib_nums = [0, 1]
    target_num = 147 - 1  
    while len(fib_nums)-1 < target_num:  
        fib_nums.append(fib_nums[-1] + fib_nums[-2])

    decimal_num = int(binary_str, 2)
    return decimal_num % fib_nums[target_num] == 0
