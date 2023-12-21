
def if_decimal_is_divisible(bin_num):
    fib_nums = [0, 1]
    num = int(bin_num, 2)
    for i in range(2, 108):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
    
    return num % fib_nums[107] == 0
